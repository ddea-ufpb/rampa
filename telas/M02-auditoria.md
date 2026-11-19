## M02 Auditoria de Relato
**Superfície ator:** Web Desktop, Moderador
**Objetivo:** Fornecer dados para o moderador deliberar sobre a veracidade ou inadequação de um relato específico que está na fila.
**Chega de / vai para:** Chega de M01 -> Vai para M01.
**Mostra:** Mini-mapa exibindo o ponto geográfico, Categoria relatada, E-mail/Nome do autor, Data, e dois botões fixos em evidência: "Aprovar" (Verde) e "Rejeitar" (Vermelho).
**Coleta:** Ações de clique, e, opcionalmente, `motivo_rejeicao` (campo de texto, em caso de rejeição).
**Ações:** 
  - Tocar em "Aprovar" -> Dispara requisição PATCH aprovando -> Volta à lista M01.
  - Tocar em "Rejeitar" -> Dispara requisição PATCH rejeitando -> Volta à lista M01.
  - Tocar em "Voltar" -> Descarta visualização -> Volta à lista M01.
**Estados:** 
  - `carregando`: botão pressionado assume ícone de carregamento durante a operação PATCH.
  - `erro`: alerta *toast* se ocorrer falha na aprovação ou expiração da sessão do admin.
**Regras:** Proteção rigorosa de rotas (Admin apenas). Após o envio da ação, o relato sai do escopo da moderação.
**Requisitos contrato:** REQ-05 | `PATCH /api/relatos/{id}/status`
**Acessibilidade:** Suporte a teclas de atalho (*Shortcuts*) para agilizar a moderação (Ex: Tecla "A" aprova, Tecla "R" rejeita, Esc cancela).