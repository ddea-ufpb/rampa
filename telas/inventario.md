# Inventário e Navegação

## Quadro de Telas

| ID  | Tela | Ator | Superfície |
|---|---|---|---|
| C01 | Mapa Principal (Consumidor) | Consumidor | Web Mobile / Desktop |
| C02 | Detalhes do Local | Consumidor | Web Mobile / Desktop |
| C03 | Filtros de Acessibilidade | Consumidor | Web Mobile / Desktop |
| R01 | Login/Autenticação | Cidadão (Relator) | Web Mobile |
| R02 | Seleção de Local no Mapa | Cidadão (Relator) | Web Mobile |
| R03 | Formulário de Categoria | Cidadão (Relator) | Web Mobile |
| R04 | Confirmação de Envio | Cidadão (Relator) | Web Mobile |
| R05 | Meus Relatos (Histórico) | Cidadão (Relator) | Web Mobile |
| M01 | Fila de Moderação | Moderador | Web Desktop |
| M02 | Auditoria de Relato | Moderador | Web Desktop |

## Mapa de Navegação
- Fluxo de Consumo: `C01 -> C02 -> C01` | `C01 -> C03 -> C01`
- Fluxo de Relato: `C01 -> R01 -> R02 -> R03 -> R04 -> C01`
- Fluxo de Perfil: `C01 -> R05 -> C01`
- Fluxo de Moderação: `M01 -> M02 -> M01`