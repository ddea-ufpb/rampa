## R03 Formulário de Categoria
**Superfície ator:** Web Mobile, Cidadão
**Objetivo:** Coletar a tipificação do relato de acessibilidade no ponto geográfico escolhido.
**Chega de / vai para:** Chega de R02 -> Vai para R04 (Confirmação)
**Mostra:** Mini-mapa estático com o pino escolhido em R02; lista de categorias disponíveis (Rampa, Piso Tátil, Elevador, Banheiro).
**Coleta:** `categoria` (enum, obrigatório), `descricao_opcional` (texto, opcional).
**Ações:** 
  - Selecionar Categoria -> Habilita botão Enviar
  - Tocar em "Enviar" -> Efetua a requisição de ingestão -> Direciona para R04
  - Tocar em "Voltar" -> Retorna para R02
**Estados:** 
  - `carregando`: botão Enviar em estado de *loading* durante requisição.
  - `sucesso`: transição para R04.
  - `erro`: *toast* vermelho indicando falha na API ou falta de internet.
**Regras:** O usuário deve estar autenticado. A categoria é obrigatória.
**Requisitos contrato:** REQ-02, REQ-03 | `POST /api/relatos`
**Acessibilidade:** Labels claros nas categorias para leitores de tela; contraste adequado nos botões de seleção.