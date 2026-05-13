# 🛡️ 3. Segurança da Informação

Este documento detalha o planejamento de segurança, análise de riscos e conformidade legal da SecureTech Solutions, focando em garantir a integridade, disponibilidade e confidencialidade dos dados corporativos e de clientes.

---

## 3.1 Mapeamento de Ameaças e Matriz GUT

Realizámos o mapeamento proativo das vulnerabilidades que podem comprometer a infraestrutura da SecureTech Solutions e dos seus clientes. Utilizámos a Matriz GUT (Gravidade, Urgência e Tendência) para quantificar matematicamente a prioridade de cada correção, focando no que gera maior impacto operacional e financeiro.

| Ameaça / Vulnerabilidade                                                                                     |  G  |  U  |  T  |  Total  |
| :----------------------------------------------------------------------------------------------------------- | :-: | :-: | :-: | :-----: |
| **Quebra de Controlo de Acesso (IDOR):** Um cliente altera parâmetros no URL e visualiza dados de terceiros. |  5  |  5  |  5  | **125** |
| **Falhas Criptográficas:** Palavras-passe de acesso remoto salvas na base de dados sem encriptação.          |  5  |  5  |  4  | **100** |
| **Backups Expostos (S3 Aberto):** Rotinas de backup em buckets públicos sem restrição de acesso.             |  5  |  5  |  4  | **100** |
| **Injection (SQL Injection no Login):** Manipulação de formulários para extrair a tabela de utilizadores.    |  4  |  5  |  4  | **80**  |
| **Falhas de Autenticação:** Acesso a painéis críticos com credenciais fracas e sem MFA.                      |  4  |  4  |  5  | **80**  |
| **Ataque de Ransomware (Phishing):** Malware que se propaga pela VPN a partir da máquina de um técnico.      |  5  |  4  |  4  | **80**  |
| **Configuração Insegura:** Dashboards de monitorização com credenciais padrão (admin/admin).                 |  4  |  5  |  3  | **60**  |
| **Componentes Desatualizados:** Servidor vulnerável a execução remota de código (RCE).                       |  4  |  4  |  3  | **48**  |
| **Ataque DDoS:** Sobrecarga intencional do portal, causando indisponibilidade e quebra de SLA.               |  4  |  4  |  3  | **48**  |
| **Rate Limiting Inexistente:** Ausência de bloqueio após múltiplas tentativas falhadas de login.             |  3  |  4  |  4  | **48**  |
| **Falha em Logs:** O sistema não regista quando ocorre um download massivo da base de clientes.              |  3  |  3  |  5  | **45**  |
| **Supply Chain (Integridade):** Atualização maliciosa em software de terceiros utilizado pela empresa.       |  5  |  3  |  3  | **45**  |
| **SSRF:** Exploração de ferramentas de diagnóstico para descobrir chaves de API internas.                    |  4  |  3  |  3  | **36**  |
| **Sequestro de Sessão:** Roubo de cookies de sessão em redes Wi-Fi públicas.                                 |  4  |  3  |  3  | **36**  |
| **Vazamento de Dados por API:** API a retornar dados excessivos de clientes numa única requisição.           |  3  |  4  |  3  | **36**  |
| **Cross-Site Scripting (XSS):** Injeção de scripts maliciosos em campos de descrição de pedidos.             |  3  |  4  |  3  | **36**  |
| **Ameaça Interna:** Técnico insatisfeito a apagar scripts críticos de automação.                             |  4  |  3  |  2  | **24**  |
| **Engenharia Social:** Ataque via telefone para reset de passwords administrativas.                          |  3  |  3  |  2  | **18**  |
| **Acesso Físico Indevido:** Furto de hardware sem encriptação de disco.                                      |  3  |  2  |  2  | **12**  |
| **Insegurança de Design:** Falha na lógica de negócio permitindo aprovações sem validação.                   |  3  |  2  |  2  | **12**  |

---

## 3.2 Políticas de Acesso e Identidade (IAM)

Adotamos o modelo de **Zero Trust** (Confiança Zero), onde cada requisição deve ser validada continuamente. Abaixo, as principais políticas:

1. **MFA Obrigatório:** Implementação de segundo fator de autenticação para todos os níveis de acesso.
2. **Passwords Fortes:** Exigência de 14 caracteres com alta complexidade.
3. **Single Sign-On (SSO):** Autenticação centralizada via Microsoft Entra ID.
4. **Fim de Contas Genéricas:** Todo o acesso é nominal para garantir auditabilidade total.
5. **Hashing Bcrypt + Salt:** As palavras-passe nunca são armazenadas em texto simples.
6. **Bloqueio por Falhas:** Conta suspensa por 30 min após 5 erros consecutivos.
7. **Rate Limiting:** Proteção contra ataques de força bruta no portal de login.
8. **Tokens JWT Curtos:** Expiração de sessão a cada 15 minutos.
9. **Refresh Tokens Seguros:** Armazenamento em cookies `HTTPOnly` e `Secure`.
10. **Revogação Remota:** Capacidade de invalidar sessões em tempo real.
11. **Validação JWT Backend:** Verificação de assinatura em todas as chamadas de API.
12. **RBAC:** Acesso baseado em cargos (Admin, Técnico N1, Financeiro).
13. **Menor Privilégio (PoLP):** Permissões mínimas necessárias para a execução da tarefa.
14. **Proteção contra IDOR:** Validação de posse do recurso no servidor.
15. **Expiração de Privilégios:** Acessos administrativos temporários expiram em 4h.
16. **Isolamento por Tenants:** Dados separados logicamente por `tenant_id`.
17. **Offboarding Imediato:** Revogação total de acessos em caso de desligamento.
18. **Segurança de API:** Uso de API Keys com escopo restrito (apenas leitura).
19. **Log de Auditoria:** Registo imutável de todas as decisões de acesso.
20. **Isolamento Dev/Prod:** Os programadores utilizam apenas dados fictícios em ambiente de teste.

