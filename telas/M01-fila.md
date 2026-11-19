## M01 Fila de Moderação
**Superfície ator:** Web Desktop, Moderador
**Objetivo:** Listar todos os relatos pendentes para curadoria e aprovação/rejeição.
**Chega de / vai para:** Chega via URL (Login Admin) -> Vai para M02 (Auditoria)
**Mostra:** Tabela/Lista em tempo real dos relatos com `status=pendente`, exibindo Data, Categoria, Autor e um botão de ação.
**Coleta:** Nenhuma entrada de texto; apenas cliques de ação.
**Ações:** 
  - Tocar em "Auditar" em uma linha -> Abre M02 com os dados do relato.
  - Tocar em "Aprovar Rápido" -> Atualiza status para aprovado -> Mantém na tela.
**Estados:** 
  - `carregando`: esqueleto de tabela (skeleton loading).
  - `vazio`: "Parabéns, a fila está zerada!".
  - `erro`: mensagem de falha ao buscar a fila.
**Regras:** Somente usuários com *role* de moderador podem acessar. Os itens devem vir ordenados do mais antigo para o mais novo (FIFO).
**Requisitos contrato:** REQ-05 | `GET /api/moderacao/pendentes` | `PATCH /api/relatos/{id}/status`
**Acessibilidade:** Navegação completa por teclado via *Tab* para rolar a tabela e acionar botões.