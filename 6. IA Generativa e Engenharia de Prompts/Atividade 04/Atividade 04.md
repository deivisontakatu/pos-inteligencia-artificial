# 🤖 MULTI-AGENT AI TEAM — Orquestração de Agentes de IA com Discord, Trello, RAG e Groq

## 📌 Sobre a atividade

Foram desenvolvidas **duas aplicações baseadas em Inteligência Artificial Generativa e arquitetura multiagente**, utilizando **Python, Agno, Groq e Discord** como elementos centrais.

Os projetos exploram diferentes possibilidades de utilização de **agentes autônomos especializados**, demonstrando como um agente principal pode receber uma solicitação, interpretar seu objetivo e delegar a execução para agentes especializados.

O primeiro projeto, **Multi-Agent Trello Discord Groq**, apresenta um fluxo voltado para **gerenciamento e execução de tarefas**, integrando agentes de IA ao Trello. A solicitação recebida pelo Discord é transformada em uma tarefa, registrada em um quadro Kanban e acompanhada pelos estados `TODO`, `DOING` e `DONE`. O fluxo utiliza um **Project Manager Agent** e um **Executor Agent**.

O segundo projeto, **AI Knowledge Team**, amplia essa abordagem para um cenário de **assistente multiagente de conhecimento**, incorporando **RAG, ChromaDB, Sentence Transformers, pesquisa na web, geração de imagens, memória persistente, cálculo e data/hora**. O sistema possui agentes especializados em conhecimento interno, pesquisa externa e geração de imagens.

Dessa forma, os dois projetos podem ser compreendidos como aplicações complementares de uma mesma arquitetura:

> **Discord → Agente Orquestrador → Agentes Especializados → Ferramentas/APIs → Resultado**

🔗 **Repositórios dos projetos:**

