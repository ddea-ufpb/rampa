import hashlib
import json
import os
import re
import time
import urllib.parse
import urllib.request
from datetime import date

OVERPASS_URL = "https://overpass-api.de/api/interpreter"
DATA_COLETA = date.today().isoformat()  # AAAA-MM-DD
ARQUIVO_BRUTO = f"bruto/osm_jp_{DATA_COLETA}.json"
ARQUIVO_CORPUS = "corpus.jsonl"
ARQUIVO_DESCARTES = "descartes.jsonl"
ARQUIVO_REGRAS = "REGRAS.md"

TAGS_ACESSIBILIDADE = ("wheelchair", "tactile_paving", "kerb", "ramp")
VALORES_INVALIDOS = {"", "unknown", "fixme", "none", "?", "undefined"}

ESTATISTICAS_REGRAS = {
    "R01_DESCARTE_SEM_COORDENADAS": {
        "descricao": "Descarta registros sem latitude/longitude ou centroide válido.",
        "afetados": 0,
        "exemplo_id": None,
    },
    "R02_DESCARTE_SEM_TAG_ACESSIBILIDADE": {
        "descricao": "Descarta registros que não possuem nenhuma das tags alvo (wheelchair, tactile_paving, kerb, ramp).",
        "afetados": 0,
        "exemplo_id": None,
    },
    "R03_DESCARTE_VALOR_INDEFINIDO": {
        "descricao": "Descarta registros cuja tag de acessibilidade contém apenas valores vagos ('unknown', 'fixme', '?').",
        "afetados": 0,
        "exemplo_id": None,
    },
    "R04_NORMALIZAR_TEXTO": {
        "descricao": "Colapsa espaços múltiplos, remove quebras de linha e preenche nome ausente como 'Sem nome registrado'.",
        "afetados": 0,
        "exemplo_id": None,
    },
    "R05_NORMALIZAR_TAGS": {
        "descricao": "Converte valores das tags de acessibilidade para minúsculas e remove espaços nas extremidades.",
        "afetados": 0,
        "exemplo_id": None,
    },
    "R06_NORMALIZAR_COORDENADAS": {
        "descricao": "Converte latitude e longitude para float arredondado em 6 casas decimais.",
        "afetados": 0,
        "exemplo_id": None,
    },
}


def registrar_regra(codigo: str, osm_ref: str) -> None:
    ESTATISTICAS_REGRAS[codigo]["afetados"] += 1
    if ESTATISTICAS_REGRAS[codigo]["exemplo_id"] is None:
        ESTATISTICAS_REGRAS[codigo]["exemplo_id"] = osm_ref


