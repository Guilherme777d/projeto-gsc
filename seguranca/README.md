# Segurança da Informação

## 3.1 Ameaças e Matriz GUT

A análise de segurança do projeto identificou algumas ameaças que podem comprometer os dados e o funcionamento do sistema da empresa.

| Ameaça / Vulnerabilidade | Gravidade (G) | Urgência (U) | Tendência (T) | Total |
|--------------------------|---------------|--------------|---------------|-------|
| SQL Injection em formulários de login | 5 | 5 | 5 | 125 |
| Vazamento de dados sensíveis | 5 | 4 | 4 | 80 |
| Acessos indevidos por senha fraca | 4 | 4 | 4 | 64 |
| Ataque de negação de serviço (DDoS) | 4 | 3 | 3 | 36 |

A vulnerabilidade com maior prioridade foi o **SQL Injection**, pois apresenta alto risco para o sistema e pode comprometer diretamente a segurança das informações armazenadas.

---

## 3.2 Políticas de Acesso

Para reduzir os riscos identificados, foram definidas políticas de acesso para o sistema:

- Uso de autenticação em dois fatores (2FA);
- Senhas armazenadas com hash para maior proteção;
- Controle de acesso por nível de permissão;
- Sessões com tempo de expiração;
- Restrição de acesso a áreas sensíveis do sistema.

---

## 3.3 Adequação à LGPD

O sistema considera princípios básicos da Lei Geral de Proteção de Dados (LGPD), buscando proteger as informações dos usuários.

### Dados coletados
- Nome
- E-mail
- CPF
- Histórico de acesso

### Medidas adotadas
- Coleta apenas de dados necessários;
- Proteção de dados sensíveis;
- Possibilidade de exclusão de conta;
- Uso de consentimento quando necessário;
- Controle de acesso às informações.

---

## Análise Crítica

A principal ameaça identificada foi o SQL Injection, pois esse tipo de falha pode ser explorado por invasores para acessar ou manipular o banco de dados do sistema. No contexto deste projeto, isso poderia comprometer dados importantes dos usuários e da empresa. Para evitar esse risco, é necessário utilizar validação de entradas, consultas parametrizadas e controle adequado de permissões no banco de dados. Essas medidas fortalecem a segurança do sistema e reduzem a possibilidade de ataques.
