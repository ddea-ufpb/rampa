## R01 Login / Autenticação
**Superfície ator:** Web Mobile, Cidadão (Relator)
**Objetivo:** Identificar e validar o cidadão antes de permitir a submissão de novos dados ao sistema.
**Chega de / vai para:** Chega de C01 -> Vai para R02 (Seleção de Local).
**Mostra:** Logotipo do projeto, formulário de e-mail e senha, botão de confirmação e link de "Criar conta".
**Coleta:** `email` (email, obrigatório), `senha` (password, obrigatório).
**Ações:** 
  - Tocar em "Entrar" -> Valida credenciais -> Redireciona para R02 com token de sessão.
  - Tocar em "Voltar" -> Retorna ao mapa C01 sem autenticar.
**Estados:** 
  - `carregando`: spinner no botão "Entrar" enquanto comunica com a API.
  - `erro`: mensagem de texto em vermelho "Credenciais inválidas" ou "Erro de conexão".
  - `sucesso`: transição de tela.
**Regras:** Inputs não podem ser submetidos em branco. O acesso posterior à fila de criação requer token válido.
**Requisitos contrato:** Vinculado ao REQ-05 (Segurança de rotas) | `POST /api/auth/login`
**Acessibilidade:** Inputs contêm o atributo HTML `autocomplete` apropriado (`email`, `current-password`) para facilitar preenchimento via gerenciador de senhas.