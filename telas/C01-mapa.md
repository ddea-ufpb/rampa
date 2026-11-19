## C01 Mapa Principal
**Superfície ator:** Web Mobile, Consumidor e Cidadão
**Objetivo:** Permitir a visualização imediata dos pontos de acessibilidade ao redor do usuário.
**Chega de / vai para:** Chega direto via URL (Início) -> Vai para C02 (Detalhes), C03 (Filtros), R01 (Novo Relato)
**Mostra:** Mapa base cartográfico, marcador de localização atual do usuário, pinos dos relatos aprovados por categoria (cores diferentes).
**Coleta:** Posição GPS do dispositivo (opcional, sob permissão).
**Ações:** 
  - Tocar em um pino -> Abre detalhes (C02)
  - Tocar no botão "Filtros" -> Abre modal de filtros (C03)
  - Tocar no botão flutuante "+" -> Inicia fluxo de relato (R01/R02)
  - Tocar em "Minha Localização" -> Centraliza o mapa na `lat`/`lng` do usuário
**Estados:** 
  - `carregando`: mapa em cinza com spinner.
  - `sucesso`: pinos renderizados.
  - `offline`: banner "Sem conexão, mostrando dados em cache".
  - `sem permissão`: aviso amigável sugerindo ativar o GPS.
**Regras:** Pinos exibidos devem ser limitados a um raio de 5km da visão atual para economizar banda; apenas relatos com status "aprovado" são renderizados.
**Requisitos contrato:** REQ-01, REQ-04 | `GET /api/relatos?bbox={limites}`
**Acessibilidade:** Leitores de tela devem ler a quantidade de pontos encontrados na visão atual ao finalizar o carregamento. Botões com no mínimo 48x48px.