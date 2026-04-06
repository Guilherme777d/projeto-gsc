# 3. Segurança da Informação

## 3.1 Mapeamento de Ameaças e Matriz GUT

Foram identificadas possíveis vulnerabilidades no sistema da SecureTech Solutions, avaliadas com base nos critérios de Gravidade (G), Urgência (U) e Tendência (T).

| Ameaça / Vulnerabilidade        | G | U | T | Total |
| ------------------------------- | - | - | - | ----- |
| SQL Injection (falha no login)  | 5 | 5 | 5 | 125   |
| Vazamento de dados (LGPD)       | 5 | 4 | 4 | 80    |
| Ataque DDoS (indisponibilidade) | 4 | 3 | 3 | 36    |

---

## 3.2 Políticas de Autenticação e Controle de Acesso

O sistema adotará práticas modernas de segurança:

* **Autenticação:** uso de JWT (JSON Web Token) com tempo de expiração de 1 hora
* **Armazenamento de senha:** utilização de hash com algoritmo bcrypt (com salt)
* **Controle de acesso:** modelo RBAC (Role-Based Access Control)

  * Admin: acesso total
  * Usuário: acesso limitado às suas informações

---

## 3.3 Adequação à LGPD

O sistema será desenvolvido conforme os princípios da Lei Geral de Proteção de Dados (LGPD).

**Dados coletados:**

* Nome
* CPF
* E-mail
* Informações de acesso

**Base legal:**

* Execução de contrato
* Consentimento do usuário

**Direito ao esquecimento:**
O sistema permitirá que o usuário solicite a exclusão dos seus dados através de um botão "Excluir Conta", garantindo a remoção das informações do banco de dados.

---

## Análise Crítica

A principal vulnerabilidade identificada foi o risco de SQL Injection, que pode ocorrer quando entradas do usuário não são devidamente validadas. Um invasor poderia manipular comandos SQL para acessar ou modificar dados sensíveis.

Para mitigar esse risco, serão utilizadas consultas parametrizadas (Prepared Statements) e validação de entrada de dados. Além disso, o uso de criptografia e autenticação segura reduz significativamente os riscos de vazamento de informações.

Essas medidas garantem maior proteção dos dados dos usuários e aumentam a confiabilidade do sistema desenvolvido.
