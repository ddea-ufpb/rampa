# Cenários de Qualidade

## 1. Persistência
* **Fonte:** Módulo de ingestão de dados (API).
* **Estímulo:** Salvar um novo relato de acessibilidade com coordenadas geográficas.
* **Ambiente:** Operação normal no banco de dados PostgreSQL com extensão PostGIS.
* **Artefato:** Tabela de Relatos no Banco de Dados.
* **Resposta:** O relato é persistido utilizando o tipo espacial `Geometry` (Point), vinculando a latitude e longitude corretamente.
* **Medida:** 100% dos relatos persistidos estão aptos para consultas geoespaciais radiais ("perto de mim").

## 2. API com contrato
* **Fonte:** Interface cliente (ex: R03 - Formulário).
* **Estímulo:** Envio de um payload JSON para o endpoint de criação de relatos.
* **Ambiente:** Operação normal do sistema.
* **Artefato:** Endpoint `submit_report` (definido no contrato `openapi-rampa.md`).
* **Resposta:** A API FastAPI intercepta e valida estritamente a requisição contra o schema `NovoRelato` antes de executar qualquer lógica de negócio.
* **Medida:** 0 requisições fora do contrato são processadas; requisições malformadas recebem erro HTTP 422 em tempo real.

## 3. Concorrência
* **Fonte:** Múltiplos cidadãos (Relatores) operando na rua.
* **Estímulo:** Ingestão de centenas de relatos simultâneos sobre um mesmo local ou evento.
* **Ambiente:** Pico de uso com alta carga de submissões simultâneas.
* **Artefato:** Fluxo de fila assíncrona (Redis) e banco de dados.
* **Resposta:** O sistema enfileira as requisições assincronamente, gravando os relatos com status "pendente" para a tela M01, evitando contenção e deadlocks no banco.
* **Medida:** 0 relatos perdidos (garantia de vivacidade) e nenhum conflito de gravação durante picos de até 500 req/s.

## 4. Desempenho medido
* **Fonte:** Consumidores do sistema visualizando o mapa.
* **Estímulo:** Requisição em massa buscando relatos aprovados em uma determinada área.
* **Ambiente:** Teste de carga simulado com a ferramenta Locust.
* **Artefato:** Endpoint geoespacial `get_relatos` (`openapi-rampa.md`).
* **Resposta:** O sistema consulta o PostGIS, processa o filtro de categoria e retorna o array JSON com os pinos.
* **Medida:** A latência no percentil 95 (p95) deve ser estritamente < 500ms para manter a usabilidade da aplicação mobile.

## 5. Testes
* **Fonte:** Desenvolvedor ou ferramenta de integração contínua (CI/CD).
* **Estímulo:** Execução da suíte de testes automatizados com o framework Pytest.
* **Ambiente:** Ambiente de testes e empacotamento Docker.
* **Artefato:** Código-fonte da aplicação (Backend).
* **Resposta:** Os testes enviam requisições simuladas, validando as respostas baseadas no contrato OpenAPI e as restrições do banco.
* **Medida:** Sucesso obrigatório em 100% dos testes que envolvem regras críticas de negócio (como a fila de moderação).