---

## 3.3 Adequação à LGPD (RoPA)

Mapeamento detalhado do ciclo de vida dos dados na SecureTech, garantindo que a proteção à privacidade esteja integrada em cada etapa do desenvolvimento e operação, conforme as diretrizes da Lei 13.709/18.

| Dado Coletado            | Finalidade                  | Base Legal                       | Direitos do Titular                                 |
| :----------------------- | :-------------------------- | :------------------------------- | :-------------------------------------------------- |
| **CPF do Cliente**       | Emissão de Fatura           | Obrigação Legal                  | Retenção de 5 anos; Hard delete posterior.          |
| **Nome do Técnico**      | Identificação no sistema    | Execução de Contrato             | Exclusão após encerramento do vínculo.              |
| **E-mail Corporativo**   | Alertas e notificações SLA  | Execução de Contrato             | Edição via painel; Exclusão ao fim do B2B.          |
| **Geolocalização**       | Otimização de atendimentos  | Execução de Contrato             | Desativado após o turno; Anonimização após 30 dias. |
| **IP de Acesso**         | Segurança e Auditoria       | Marco Civil / Legítimo Interesse | Retenção mínima de 6 meses.                         |
| **Telefone Pessoal**     | Emergência e 2FA            | Consentimento                    | Revogação via configurações.                        |
| **Dados Bancários**      | Cobranças mensais           | Execução de Contrato             | Exclusão ao cancelar a subscrição.                  |
| **Logs de Ações**        | Accountability técnica      | Legítimo Interesse               | Mantido imutável; Direito ao extrato (Acesso).      |
| **Cookies**              | Sessão de utilizador        | Legítimo Interesse               | Excluído no logout ou limpeza de cache.             |
| **Avaliação (NPS)**      | Qualidade de serviço        | Legítimo Interesse               | Direito à revisão manual pela Qualidade.            |
| **Biometria Facial**     | Ponto e segurança           | Consentimento (Dado Sensível)    | Direito à opção de método alternativo.              |
| **Histórico de Pedidos** | Documentação técnica        | Execução de Contrato             | Direito à ofuscação de dados sensíveis.             |
| **Documentos (RG/CNH)**  | Vínculo e controlo de frota | Obrigação Legal                  | Temporalidade definida pela lei laboral.            |
| **Cargo/Função**         | Controlo de Acesso (RBAC)   | Execução de Contrato             | Editável pelo gestor; excluído com a conta.         |
| **Foto de Perfil**       | Personalização do suporte   | Consentimento                    | Remoção imediata via painel de perfil.              |
| **Morada Residencial**   | Suporte Home Office         | Execução de Contrato             | Apagado do histórico após o atendimento.            |
| **Atestados Médicos**    | Justificação de faltas      | Tutela da Saúde (Dado Sensível)  | Acesso restrito ao RH/Médico.                       |
| **Matrícula do Veículo** | Estacionamento e Reembolso  | Execução de Contrato             | Exclusão após prestação de contas.                  |
| **Gravação de Voz**      | Qualidade do Helpdesk       | Legítimo Interesse               | Direito à cópia; deleção após 90 dias.              |
| **E-mail Secundário**    | Recuperação de conta        | Consentimento                    | Editável ou removível a qualquer momento.           |

---

## 3.4 Análise Crítica Exigida (Segurança)

A vulnerabilidade que recebeu a pontuação máxima na nossa Matriz GUT (125) foi a **Quebra de Controlo de Acesso**, especificamente através de **IDOR (Insecure Direct Object Reference)**. Num cenário real dentro da SecureTech Solutions, um atacante autenticado como "Cliente A" poderia observar que o URL para descarregar o seu relatório de segurança termina em `/api/reports/1001`. Através de uma técnica simples de manipulação de parâmetros (_parameter tampering_), o atacante poderia tentar aceder a `/api/reports/1002`, `1003`, e assim sucessivamente. Sem uma validação de propriedade no servidor, o sistema entregaria dados sensíveis de outras empresas, expondo topologias de rede e vulnerabilidades críticas de terceiros, o que resultaria no incumprimento imediato de SLAs e multas pesadíssimas por violação da LGPD.

Para mitigar este risco de forma robusta, a equipa de SecOps implementou uma estratégia de defesa em profundidade:

1.  **UUIDs v4:** Abandonámos o uso de IDs sequenciais em todos os recursos expostos via API. Diferente dos números inteiros, os UUIDs são aleatórios e possuem um espaço de endereçamento de 128 bits, tornando a técnica de tentativa e erro (_brute-force_) matematicamente inviável para um invasor.
2.  **Verificação de Isolamento por Tenant:** Reforçámos o nosso _middleware_ de autorização no backend. Agora, para cada requisição, o sistema não valida apenas se o token JWT é autêntico, mas executa um cruzamento de dados: o código extrai o `tenant_id` encriptado no token e verifica se ele corresponde ao proprietário do recurso solicitado na base de dados. Se os IDs não coincidirem, a ligação é interrompida com um erro **403 Forbidden**, e a tentativa de acesso indevido é registada nos logs de auditoria para análise forense posterior.
