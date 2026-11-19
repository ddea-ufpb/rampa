## R04 Confirmação de Envio
**Superfície ator:** Web Mobile, Cidadão (Relator)
**Objetivo:** Fornecer feedback positivo de conclusão do fluxo de relato e comunicar a existência da fila de moderação.
**Chega de / vai para:** Chega de R03 (via resposta HTTP 202) -> Vai para C01 (Início).
**Mostra:** Ilustração amigável de sucesso, título "Relato Enviado!", texto explicativo "Obrigado por colaborar. Seu relato está em análise pela nossa equipe e logo aparecerá no mapa."
**Coleta:** Nenhuma.
**Ações:** 
  - Tocar em "Voltar ao Mapa" -> Retorna a navegação normal no C01.
**Estados:** 
  - `sucesso`: tela estática de confirmação.
**Regras:** Esta tela só deve ser renderizada se a API retornar HTTP 202/201.
**Requisitos contrato:** REQ-02 (Validação do status pendente criado no backend).
**Acessibilidade:** Foco dinâmico redirecionado automaticamente para o texto de sucesso para que o leitor de tela (VoiceOver/TalkBack) verbalize a vitória imediatamente.