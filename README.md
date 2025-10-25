# TermIA — Entrega Parcial (Semanas 1–3) 

---

## 🎯 Visão Geral

O projeto **TermIA (Terminal Inteligente)** tem como objetivo aplicar os conceitos fundamentais de **análise léxica e sintática** da disciplina de Compiladores, integrando-os ao desenvolvimento de um shell personalizado com suporte posterior a Inteligência Artificial.

Esta entrega corresponde às **Semanas 1, 2 e 3** do cronograma, abrangendo:
- **Definição da gramática inicial (EBNF);**
- **Implementação do analisador léxico (Lexer) funcional;**
- **Implementação do analisador sintático (Parser) integrado.**

A implementação foi feita em **Python 3.10+** utilizando o pacote **PLY (Python Lex-Yacc)**, conforme sugerido nos recursos recomendados do PRD.

---

## 🧩 Estrutura do Projeto

```
termia_parcial/
├─ grammar.ebnf           # Definição formal da linguagem (gramática EBNF)
├─ README_parcial.md      # Documento descritivo (este arquivo)
├─ termia/
│  ├─ __init__.py
│  ├─ ast.py              # Estrutura da Árvore Sintática Abstrata (AST)
│  ├─ tokens.py           # Analisador Léxico (Lexer)
│  ├─ parser.py           # Analisador Sintático (Parser)
│  └─ main_demo.py        # Interface de teste simples (REPL)
└─ 
```

---

## ⚙️ Requisitos

- **Python 3.10+**
- **Biblioteca PLY** instalada:  
  ```bash
  pip install ply
  ```
- Sistema operacional Linux ou WSL.

---

## 🧠 Estrutura dos Comandos Implementados

A gramática define um **conjunto de comandos reconhecidos** pelo shell TermIA.  
Abaixo estão descritas as **estruturas válidas** e os **requisitos de entrada** para cada tipo de comando.

---

### 🔹 Comandos de Sistema Operacional

#### **1. `ls`**
- **Função:** listar conteúdo de um diretório.
- **Estrutura:**  
  ```
  ls [<path>]
  ```
- **Requisitos:**
  - `<path>` é **opcional**.
  - Quando fornecido, deve representar um caminho válido (exemplo: `/home/usuario`).
  - Pode ser omitido para listar o diretório atual.

---

#### **2. `mkdir`**
- **Função:** criar um novo diretório.
- **Estrutura:**  
  ```
  mkdir <nome>
  ```
- **Requisitos:**
  - `<nome>` é **obrigatório**.
  - Pode conter letras, números, pontos (`.`), hífens (`-`) ou underscores (`_`).

---

#### **3. `cd`**
- **Função:** alterar o diretório de trabalho atual.
- **Estrutura:**  
  ```
  cd [<path>]
  ```
- **Requisitos:**
  - `<path>` é **opcional**.
  - Pode ser um caminho absoluto (`/home/usuario`), relativo (`../pasta`), nome simples (`projetos`) ou literal (`"Meu Diretório"`).
  - Caso seja omitido, poderá futuramente significar “voltar ao diretório inicial” (HOME).

---

#### **4. `exit`**
- **Função:** encerrar o terminal.
- **Estrutura:**  
  ```
  exit
  ```
- **Requisitos:**  
  - Nenhum argumento é permitido.

---

### 🔹 Comandos de Inteligência Artificial

Os comandos do grupo `ia` correspondem às operações de integração com APIs de IA (como OpenAI GPT ou Ollama local).  
Eles seguem o formato geral:

```
ia <subcomando> <entrada>
```

#### **1. `ia ask`**
- **Função:** fazer uma pergunta direta à IA.
- **Estrutura:**  
  ```
  ia ask "<pergunta>"
  ```
- **Requisitos:**
  - A entrada deve estar entre aspas duplas.
  - Exemplo de entrada válida: `"Qual é a capital da França?"`

---

#### **2. `ia summarize`**
- **Função:** solicitar um resumo de um texto fornecido.
- **Estrutura:**  
  ```
  ia summarize "<texto>"
  ```
- **Requisitos:**
  - O texto deve ser passado entre aspas duplas.
  - É recomendável limitar o tamanho da entrada para facilitar o processamento.

---

#### **3. `ia codeexplain`**
- **Função:** pedir à IA uma explicação de código ou arquivo.
- **Estrutura:**  
  ```
  ia codeexplain <alvo>
  ```
- **Requisitos:**
  - `<alvo>` pode ser:
    - um **caminho** de arquivo (ex.: `/home/usuario/script.py`);
    - um **nome simples** (ex.: `main.py`);
    - ou uma **string literal** entre aspas (ex.: `"arquivo.py"`).

---

## 🧱 Funcionamento Interno (Resumo)

| Componente | Função | Implementação |
|-------------|--------|----------------|
| **Lexer (`tokens.py`)** | Identifica as palavras e símbolos da linguagem (tokens) | PLY – Lex |
| **Parser (`parser.py`)** | Organiza os tokens conforme a gramática e monta a AST | PLY – Yacc |
| **AST (`ast.py`)** | Representa a estrutura lógica de cada comando | Dicionários Python |
| **REPL (`main_demo.py`)** | Interface interativa de testes (ainda sem execução real) | Python CLI |

---

## 📈 Próximos Passos

- Executar comandos reais do sistema operacional (em ambiente controlado);
- Integrar APIs de IA externas via REST ou localmente;
- Implementar histórico de comandos e mensagens de ajuda;
- Aprimorar UX.

---

**Autores:** Gabriel Pereira Barcellos Sacramento, Rhuan Pablo Malta Lage, Ueld Judah Nunes Nóbrega
**Projeto:** TermIA – Terminal Inteligente  
**Entrega:** Parcial
**Disciplina:** ECOI26 – Compiladores  
**Universidade Federal de Itajubá – Campus Itabira**
