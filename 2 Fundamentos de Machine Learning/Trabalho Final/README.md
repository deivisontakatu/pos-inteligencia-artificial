# 📊 **Customer Churn Prediction - Telecom Dataset**

## 🎯 **Descrição Geral do Projeto**

Este projeto faz parte do **Trabalho Final** da disciplina, com o objetivo de aplicar técnicas de **Ciência de Dados e Machine Learning** na **resolução de um problema de negócio real**.  
O grupo escolheu um **dataset sobre churn de clientes em uma empresa de telecomunicações**, com foco em prever **quais clientes têm maior probabilidade de encerrar seus serviços**.

A redução do churn é essencial para empresas de telecomunicação, pois **reter um cliente é significativamente mais barato do que adquirir um novo**.  
A previsão de churn permite que a empresa **atue de forma proativa**, oferecendo benefícios personalizados ou melhorias de serviço para reter clientes em risco.

---

## 🧩 **Problema de Negócio**

O **churn de clientes** ocorre quando um cliente cancela o serviço ou deixa de ser assinante.  
Na indústria de telecomunicações, a alta concorrência e a facilidade de migração entre operadoras tornam o churn um problema crítico.

### O desafio:
- Detectar **precocemente quais clientes estão propensos a cancelar** seus serviços.
- Identificar **padrões e variáveis-chave** que explicam o comportamento de churn.
- Criar **modelos preditivos** que possam apoiar **decisões estratégicas de retenção**.

---

## 🎯 **Objetivos do Projeto**

### **Objetivo Geral**
Desenvolver um modelo de aprendizado de máquina capaz de prever o churn de clientes de uma empresa de telecomunicações com base em dados históricos.

### **Objetivos Específicos**
- Realizar uma **análise exploratória** detalhada do dataset, extraindo **insights relevantes**.
- Tratar e preparar os dados para **modelagem supervisionada**.
- Aplicar e comparar diferentes **algoritmos de classificação**.
- Avaliar os modelos com **métricas de desempenho** (Acurácia, Precisão, Recall, F1-Score).
- Apresentar **conclusões técnicas e de negócio**.

---

## 🗂️ **Descrição do Dataset**

**Fonte:** [Kaggle - Telco Customer Churn Dataset](https://www.kaggle.com/blastchar/telco-customer-churn)  
**Quantidade de registros:** 7.043 clientes  
**Quantidade de variáveis:** 21 colunas  

Cada linha representa um cliente e suas características contratuais, de uso e demográficas.

| Tipo de Informação | Variáveis Exemplo |
|--------------------|------------------|
| **Dados Demográficos** | `gender`, `SeniorCitizen`, `Partner`, `Dependents` |
| **Dados de Serviço** | `PhoneService`, `InternetService`, `StreamingTV`, `TechSupport` |
| **Dados Contratuais** | `Contract`, `PaymentMethod`, `PaperlessBilling` |
| **Dados Financeiros** | `MonthlyCharges`, `TotalCharges`, `tenure` |
| **Variável Alvo** | `Churn` (Yes/No) |

---

## ⚙️ **Etapas do Projeto**

### **1. Importação de Bibliotecas e Leitura dos Dados**
Utilizamos bibliotecas como **Pandas**, **NumPy**, **Seaborn**, **Matplotlib**, e **Scikit-learn** para manipulação e modelagem dos dados.

### **2. Entendimento e Exploração Inicial**
- Análise do formato dos dados (`.info()`, `.describe()`).
- Contagem de valores de churn (`Churn`).
- Verificação de tipos de variáveis (numéricas e categóricas).

### **3. Análise de Valores Ausentes**
- Identificação visual com **missingno**.
- Conversão de `TotalCharges` para tipo numérico.
- Remoção de registros inconsistentes (`tenure = 0`).

### **4. Manipulação e Limpeza de Dados**
- Exclusão de colunas irrelevantes (`customerID`).
- Mapeamento de variáveis binárias (`SeniorCitizen` → “Yes”/“No”).
- Codificação de variáveis categóricas com **LabelEncoder**.

### **5. Análise Exploratória (EDA)**
Exploração gráfica para entender padrões e relações:
- Distribuição de churn.
- Comparações entre churn e variáveis contratuais.
- Correlação entre variáveis numéricas (heatmap).

### **6. Pré-processamento**
- Padronização de atributos numéricos com **StandardScaler**.
- Divisão dos dados em **conjuntos de treino e teste (80/20)**.

### **7. Modelagem e Avaliação**
Foram testados diferentes algoritmos de classificação:
- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Support Vector Classifier (SVC)  
- Decision Tree  
- Random Forest  
- AdaBoost  
- Gradient Boosting  

Cada modelo foi avaliado com as métricas:
- **Accuracy (Acurácia)**
- **Precision (Precisão)**
- **Recall (Sensibilidade)**
- **F1-Score**
- **Matriz de Confusão**

### **8. Comparação de Resultados**
- Comparação visual dos desempenhos (barplot).
- Discussão sobre o modelo com melhor equilíbrio entre recall e precisão.

### **9. Conclusões e Insights de Negócio**
- Identificação dos principais fatores relacionados ao churn.
- Sugestões para ações de retenção de clientes.
- Indicação de próximos passos (tuning, SMOTE, feature importance, etc.).

---

## 🧠 **Principais Insights Esperados**

- Clientes com **contratos mensais** têm maior probabilidade de churn.  
- **Pagamentos eletrônicos (electronic check)** estão mais associados ao churn.  
- Clientes com **serviço de Internet “Fiber optic”** tendem a ter maior rotatividade.  
- O **tempo de contrato (tenure)** é uma das variáveis mais relevantes.  

---

## 📈 **Resultados Esperados**

| Modelo | Acurácia Esperada | Observações |
|--------|-------------------|-------------|
| Logistic Regression | ~80% | Simples e interpretável |
| Random Forest | ~83-85% | Melhor equilíbrio entre precisão e recall |
| Gradient Boosting | ~86-87% | Potencialmente o melhor desempenho geral |

---

## 🧾 **Conclusões**

- A previsão de churn é viável e oferece **grande valor estratégico** para o negócio.  
- Modelos de ensemble (Random Forest, Gradient Boosting) apresentaram melhor desempenho.  
- As análises permitiram identificar **perfis de clientes mais propensos a cancelar o serviço**, permitindo que a empresa direcione **campanhas de retenção mais eficazes**.  

---

## 🧰 **Ferramentas Utilizadas**
- **Python 3.10+**
- **Google Colab / Jupyter Notebook**
- **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn**
- **Scikit-learn**
- **Missingno**

---