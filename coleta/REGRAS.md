# Regras de Normalização e Descarte (Etapa 1)

| Código | Regra | Item do bruto que motivou | Itens afetados |
| :--- | :--- | :--- | :--- |
| `R01_DESCARTE_SEM_COORDENADAS` | Descarta registros sem latitude/longitude ou centroide válido. | `Nenhum registro disparou` | 0 |
| `R02_DESCARTE_SEM_TAG_ACESSIBILIDADE` | Descarta registros que não possuem nenhuma das tags alvo (wheelchair, tactile_paving, kerb, ramp). | `Nenhum registro disparou` | 0 |
| `R03_DESCARTE_VALOR_INDEFINIDO` | Descarta registros cuja tag de acessibilidade contém apenas valores vagos ('unknown', 'fixme', '?'). | `Nenhum registro disparou` | 0 |
| `R04_NORMALIZAR_TEXTO` | Colapsa espaços múltiplos, remove quebras de linha e preenche nome ausente como 'Sem nome registrado'. | `node/2531341360` | 237 |
| `R05_NORMALIZAR_TAGS` | Converte valores das tags de acessibilidade para minúsculas e remove espaços nas extremidades. | `Nenhum registro disparou` | 0 |
| `R06_NORMALIZAR_COORDENADAS` | Converte latitude e longitude para float arredondado em 6 casas decimais. | `node/1028957865` | 433 |