# 1. OBTER:
def obter(origem: str) -> str:
    os.makedirs("bruto", exist_ok=True)
    if os.path.exists(ARQUIVO_BRUTO):
        print(f"[OBTER] Arquivo bruto já existe em {ARQUIVO_BRUTO}. Reutilizando...")
        return ARQUIVO_BRUTO

    query = """
    [out:json][timeout:60];
    area["name"="João Pessoa"]["admin_level"="8"]->.searchArea;
    (
      node["wheelchair"](area.searchArea);
      way["wheelchair"](area.searchArea);
      node["tactile_paving"](area.searchArea);
      way["tactile_paving"](area.searchArea);
      node["kerb"](area.searchArea);
      way["kerb"](area.searchArea);
      node["ramp"](area.searchArea);
      way["ramp"](area.searchArea);
    );
    out center tags;
    """
    print("[OBTER] Consultando Overpass API (aguardando intervalo de cortesia de 2s)...")
    time.sleep(2)

    dados_post = urllib.parse.urlencode({"data": query}).encode("utf-8")
    req = urllib.request.Request(
        origem,
        data=dados_post,
        headers={"User-Agent": "Rampa-DINF00071-Coletor/1.0"},
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        conteudo = resp.read().decode("utf-8")

    with open(ARQUIVO_BRUTO, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"[OBTER] Dados brutos salvos em {ARQUIVO_BRUTO}")
    return ARQUIVO_BRUTO


# 2. EXTRAIR: 
def extrair(caminho_bruto: str) -> list[dict]:
    with open(caminho_bruto, "r", encoding="utf-8") as f:
        dados = json.load(f)
    elementos = dados.get("elements", [])
    print(f"[EXTRAIR] {len(elementos)} elementos extraídos do bruto.")
    return elementos


def limpar_texto(valor: str) -> str:
    return re.sub(r"\s+", " ", valor).strip()


# 3. NORMALIZAR: aplica regras explícitas ou retorna DESCARTE com motivo
def normalizar(registro: dict) -> tuple[bool, dict]:
    osm_type = registro.get("type", "desconhecido")
    osm_id = registro.get("id", "0")
    osm_ref = f"{osm_type}/{osm_id}"
    tags = registro.get("tags", {})

    # Regra 1: Coordenadas obrigatórias (diretas em node ou center em way)
    lat = registro.get("lat") or registro.get("center", {}).get("lat")
    lon = registro.get("lon") or registro.get("center", {}).get("lon")
    if lat is None or lon is None:
        registrar_regra("R01_DESCARTE_SEM_COORDENADAS", osm_ref)
        return False, {"fonte": f"{ARQUIVO_BRUTO}:{osm_ref}", "motivo": "coordenadas ausentes"}

    # Regra 2: Pelo menos uma tag de acessibilidade presente
    tags_presentes = {k: tags[k] for k in TAGS_ACESSIBILIDADE if k in tags}
    if not tags_presentes:
        registrar_regra("R02_DESCARTE_SEM_TAG_ACESSIBILIDADE", osm_ref)
        return False, {"fonte": f"{ARQUIVO_BRUTO}:{osm_ref}", "motivo": "tag de acessibilidade ausente"}

    # Regra 5: Normalizar valores das tags
    tags_norm = {}
    for k, v in tags_presentes.items():
        v_limpo = limpar_texto(str(v)).lower()
        if v_limpo != str(v):
            registrar_regra("R05_NORMALIZAR_TAGS", osm_ref)
        if v_limpo not in VALORES_INVALIDOS:
            tags_norm[k] = v_limpo

    # Regra 3: Descartar se sobrou apenas valor vago/indefinido
    if not tags_norm:
        registrar_regra("R03_DESCARTE_VALOR_INDEFINIDO", osm_ref)
        return False, {
            "fonte": f"{ARQUIVO_BRUTO}:{osm_ref}",
            "motivo": f"valor de acessibilidade indefinido ({tags_presentes})",
        }

    # Regra 6: Normalizar coordenadas
    lat_f = round(float(lat), 6)
    lon_f = round(float(lon), 6)
    registrar_regra("R06_NORMALIZAR_COORDENADAS", osm_ref)

    # Regra 4: Normalizar texto livre que será julgado pelo LLM na Etapa 2
    nome_bruto = tags.get("name", "")
    nome_limpo = limpar_texto(nome_bruto) if nome_bruto else "Sem nome registrado"
    tipo_local = (
        tags.get("amenity")
        or tags.get("highway")
        or tags.get("shop")
        or tags.get("building")
        or tags.get("leisure")
        or "local_urbano"
    )
    descricao_bruta = tags.get("description") or tags.get("wheelchair:description") or ""
    descricao_limpa = limpar_texto(descricao_bruta)

    if nome_bruto != nome_limpo or descricao_bruta != descricao_limpa:
        registrar_regra("R04_NORMALIZAR_TEXTO", osm_ref)

    partes_texto = [f"Local: {nome_limpo}", f"Tipo: {tipo_local}", f"Tags: {json.dumps(tags_norm, ensure_ascii=False)}"]
    if descricao_limpa:
        partes_texto.append(f"Observação: {descricao_limpa}")
    texto_final = " | ".join(partes_texto)

    item_normalizado = {
        "texto": texto_final,
        "campos": {
            "osm_ref": osm_ref,
            "nome": nome_limpo,
            "tipo_local": limpar_texto(str(tipo_local)).lower(),
            "latitude": lat_f,
            "longitude": lon_f,
            "tags_acessibilidade": tags_norm,
            "observacao": descricao_limpa or None,
        },
        "fonte": f"{ARQUIVO_BRUTO}:{osm_ref}",
        "coletado_em": DATA_COLETA,
    }
    return True, item_normalizado


# 4. DEDUPLICAR:
def chave(registro_normalizado: dict) -> str:
    campos = registro_normalizado["campos"]
    base = f"{campos['osm_ref']}|{campos['latitude']}|{campos['longitude']}|{json.dumps(campos['tags_acessibilidade'], sort_keys=True)}"
    return hashlib.sha256(base.encode("utf-8")).hexdigest()[:16]


# 5. GRAVAR: 
def gravar(validos: list[dict], descartados: list[dict]) -> None:
    chaves_existentes = set()
    total_existente = 0

    if os.path.exists(ARQUIVO_CORPUS):
        with open(ARQUIVO_CORPUS, "r", encoding="utf-8") as f:
            for linha in f:
                if linha.strip():
                    dado = json.loads(linha)
                    chaves_existentes.add(dado["chave"])
                    total_existente += 1

    novos_gravados = 0
    with open(ARQUIVO_CORPUS, "a", encoding="utf-8") as f_corpus:
        for item in validos:
            h = chave(item)
            if h in chaves_existentes:
                continue
            chaves_existentes.add(h)
            seq = total_existente + novos_gravados + 1
            registro_final = {
                "id": f"rampa-{DATA_COLETA[:4]}-{seq:06d}",
                "texto": item["texto"],
                "campos": item["campos"],
                "fonte": item["fonte"],
                "coletado_em": item["coletado_em"],
                "chave": h,
            }
            f_corpus.write(json.dumps(registro_final, ensure_ascii=False) + "\n")
            novos_gravados += 1

    with open(ARQUIVO_DESCARTES, "w", encoding="utf-8") as f_desc:
        for desc in descartados:
            f_desc.write(json.dumps(desc, ensure_ascii=False) + "\n")

    with open(ARQUIVO_REGRAS, "w", encoding="utf-8") as f_reg:
        f_reg.write("# Regras de Normalização e Descarte (Etapa 1)\n\n")
        f_reg.write("| Código | Regra | Item do bruto que motivou | Itens afetados |\n")
        f_reg.write("| :--- | :--- | :--- | :--- |\n")
        for codigo, info in ESTATISTICAS_REGRAS.items():
            ex = info["exemplo_id"] or "Nenhum registro disparou"
            f_reg.write(f"| `{codigo}` | {info['descricao']} | `{ex}` | {info['afetados']} |\n")

    print(f"[GRAVAR] Novos itens adicionados ao {ARQUIVO_CORPUS}: {novos_gravados} (Total no arquivo: {total_existente + novos_gravados})")
    print(f"[GRAVAR] Itens descartados registrados em {ARQUIVO_DESCARTES}: {len(descartados)}")
    print(f"[GRAVAR] Relatório de regras atualizado em {ARQUIVO_REGRAS}")


def main() -> None:
    caminho_bruto = obter(OVERPASS_URL)
    elementos = extrair(caminho_bruto)

    validos = []
    descartados = []
    for el in elementos:
        ok, resultado = normalizar(el)
        if ok:
            validos.append(resultado)
        else:
            descartados.append(resultado)

    gravar(validos, descartados)


if __name__ == "__main__":
    main()