* [GitHub — Multi-Agent Trello Discord Groq](https://github.com/deivisontakatu/projeto-agent-trello-discord)
* [GitHub — AI Knowledge Team](https://github.com/deivisontakatu/projeto-ai-knowledge-team)

---

## 🎯 Objetivos

Os projetos foram desenvolvidos com os seguintes objetivos:

* Desenvolver aplicações utilizando **Inteligência Artificial Generativa**;

* Aplicar conceitos de **arquitetura multiagente**;

* Utilizar um agente principal para realizar a **orquestração de agentes especializados**;

* Integrar modelos de linguagem utilizando a **Groq**;

* Utilizar o **Agno** para criação e coordenação de agentes;

* Integrar agentes de IA com aplicações externas;

* Automatizar fluxos de gerenciamento de tarefas;

* Integrar IA com o **Trello** para gerenciamento de atividades;

* Implementar **RAG — Retrieval-Augmented Generation** para consulta de documentos internos;

* Utilizar **ChromaDB** como banco de dados vetorial;

* Realizar pesquisas externas utilizando agentes especializados;

* Integrar geração de imagens a um fluxo de agentes;

* Implementar memória persistente para conversações;

* Demonstrar o uso de ferramentas especializadas dentro de um sistema multiagente;

* Aplicar conceitos de integração entre **LLMs, APIs, bancos de dados e plataformas externas**.

---

# 🧠 Tecnologias utilizadas

| Tecnologia                   | Utilização                                                         |
| ---------------------------- | ------------------------------------------------------------------ |
| 🐍 **Python 3.12+**          | Linguagem principal dos projetos                                   |
| 🤖 **Agno**                  | Criação, configuração e orquestração dos agentes                   |
| ⚡ **Groq**                   | Execução dos modelos de linguagem                                  |
| 💬 **Discord**               | Interface de interação com os usuários                             |
| 📋 **Trello**                | Gerenciamento e acompanhamento de tarefas                          |
| 🔎 **RAG**                   | Recuperação de informações relevantes antes da geração da resposta |
| 🗄️ **ChromaDB**             | Armazenamento e recuperação dos embeddings                         |
| 🧠 **Sentence Transformers** | Geração dos embeddings dos documentos                              |
| 💾 **SQLite**                | Persistência do histórico de conversações                          |
| 🌐 **Web Search**            | Pesquisa de informações externas e atuais                          |
| 🖼️ **Image Agent**          | Geração de imagens a partir de solicitações                        |
| 🔢 **Calculate**             | Execução de expressões matemáticas                                 |
| 🕐 **DateTime**              | Consulta de data e hora atuais                                     |
| 🔐 **python-dotenv**         | Gerenciamento de variáveis de ambiente                             |
| 📦 **uv**                    | Gerenciamento do ambiente e dependências Python                    |
| 🌐 **Requests**              | Comunicação com a API REST do Trello                               |

O primeiro projeto utiliza Agno, discord.py, Groq, python-dotenv e Requests para implementar o fluxo de gerenciamento de tarefas e integração com o Trello.

O segundo adiciona ao ecossistema recursos de RAG, ChromaDB, Sentence Transformers, memória persistente e geração de imagens.

---

# 🏗️ Arquitetura geral dos projetos

Os dois projetos apresentam uma arquitetura baseada no conceito de **Team de agentes**, no qual um agente principal recebe a solicitação e decide quais agentes ou ferramentas devem participar do processamento.

Uma representação integrada das soluções pode ser apresentada da seguinte forma:

```text
                         👤 USUÁRIO
                             │
                             ▼
                       💬 DISCORD
                             │
                             ▼
                    🤖 AGENTE ORQUESTRADOR
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
       📋 PROJECT TEAM   🧠 KNOWLEDGE     🔎 RESEARCHER
              │            AGENT             │
              │              │               │
              ▼              ▼               ▼
        👨‍💼 PM AGENT     🗄️ RAG          🌐 WEB
              │              │
              ▼              ▼
          📋 TRELLO       CHROMADB
              │
              ▼
        ⚙️ EXECUTOR
              │
              ▼
        TODO → DOING → DONE


              ┌─────────────────────┐
              │   OUTROS RECURSOS  │
              ├─────────────────────┤
              │ 🖼️ Image Agent      │
              │ 🔢 Calculate        │
              │ 🕐 DateTime         │
              │ 💾 Memory / SQLite  │
              └─────────────────────┘
```

O **Multi-Agent Trello Discord Groq** concentra-se no gerenciamento e execução simulada de tarefas, enquanto o **AI Knowledge Team** possui uma arquitetura mais ampla, com agentes especializados em conhecimento, pesquisa e geração de imagens.

---

# 📋 Projeto 1 — Multi-Agent Trello Discord Groq

O primeiro projeto implementa um fluxo de **gerenciamento automatizado de tarefas utilizando agentes de IA**.

A aplicação recebe uma solicitação no Discord e utiliza um time de agentes para transformar essa solicitação em uma tarefa acompanhada dentro do Trello.

O fluxo é composto principalmente por:

* `Project Team`;
* `Project Manager Agent`;
* `Executor Agent`;
* ferramentas de integração com Trello.

O fluxo definido no projeto é:

```text
👤 Usuário
     │
     ▼
💬 Discord
     │
     ▼
🤖 Project Team
     │
     ▼
👨‍💼 Project Manager Agent
     │
     ▼
📋 Criar card
     │
     ▼
🟡 TODO
     │
     ▼
⚙️ Executor Agent
     │
     ▼
🔵 DOING
     │
     ▼
📝 Registrar execução
     │
     ▼
🟢 DONE
     │
     ▼
💬 Resposta no Discord
```

O projeto utiliza o Trello como uma camada de **controle visual do ciclo de vida da tarefa**. O PM cria o card, enquanto o executor encontra o card, atualiza seu status e registra comentários referentes à execução.

---

# 👨‍💼 Project Manager Agent

O **Project Manager Agent** representa o papel de gerenciamento dentro da arquitetura.

Sua responsabilidade é interpretar a solicitação recebida e criar uma tarefa correspondente no Trello.

O resultado da atuação do agente é a criação de um card na lista configurada como:

```text
TODO
```

Dessa maneira, a inteligência artificial passa a atuar não somente como um sistema de perguntas e respostas, mas também como parte de um **fluxo de gerenciamento de trabalho**.

---

# ⚙️ Executor Agent

Após a criação da tarefa, o **Executor Agent** assume o processamento.

Seu fluxo consiste em:

1. 🔎 Localizar o card no Trello;
2. 🔵 Movê-lo para `DOING`;
3. 📝 Registrar o início da execução;
4. 🤖 Simular a realização da tarefa;
5. 📝 Registrar o resultado;
6. 🟢 Mover o card para `DONE`;
7. 💬 Retornar o resultado ao Discord.

É importante destacar que a execução externa da tarefa é **simulada pelo modelo**. O agente registra o processo e o resultado no Trello, mas não executa operações externas relacionadas à tarefa solicitada.

---

# 📋 Integração com Trello

O Trello funciona como a camada de **gestão operacional** do primeiro projeto.

A integração é realizada por meio da API REST do Trello, permitindo operações como:

* criação de cards;
* localização de cards;
* movimentação entre listas;
* inclusão de comentários.

O quadro pode ser organizado seguindo um fluxo Kanban:

```text
┌────────────┐
│   TODO     │
│            │
│ 📝 Tarefa  │
└─────┬──────┘
      │
      ▼
┌────────────┐
│   DOING    │
│            │
│ ⚙️ Execução│
└─────┬──────┘
      │
      ▼
┌────────────┐
│    DONE    │
│            │
│ ✅ Concluído│
└────────────┘
```

Assim, o Trello funciona como uma representação visual do estado de execução da atividade.

---

# 🧠 Projeto 2 — AI Knowledge Team

O segundo projeto expande o conceito de arquitetura multiagente.

Em vez de possuir somente agentes voltados para gerenciamento de tarefas, o sistema possui especialistas para diferentes tipos de solicitações.

O **AI Knowledge Team** pode:

* responder perguntas gerais;
* consultar documentos internos;
* realizar pesquisas externas;
* gerar imagens;
* executar cálculos;
* consultar data e hora;
* manter histórico das conversações.

As solicitações são recebidas pelo Discord utilizando o comando:

```text
!ask
```

O Team identifica o tipo de solicitação e direciona o processamento para o especialista adequado.

---

# 🧩 Agentes especializados

O projeto utiliza diferentes agentes com responsabilidades específicas.

| Agente                   | Responsabilidade                            |
| ------------------------ | ------------------------------------------- |
| 🤖 **AI Knowledge Team** | Orquestra os agentes e ferramentas          |
| 🧠 **Knowledge Agent**   | Consulta documentos internos utilizando RAG |
| 🔎 **Researcher**        | Realiza pesquisas externas                  |
| 🖼️ **Image Agent**      | Processa solicitações de geração de imagens |

Essa divisão permite aplicar o princípio de **especialização de agentes**, no qual cada agente possui uma responsabilidade específica dentro do sistema.

---

# 📚 RAG e conhecimento interno

Uma das principais diferenças do segundo projeto é a utilização de **RAG — Retrieval-Augmented Generation**.

Os documentos internos ficam armazenados em:

```text
data/documents/
```

Durante a inicialização da aplicação, os documentos podem ser processados e indexados.

O processo é:

```text
📄 Documento
     │
     ▼
✂️ Chunking
     │
     ▼
🧠 Sentence Transformers
     │
     ▼
🔢 Embeddings
     │
     ▼
🗄️ ChromaDB
```

Os textos são divididos em chunks de até aproximadamente 400 caracteres e os embeddings são gerados utilizando o modelo `all-MiniLM-L6-v2`. Os embeddings e metadados são persistidos no diretório `chroma_db/`.

Quando uma pergunta depende de conhecimento interno, o **Knowledge Agent** recupera informações relevantes da base antes de produzir a resposta.

---

# 🔎 Pesquisa externa

O **Researcher** é responsável por solicitações que dependem de informações externas ou atuais.

Exemplo:

```text
Usuário:

!ask Pesquise as boas práticas atuais
para governança de IA.

          ↓

AI Knowledge Team

          ↓

Researcher

          ↓

🌐 Pesquisa externa

          ↓

🧠 Síntese das informações

          ↓

💬 Resposta no Discord
```

O sistema também prevê situações em que uma solicitação exige simultaneamente **conhecimento interno e pesquisa externa**, acionando os especialistas correspondentes antes da síntese final.

---

# 🖼️ Geração de imagens

Outro recurso implementado no segundo projeto é o **Image Agent**.

Quando o usuário solicita uma imagem, o agente transforma a solicitação em um prompt visual e aciona um provedor de geração de imagens.

Exemplo:

```text
!ask Gere uma imagem de um
laboratório futurista com luz natural.

              ↓

        🖼️ Image Agent

              ↓

      📝 Prompt visual

              ↓

      🎨 Image Provider

              ↓

          🖼️ Imagem

              ↓

        💬 Discord
```

A imagem gerada é anexada à resposta enviada ao Discord.

---

# 💾 Memória e persistência

O segundo projeto também implementa **memória persistente**.

O histórico das conversações é armazenado pelo Agno em:

```text
data/ai_knowledge_team.db
```

O ID do autor do Discord é utilizado como identificador da sessão.

A arquitetura passa, portanto, a trabalhar com três tipos importantes de armazenamento:

```text
📄 Documentos
      ↓
🗄️ ChromaDB
      ↓
Conhecimento recuperável


💬 Conversações
      ↓
💾 SQLite
      ↓
Memória persistente


📋 Tarefas
      ↓
Trello
      ↓
Gestão operacional
```

---

# 🔗 Relação entre os dois projetos

Os projetos possuem uma relação direta do ponto de vista arquitetural.

O primeiro demonstra como **agentes de IA podem organizar e executar um fluxo de tarefas**.

O segundo demonstra como uma arquitetura semelhante pode ser expandida para **conhecimento, pesquisa, memória, ferramentas e geração de conteúdo**.

Podemos representar essa evolução da seguinte forma:

```text
              MULTI-AGENT AI
                    │
                    ▼
          🤖 Agente Orquestrador
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
   📋 Gestão de tarefas   🧠 Conhecimento
          │                   │
          ▼                   ▼
       Trello              RAG
          │                   │
          ▼                   ▼
      Executor          Knowledge Agent
                              │
                    ┌─────────┼─────────┐
                    │         │         │
                    ▼         ▼         ▼
                  🌐 Web    🖼️ Image   🔢 Tools
```

Assim, o **Multi-Agent Trello Discord Groq** pode ser entendido como uma aplicação de agentes orientada à **gestão de processos**, enquanto o **AI Knowledge Team** representa uma aplicação orientada à **gestão de conhecimento e resolução de solicitações heterogêneas**.

---

# 🔄 Comparação entre os projetos

| Característica         | Multi-Agent Trello | AI Knowledge Team |
| ---------------------- | ------------------ | ----------------- |
| 💬 Discord             | ✅                  | ✅                 |
| 🤖 Agentes de IA       | ✅                  | ✅                 |
| 🧠 Agente orquestrador | ✅                  | ✅                 |
| ⚡ Groq                 | ✅                  | ✅                 |
| 🔗 Agno                | ✅                  | ✅                 |
| 📋 Trello              | ✅                  | ❌                 |
| 👨‍💼 Project Manager  | ✅                  | ❌                 |
| ⚙️ Executor Agent      | ✅                  | ❌                 |
| 🧠 Knowledge Agent     | ❌                  | ✅                 |
| 🔎 Researcher          | ❌                  | ✅                 |
| 🖼️ Image Agent        | ❌                  | ✅                 |
| 📚 RAG                 | ❌                  | ✅                 |
| 🗄️ ChromaDB           | ❌                  | ✅                 |
| 🧬 Embeddings          | ❌                  | ✅                 |
| 🌐 Pesquisa web        | ❌                  | ✅                 |
| 💾 Memória persistente | ❌                  | ✅                 |
| 🔢 Calculadora         | ❌                  | ✅                 |
| 🕐 Data/hora           | ❌                  | ✅                 |
| 🖼️ Geração de imagens | ❌                  | ✅                 |
| 🔐 Aprovação humana    | Simulação          | Simulação         |

---

# 🔐 Segurança e controle humano

Os dois projetos também apresentam preocupações relacionadas à segurança e ao controle das ações executadas por agentes.

No projeto do Trello, as credenciais são armazenadas em variáveis de ambiente, evitando que tokens sejam inseridos diretamente no código-fonte.

No **AI Knowledge Team**, existe uma ferramenta denominada `execute_critical_action`, porém ela **não executa alterações reais automaticamente**. O sistema representa a ação e informa que é necessária aprovação humana.

Essa abordagem demonstra um conceito importante em sistemas baseados em agentes:

> **Nem toda decisão produzida por uma IA deve resultar automaticamente em uma ação externa.**

A arquitetura pode, portanto, combinar **autonomia para raciocínio e delegação** com **controle humano para operações críticas**.

---

# 📊 Observabilidade

O segundo projeto também apresenta uma camada explícita de **observabilidade**.

Quando `OBSERVABILITY=true`, são registrados dados relacionados à execução, incluindo:

* pergunta realizada;
* modelo utilizado;
* Team e ID da execução;
* sessão persistente;
* agentes acionados;
* ferramentas utilizadas;
* rotas realizadas;
* chunks recuperados pelo RAG;
* informações relacionadas às imagens geradas.

Isso permite acompanhar não apenas **qual foi a resposta**, mas também **como o sistema chegou até ela**.

---

# ⚙️ Configuração e execução

Os dois projetos utilizam **Python 3.12 ou superior** e o gerenciador de ambientes e dependências `uv`.

No projeto do Trello:

```bash
uv sync
uv run python main.py
```

No AI Knowledge Team:

```bash
uv sync
uv run a4-ai-knowledge-team
```

ou:

```bash
uv run python -m a4_ai_knowledge_team.main
```

As credenciais e configurações são mantidas em arquivos `.env`, evitando a exposição de tokens no código-fonte.

---

# 💡 Exemplos de utilização

## 📋 Cenário 1 — Gestão de tarefa

```text
Usuário:

@MeuBot preparar um resumo dos riscos do projeto

              ↓

Project Team

              ↓

Project Manager Agent

              ↓

📋 Criação do card

              ↓

TODO

              ↓

Executor Agent

              ↓

DOING

              ↓

📝 Execução simulada

              ↓

DONE

              ↓

💬 Resultado no Discord
```

---

## 🧠 Cenário 2 — Conhecimento interno

```text
Usuário:

!ask Qual é o responsável pela
governança de Inteligência Artificial?

              ↓

AI Knowledge Team

              ↓

Knowledge Agent

              ↓

RAG

              ↓

ChromaDB

              ↓

📄 Documentos internos

              ↓

🧠 Resposta fundamentada
```

---

## 🌐 Cenário 3 — Pesquisa externa

```text
Usuário:

!ask Pesquise as boas práticas atuais
para governança de IA.

              ↓

AI Knowledge Team

              ↓

Researcher

              ↓

🌐 Web

              ↓

🧠 Síntese

              ↓

💬 Resposta
```

---

## 🖼️ Cenário 4 — Geração de imagem

```text
Usuário:

!ask Gere uma imagem de um
laboratório futurista.

              ↓

AI Knowledge Team

              ↓

Image Agent

              ↓

🎨 Provedor de imagens

              ↓

🖼️ Imagem

              ↓

💬 Discord
```

Os exemplos de interação e os fluxos descritos correspondem aos comportamentos documentados no projeto AI Knowledge Team.

---

# 📚 Conceitos aplicados

Durante o desenvolvimento dos dois projetos foram aplicados conceitos relacionados a:

* 🤖 **Inteligência Artificial Generativa**;

* 🧠 **Large Language Models — LLMs**;

* 👥 **Arquitetura Multiagente**;

* 🎯 **Agentes especializados**;

* 🔀 **Orquestração de agentes**;

* 🔗 **Integração de APIs**;

* 💬 **Bots para Discord**;

* 📋 **Gerenciamento automatizado de tarefas**;

* 🔎 **Retrieval-Augmented Generation — RAG**;

* 🧬 **Embeddings**;

* 🗄️ **Bancos de dados vetoriais**;

* 🌐 **Pesquisa de informações externas**;

* 🖼️ **Geração de imagens por IA**;

* 💾 **Memória persistente**;

* 📊 **Observabilidade de agentes**;

* 🔐 **Gerenciamento de credenciais**;

* 👤 **Human-in-the-loop**;

* 🐍 **Desenvolvimento Python**;

* 📦 **Gerenciamento de dependências com uv**.

---

# 🚀 Evolução arquitetural

Os dois projetos demonstram uma evolução progressiva na utilização de agentes de IA.

No primeiro projeto, o agente de IA é utilizado principalmente para **organizar e executar um processo operacional**:

```text
Solicitação
    ↓
Orquestração
    ↓
PM
    ↓
Executor
    ↓
Trello
```

No segundo, a arquitetura é ampliada:

```text
Solicitação
    ↓
Orquestração
    ↓
┌───────────────┬──────────────┬──────────────┐
│               │              │              │
▼               ▼              ▼              ▼
Knowledge    Researcher     Image Agent    Tools
│               │              │              │
▼               ▼              ▼              ▼
RAG             Web          Imagem        Funções
│
▼
ChromaDB
```

Essa evolução demonstra que a arquitetura multiagente pode ser utilizada não apenas para **dividir tarefas**, mas também para criar sistemas capazes de **selecionar dinamicamente especialistas e ferramentas de acordo com a necessidade de cada solicitação**.

---

# ✅ Resultado

O desenvolvimento dos dois projetos resultou em duas aplicações práticas de **arquitetura multiagente utilizando Inteligência Artificial Generativa**.

O primeiro projeto demonstra a utilização de agentes para **gerenciamento e execução de tarefas**, conectando Discord, Agno, Groq e Trello em um fluxo automatizado de trabalho.

O segundo projeto amplia esse conceito e apresenta um **time de agentes especializados**, capaz de trabalhar com conhecimento interno, pesquisa externa, geração de imagens, cálculo, data/hora e memória persistente.

Dessa forma, os projetos demonstram diferentes níveis de aplicação de agentes de IA:

> **📋 Multi-Agent Trello:** IA aplicada à **gestão e execução de tarefas**.

> **🧠 AI Knowledge Team:** IA aplicada à **gestão de conhecimento, pesquisa e utilização de ferramentas especializadas**.

Em conjunto, as aplicações demonstram como **LLMs podem deixar de atuar somente como interfaces conversacionais e passar a funcionar como componentes de sistemas capazes de interpretar solicitações, selecionar especialistas, utilizar ferramentas, acessar fontes de conhecimento e coordenar fluxos de trabalho**.

---

# 🔗 Repositórios

📂 **Projeto 1 — Multi-Agent Trello Discord Groq**

[GitHub — projeto-agent-trello-discord](https://github.com/deivisontakatu/projeto-agent-trello-discord)

📂 **Projeto 2 — AI Knowledge Team**

[GitHub — projeto-ai-knowledge-team](https://github.com/deivisontakatu/projeto-ai-knowledge-team)

---

## 👨‍💻 Desenvolvimento

**Deivison Takatu**

Projetos desenvolvidos como atividades práticas na área de **Inteligência Artificial, LLMs, Agentes Autônomos e Integração de Sistemas**, explorando a aplicação de arquiteturas multiagente em diferentes cenários de uso.
