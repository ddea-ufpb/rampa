## R05 Meus Relatos
**Superfície ator:** Web Mobile, Cidadão (Relator)
**Objetivo:** Permitir ao cidadão acompanhar o histórico de suas próprias contribuições e entender o trabalho de moderação.
**Chega de / vai para:** Chega de C01 (via Menu Principal) -> Vai para C01.
**Mostra:** Lista vertical (cards) dos relatos submetidos. Cada item apresenta a Categoria, a Data e uma *tag* visual com o Status (Pendente, Aprovado, Rejeitado).
**Coleta:** Nenhuma.
**Ações:** 
  - Tocar em "Voltar" -> Volta ao mapa (C01).
**Estados:** 
  - `carregando`: esqueletos simulando os cards.
  - `vazio`: ilustração e texto "Você ainda não enviou nenhum relato".
  - `erro`: falha ao buscar os dados na rede.
  - `sucesso`: listagem preenchida.
**Regras:** Endpoint seguro: o backend deve filtrar os dados baseando-se unicamente no ID do token do usuário logado (nunca confiar no frontend para mandar o ID de busca).
**Requisitos contrato:** Vinculado ao REQ-05 | `GET /api/relatos/meus`
**Acessibilidade:** Não depender apenas da cor para indicar o status; o texto (ex: "Pendente") deve ser renderizado dentro do badge e não apenas uma "bolinha laranja".