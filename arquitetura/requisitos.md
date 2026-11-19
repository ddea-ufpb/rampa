# Requisitos (Sintaxe EARS)

- **REQ-01** (Ubíquo): O SISTEMA DEVE fornecer uma representação visual (mapa) contendo os relatos de acessibilidade.
- **REQ-02** (Evento): QUANDO o Relator enviar um novo formulário de relato, O SISTEMA DEVE gravar o status do relato inicial como "pendente".
- **REQ-03** (Indesejado): SE um payload de ingestão de relato chegar sem os campos obrigatórios de `latitude`, `longitude` ou `categoria`, ENTÃO O SISTEMA DEVE recusar a requisição com código HTTP 422 Unprocessable Entity.
- **REQ-04** (Estado): ENQUANTO o status de um relato for "pendente" ou "rejeitado", O SISTEMA DEVE ocultá-lo da consulta pública no mapa do Consumidor.
- **REQ-05** (Opcional): ONDE um usuário autenticado possuir o perfil (role) de 'Moderador', O SISTEMA DEVE permitir o acesso à rota de alteração de status (aprovar/rejeitar).