<div align="center">
  <h1>
    <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Hourglass%20Not%20Done.png" alt="Ampulheta" width="45" height="45" />
    Laboratório de Time-Based Blind SQL Injection
    <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Database.png" alt="Banco de Dados" width="45" height="45" />
  </h1>
</div>

<p align="center">
  <img alt="Linguagens" src="https://img.shields.io/github/languages/top/vrsmarcos26/SQL-Injection-Time-Based-Blind?style=for-the-badge&color=563D7C">
  <img alt="Licença" src="https://img.shields.io/github/license/vrsmarcos26/SQL-Injection-Time-Based-Blind?style=for-the-badge&color=blue">
</p>

<p align="center">
  Um ambiente de laboratório avançado para demonstrar e estudar uma das técnicas mais sutis de SQL Injection: <strong>Time-Based Blind</strong>. Este projeto foi construído com PHP e MySQL para simular um cenário realista onde um atacante extrai dados de um banco de dados sem receber nenhuma resposta visual direta da aplicação.
</p>

<p align="center">
  <a href="#-aviso-importante">Aviso</a> •
  <a href="#-o-desafio">O Desafio</a> •
  <a href="#-tecnologias-utilizadas">Tecnologias</a> •
  <a href="#-como-rodar-o-laboratório">Como Rodar</a> •
  <a href="#-explorando-a-vulnerabilidade">Explorando</a> •
  <a href="#-licença">Licença</a>
</p>

---

### ⚠️ Aviso Importante

**Este projeto é intencionalmente vulnerável.** Ele foi criado para fins estritamente educacionais. **NÃO FAÇA O DEPLOY DESTA APLICAÇÃO EM UM SERVIDOR PÚBLICO OU DE PRODUÇÃO.** Use-o apenas em um ambiente local e controlado.

---

### 🎯 O Desafio: Time-Based Blind SQL Injection

Diferente de uma injeção de SQL clássica, em um cenário "Blind" (cego), a aplicação não retorna erros do banco de dados ou dados extraídos diretamente na tela. A resposta da página é sempre a mesma, seja o login bem-sucedido ou não.

O desafio aqui é explorar a vulnerabilidade usando o **tempo** como único canal de comunicação. O atacante injeta comandos `SLEEP()` na consulta SQL e, ao medir o tempo de resposta do servidor, consegue fazer perguntas de "sim" ou "não" ao banco de dados para extrair informações caractere por caractere.

---

### 🛠️ Tecnologias Utilizadas

<p align="center">
  <a href="https://www.php.net/"><img src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white" alt="PHP"></a>
  <a href="https://www.mysql.com/"><img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"></a>
</p>

---

### ⚙️ Como Rodar o Laboratório

Você precisará ter **PHP**, **MySQL** (ou MariaDB) e **Python 3** (para o script de exploração) instalados.

1.  **Clone o Repositório**
    ```bash
    git clone https://github.com/vrsmarcos26/SQL-Injection-Time-Based-Blind.git
    cd SQL-Injection-Time-Based-Blind
    ```

2.  **Configure o Banco de Dados**
    Execute o script `setup.sql` para criar o banco, a tabela e o usuário. Você precisará da sua senha de `root` do MySQL.
    ```bash
    mysql -u root -p < setup.sql
    ```

3.  **Inicie o Servidor Local**
    Use o servidor embutido do PHP para rodar a aplicação. Mantenha este terminal aberto.
    ```bash
    php -S localhost:8888
    ```

4.  **Acesse o Laboratório**
    Abra seu navegador e acesse: `http://localhost:8888/index.html`

---

### 💣 Explorando a Vulnerabilidade

A exploração de uma falha Time-Based Blind SQLi é tipicamente automatizada com um script.

#### Script de Exploração em Python

Um script de exemplo (`exploit.py`) é fornecido neste repositório para demonstrar como o ataque funciona na prática. Ele calibra o tempo de resposta normal do servidor e, em seguida, testa cada caractere para extrair a senha do usuário alvo.

**Como usar o script de exemplo:**

Em um **novo terminal** (mantendo o servidor PHP rodando no outro), execute:
```bash
python exploit.py

Nota Importante: O script fornecido é apenas uma das muitas maneiras de automatizar este ataque. O verdadeiro aprendizado vem de entender a lógica por trás dele. É altamente recomendado que você tente construir seu próprio script do zero! Isso solidificará seu entendimento sobre como a vulnerabilidade é explorada passo a passo.

📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
