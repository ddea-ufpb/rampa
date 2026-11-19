```yaml
openapi: 3.1.0
info:
  title: API Rampa - Mapa de Acessibilidade
  version: 1.0.0
  description: Contratos de comunicação entre as telas (Cidadão, Consumidor, Moderador) e o backend.

paths:
  /auth/login:
    post:
      summary: Autenticar utilizador no sistema
      operationId: autenticar_usuario
      description: Ação disparada pela tela R01 (Login).
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - email
                - senha
              properties:
                email:
                  type: string
                  format: email
                senha:
                  type: string
                  format: password
      responses:
        '200':
          description: Autenticação bem-sucedida. Retorna o token.
        '401':
          description: Credenciais inválidas.

  /relatos:
    post:
      summary: Criação de um novo relato de acessibilidade
      operationId: submit_report
      description: Ação disparada pela tela R03 (Formulário).
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/NovoRelato'
      responses:
        '201':
          description: Relato criado e inserido na fila de moderação.
        '422':
          description: Erro de validação.
          
    get:
      summary: Consulta de relatos aprovados
      operationId: get_relatos
      description: Ação disparada pelas telas C01 (Mapa) e C03 (Filtros).
      parameters:
        - name: categoria
          in: query
          required: false
          schema:
            type: string
            enum: [rampa, piso_tatil, elevador, banheiro]
      responses:
        '200':
          description: Lista de relatos geolocalizados e aprovados.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Relato'

  /relatos/{id}:
    get:
      summary: Detalhes de um relato específico
      operationId: get_detalhe_relato
      description: Ação disparada pelas telas C02 (Detalhes Local) e M02 (Auditoria).
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Dados completos do relato selecionado.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Relato'

  /relatos/meus:
    get:
      summary: Histórico do cidadão
      operationId: get_meus_relatos
      description: Ação disparada pela tela R05 (Meus Relatos).
      responses:
        '200':
          description: Lista de todos relatos enviados pelo utilizador logado.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Relato'

  /moderacao/fila:
    get:
      summary: Listar relatos pendentes
      operationId: get_fila_moderacao
      description: Ação disparada pela tela M01 (Fila de Moderação).
      responses:
        '200':
          description: Lista de relatos com status 'pendente'.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Relato'

  /moderacao/relatos/{id}:
    patch:
      summary: Avaliar relato (Aprovar/Rejeitar)
      operationId: avaliar_relato
      description: Ação disparada pela tela M02 (Auditoria de Relato).
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  enum: [aprovado, rejeitado]
      responses:
        '200':
          description: Status atualizado com sucesso.

components:
  schemas:
    NovoRelato:
      type: object
      required:
        - latitude
        - longitude
        - categoria
      properties:
        latitude:
          type: number
          format: float
        longitude:
          type: number
          format: float
        categoria:
          type: string
          enum: [rampa, piso_tatil, elevador, banheiro]
          
    Relato:
      type: object
      properties:
        id:
          type: string
          format: uuid
        latitude:
          type: number
          format: float
        longitude:
          type: number
          format: float
        categoria:
          type: string
        status:
          type: string
          enum: [pendente, aprovado, rejeitado]
        data_envio:
          type: string
          format: date-time
```