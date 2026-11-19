## C03 Filtros de Acessibilidade
**Superfície ator:** Web Mobile / Desktop, Consumidor
**Objetivo:** Permitir ao usuário filtrar os pinos no mapa exibindo apenas as categorias que lhe interessam.
**Chega de / vai para:** Chega de C01 (Mapa) -> Vai para C01 (Mapa).
**Mostra:** Lista de checkboxes com as categorias padronizadas do sistema (ex: Rampa, Piso Tátil, Elevador, Banheiro Adaptado).
**Coleta:** `categorias_selecionadas` (array de string, opcional).
**Ações:** 
  - Marcar/Desmarcar categoria -> Alterna o estado visual da opção.
  - Tocar em "Aplicar Filtros" -> Fecha o modal, aciona a API e recarrega os pinos no C01.
  - Tocar em "Limpar" -> Desmarca todas as opções e aplica.
**Estados:** 
  - `sucesso`: painel de filtros visível e interativo.
**Regras:** Se nenhuma categoria estiver selecionada (array vazio), o sistema deve tratar como "mostrar todas".
**Requisitos contrato:** REQ-01 | `GET /api/relatos?categorias={array}`
**Acessibilidade:** Checkboxes com áreas mínimas de toque de 44x44px. Elementos semânticos de `<fieldset>` e `<legend>` para agrupamento em leitores de tela.