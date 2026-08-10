# 🎙️ VOICE DATA AGENT — Assistente de Voz com IA

## 📌 Sobre a atividade

Foi desenvolvido um **assistente de voz baseado em Inteligência Artificial**, utilizando Python e integração com diferentes tecnologias de IA para permitir **interação por voz, processamento de linguagem natural e análise de dados**.

O projeto integra **Groq, LangChain, PandasAI e Edge TTS**, proporcionando uma aplicação capaz de receber comandos de voz, processá-los com modelos de linguagem e retornar respostas utilizando síntese de voz.

🔗 **Repositório do projeto:**
https://github.com/deivisontakatu/projeto-ia-voz

---

## 🎯 Objetivos

* Desenvolver um assistente de voz utilizando IA;
* Realizar **reconhecimento e transcrição de voz**;
* Processar perguntas utilizando **Large Language Models (LLMs)**;
* Gerar respostas automaticamente;
* Converter respostas de texto em **áudio**;
* Integrar IA generativa com **análise de dados em arquivos CSV**;
* Aplicar conceitos de integração entre diferentes ferramentas e APIs de IA.

---

## 🧠 Tecnologias utilizadas

| Tecnologia           | Utilização                                       |
| -------------------- | ------------------------------------------------ |
| 🐍 **Python 3.11**   | Linguagem principal do projeto                   |
| ⚡ **Groq**           | Execução dos modelos de linguagem e transcrição  |
| 🔗 **LangChain**     | Integração e gerenciamento da interação com LLMs |
| 📊 **PandasAI**      | Análise de dados utilizando linguagem natural    |
| 🗣️ **Edge TTS**     | Conversão de texto em fala                       |
| 🔊 **SoundDevice**   | Captura de áudio pelo microfone                  |
| 🎵 **Pygame**        | Reprodução do áudio gerado                       |
| 🔐 **python-dotenv** | Gerenciamento das variáveis de ambiente          |

---

## 🏗️ Funcionamento

O projeto apresenta um menu principal com duas possibilidades:

```text
                    🎙️ OICE DATA AGENT
                           │
             ┌─────────────┴─────────────┐
             │                           │
       🤖 Assistente                📊 Análise CSV
             │                           │
       🎤 Entrada de voz          📁 Arquivo CSV
             │                           │
       📝 Transcrição             🤖 PandasAI
             │                           │
       🧠 LLM / Groq              📈 Análise dos dados
             │
       💬 Geração da resposta
             │
       🔊 Edge TTS
             │
       🎧 Resposta em áudio
```

---

## 🤖 Modo Assistente

No modo **Assistente**, o usuário pode interagir por meio da voz.

O fluxo principal é:

1. 🎤 Captura da voz pelo microfone;
2. 📝 Transcrição do áudio utilizando modelo de reconhecimento de fala;
3. 🧠 Processamento da pergunta por um modelo de linguagem;
4. 💬 Geração da resposta;
5. 🗣️ Conversão da resposta para áudio;
6. 🔊 Reprodução da resposta para o usuário.

---

## 📊 Modo Análise de CSV

O segundo modo permite trabalhar com **arquivos CSV** utilizando recursos de IA.

O **PandasAI** possibilita realizar perguntas sobre os dados utilizando linguagem natural, reduzindo a necessidade de escrever manualmente consultas ou operações de análise.

Exemplo de interação:

```text
Usuário:
"Qual foi o produto com maior quantidade de vendas?"

              ↓

PandasAI + LLM

              ↓

Análise do arquivo CSV

              ↓

Resposta em linguagem natural
```

---

## 🔐 Configuração da API

A aplicação utiliza uma chave da API da Groq armazenada em um arquivo `.env`, evitando que a chave seja diretamente inserida no código-fonte.

Exemplo:

```env
GROQ_API_KEY=seu_token_aqui
```

Também podem ser configurados parâmetros como:

```env
GROQ_MODEL=llama-3.3-70b-versatile
GROQ_TRANSCRIPTION_MODEL=whisper-large-v3-turbo
GROQ_TEMPERATURE=...
GROQ_MAX_COMPLETION_TOKENS=...
```

---

## ⚙️ Execução

O projeto requer:

* Python **3.11**
* Microfone
* Saída de áudio
* Chave da API da Groq
* Ambiente virtual Python

Após instalar as dependências e configurar o `.env`, a aplicação pode ser executada com:

```bash
python main.py
```

---

## 📚 Conceitos aplicados

Durante o desenvolvimento foram aplicados conceitos relacionados a:

* 🧠 Inteligência Artificial Generativa;
* 🤖 Large Language Models (LLMs);
* 🎙️ Processamento de voz;
* 📝 Speech-to-Text;
* 🔊 Text-to-Speech;
* 🔗 Integração de APIs;
* 📊 Análise de dados;
* 🐍 Desenvolvimento em Python;
* 🔐 Gerenciamento de variáveis de ambiente;
* 🧩 Integração entre diferentes bibliotecas de IA.

---

## ✅ Resultado

A atividade resultou em uma aplicação integrada de **IA conversacional e análise de dados**, demonstrando como diferentes tecnologias podem ser combinadas para criar uma solução prática.

O projeto permite explorar dois cenários de aplicação de IA:

> **Interação por voz + LLM + síntese de voz**

e

> **LLM + PandasAI + análise de dados**

Dessa forma, a atividade demonstra na prática a utilização de modelos de IA em uma aplicação Python completa, desde a **entrada de dados pelo usuário até o processamento e apresentação dos resultados**.

---

## 🔗 Repositório

📂 **Projeto completo:**
[GitHub — projeto-ia-voz](https://github.com/deivisontakatu/projeto-ia-voz)

---

### 👨‍💻 Desenvolvimento

**Deivison Takatu**

Projeto desenvolvido como atividade prática na área de **Inteligência Artificial e Machine Learning**.
