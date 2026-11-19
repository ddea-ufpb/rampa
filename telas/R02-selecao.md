## R02 Seleção de Local no Mapa
**Superfície ator:** Web Mobile, Cidadão (Relator)
**Objetivo:** Garantir a precisão máxima (ajuste fino) da coordenada geográfica onde se encontra o recurso de acessibilidade.
**Chega de / vai para:** Chega de R01 -> Vai para R03 (Categoria).
**Mostra:** Mapa em tela cheia com um pino marcador fixo no centro da tela; botão inferior flutuante "Confirmar Local".
**Coleta:** `lat`, `lng` (coordenadas numéricas, obrigatório - geradas pelo centro geométrico do mapa).
**Ações:** 
  - Arrastar mapa -> O mapa se move, o pino fica imóvel no centro, recalculando a coordenada.
  - Tocar em "Confirmar Local" -> Salva a coordenada em estado local e avança para R03.
  - Tocar no botão "Minha Localização" -> Força o mapa a centralizar no GPS do celular.
**Estados:** 
  - `obtendo posição`: tela com alerta ou esqueleto indicando busca do GPS físico do aparelho.
  - `sem permissão`: aviso solicitando ativação de GPS, caso esteja desativado.
  - `offline`: erro de "Sem internet para carregar o mapa".
**Regras:** O usuário deve estar autenticado. As coordenadas não podem ser (0,0).
**Requisitos contrato:** REQ-03 | Apenas gerenciamento de estado local (SPA); sem chamada à API no momento.
**Acessibilidade:** Prompt visual legível indicando "Arraste o mapa para ajustar o pino".