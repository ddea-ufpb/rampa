## C02 Detalhes do Local
**Superfície ator:** Web Mobile / Desktop, Consumidor
**Objetivo:** Mostrar as informações detalhadas de um ponto de acessibilidade selecionado no mapa.
**Chega de / vai para:** Chega de C01 (Mapa) -> Vai para C01 (Fechar) ou aplicativo externo de rotas.
**Mostra:** Categoria da infraestrutura, data da postagem, autor (anonimizado ou primeiro nome), coordenadas (ou endereço aproximado) e botão para traçar rota.
**Coleta:** Nenhuma.
**Ações:** 
  - Tocar em "Como chegar" -> Abre aplicativo de rotas nativo do dispositivo (Google Maps/Waze/Apple Maps).
  - Tocar em "Fechar" (ou X) -> Fecha o modal/tela e volta para C01.
**Estados:** 
  - `carregando`: esqueleto de dados (skeleton loading) se precisar buscar dados complementares.
  - `sucesso`: modal renderizado na tela.
  - `erro`: mensagem genérica caso o relato não seja encontrado (ex: foi excluído recentemente).
**Regras:** Só pode exibir os detalhes se o status do relato for "aprovado".
**Requisitos contrato:** REQ-04 | `GET /api/relatos/{id}`
**Acessibilidade:** Ao abrir, o leitor de tela deve mover o foco automaticamente para o título do modal (nome da categoria).