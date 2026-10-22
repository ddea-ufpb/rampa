# Rampa

Mapa colaborativo de acessibilidade urbana: o que é possível atravessar, entrar e usar na cidade —
dito por quem precisa disso todo dia.

> **Status:** repositório recém-criado. Nenhuma linha de aplicação escrita. Este README existe para
> receber os artefatos que alimentam o `/paul:init` de cada módulo.
>
> **Disciplina:** DINF00071 — Desenvolvimento Dirigido por Especificação com Agentes · CI/UFPB · 2026.2

---

## O problema

Para quem usa cadeira de rodas, anda com dificuldade ou não enxerga, sair de casa é um cálculo de
risco feito sem dados: não dá para saber de antemão se a calçada tem rebaixamento, se a rampa
termina num degrau, se o banheiro é utilizável, se o elevador funciona. A informação existe —
está na cabeça de quem já tentou — e não está em lugar nenhum consultável.

O resultado é que a pessoa descobre a barreira quando já está na frente dela.

## O que o sistema faz

Qualquer pessoa relata a condição de acessibilidade de um ponto, por categoria. Os relatos passam
por moderação e por uma regra de confiabilidade que leva em conta concordância e tempo — porque uma
rampa quebrada é consertada e um relato de dois anos atrás pode estar errado. O resultado é um mapa
consultável por tipo de necessidade.

## Quem usa

| Papel | O que precisa |
|---|---|
| Pessoa com deficiência | Saber antes de sair se o caminho e o destino são utilizáveis |
| Acompanhante ou cuidador | Planejar o trajeto com antecedência |
| Gestor urbano | Ver onde estão as barreiras reclamadas e priorizar obra |

## Fora de escopo (preliminar — o grupo fecha e justifica)

- Roteamento ponta a ponta com navegação em tempo real: depende de base de calçadas que não existe.
- Avaliação técnica de conformidade com norma: o relato é experiência de uso, não laudo.
- Denúncia formal a órgão público: o sistema informa, não aciona.
- Dados médicos ou de deficiência do usuário: o sistema não pergunta quem você é.

## Módulos

Um repositório, quatro módulos independentes. Cada módulo tem persistência, API, componente
concorrente, desempenho medido e testes — os cinco, sozinho.

| # | Módulo | Responsável | O que faz |
|---|---|---|---|
| 1 | `relato` | *a definir* | Recebe o relato geolocalizado por categoria, valida e persiste |
| 2 | `moderacao` | *a definir* | Fila de revisão, detecção de duplicata, concordância entre relatos e decaimento no tempo |
| 3 | `consulta` | *a definir* | Busca geoespacial e filtros por tipo de acessibilidade; API pública |
| 4 | `mapa` | *a definir* | Visualização, agregação por região e exportação para o gestor |

**Contrato principal:** o relato com seu grau de confiabilidade. Relato publica; moderação atribui
confiança; consulta e mapa leem — e nunca recalculam confiança por conta própria.

**O decaimento é requisito, não enfeite:** sem ele, o mapa envelhece e passa a mentir — e mentir
sobre acessibilidade manda alguém para uma viagem perdida.

## Dados e privacidade

O relato é sobre **lugar**, não sobre pessoa. Decisões preliminares:

- Não se coleta condição, deficiência ou dado de saúde de quem relata.
- Relato anônimo por padrão; identificação só se o usuário quiser acompanhar o que reportou.
- Fotos do ponto, se houver, não podem expor pessoas — mesma regra de armazenamento privado.
- A contagem de relatos por região é pública; quem relatou, não.

**Dados:** gerados pelos usuários, com possível enriquecimento de base aberta de logradouros.
Para demonstrar o sistema antes de haver massa crítica, prevê-se semente sintética — declarada como
tal na interface.

## Estrutura do repositório

```
rampa/
├── README.md              # este arquivo — brief do projeto
├── CONTRATOS.md           # FI-02: módulos, contratos e duplos
├── modulos/
│   ├── relato/     .paul/
│   ├── moderacao/  .paul/
│   ├── consulta/   .paul/
│   └── mapa/       .paul/
└── .gitignore             # .claude/ fora do versionamento
```

## Artefatos de entrada do `/paul:init`

O init de cada módulo só roda depois que isto estiver no repositório:

- [ ] **FI-01 de cada integrante**, com as seções 7 e 8 escritas no nível do módulo
- [ ] **CONTRATOS.md** do grupo: os quatro módulos, os contratos entre pares que se tocam e o duplo de cada contrato
- [ ] **Teste de independência** respondido por cada integrante
- [ ] **Telas do sistema** (Trabalho 1): no mínimo dez, como mock, descrição detalhada ou desenho
- [ ] **Artefatos de arquitetura** (Trabalho 1): padrão de especificação escolhido, justificativa e os artefatos produzidos

## Como o trabalho é conduzido

Cada módulo roda o ciclo **Plan → Audit → Apply → Unify**: o plano declara critérios de aceitação
verificáveis, a auditoria revisa antes de qualquer código, a execução segue o plano aprovado e o
fechamento compara planejado com entregue.

A **Fase 1 (Fundação)** é a mesma para todos os projetos da turma: scaffold com CI que falha quando
deve, banco com as restrições de dados no schema, e deploy que só publica com o CI verde. A
diferença entre os projetos começa na Fase 2.

## Licença

MIT.
