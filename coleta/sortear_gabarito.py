import json
import random

ARQUIVO_CORPUS = "corpus.jsonl"
ARQUIVO_GABARITO = "gabarito.jsonl"
QTD_SORTEIO = 40
SEED = 42


def main() -> None:
    with open(ARQUIVO_CORPUS, "r", encoding="utf-8") as f:
        itens = [json.loads(linha) for linha in f if linha.strip()]

    if len(itens) < QTD_SORTEIO:
        raise ValueError(f"O corpus tem apenas {len(itens)} itens; são necessários {QTD_SORTEIO}.")

    random.seed(SEED)
    sorteados = random.sample(itens, QTD_SORTEIO)
    sorteados.sort(key=lambda x: x["id"])

    with open(ARQUIVO_GABARITO, "w", encoding="utf-8") as f_out:
        for item in sorteados:
            registro_gabarito = {
                "id": item["id"],
                "texto": item["texto"],
                "campos": item["campos"],
                "gabarito": {
                    "tipo_recurso_ou_barreira": "",  # Preencher à mão
                    "confiabilidade": "",            # Preencher à mão
                },
            }
            f_out.write(json.dumps(registro_gabarito, ensure_ascii=False) + "\n")

    print(f"Arquivo '{ARQUIVO_GABARITO}' criado com {len(sorteados)} itens sorteados.")
    print("Próximo passo: abra o arquivo e preencha os campos dentro de 'gabarito' à mão.")


if __name__ == "__main__":
    main()