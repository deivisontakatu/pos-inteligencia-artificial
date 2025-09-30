# Explicação dos Algoritmos

Este documento explica o funcionamento dos algoritmos presentes no arquivo [trabalho_aula_2-1.ipynb](c:/Users/Acer/Downloads/trabalho_aula_2-1.ipynb) e os parâmetros que podem ser alterados para uso em outros cenários.

---

## Exercício 1: Par ou Ímpar em Arquivo

- **Função:** [`par_ou_impar_arquivo`](c:/Users/Acer/Downloads/trabalho_aula_2-1.ipynb)
- **Descrição:** Recebe um número inteiro `n` e escreve em um arquivo se cada número de 1 até `n` é par ou ímpar.
- **Parâmetros alteráveis:**
  - O valor de entrada `n` (número inteiro desejado).
  - O nome do arquivo de saída pode ser alterado na linha:  
    ```python
    caminho = Path("exercicio1_resultado.txt")
    ```

---

## Exercício 2: Soma de Números em Arquivo

- **Função:** [`somar_numeros_arquivo`](c:/Users/Acer/Downloads/trabalho_aula_2-1.ipynb)
- **Descrição:** Lê números de um arquivo de entrada, soma todos e escreve o resultado em um arquivo de saída.
- **Parâmetros alteráveis:**
  - Nome do arquivo de entrada (`arquivo_entrada`).
  - Nome do arquivo de saída (`arquivo_saida`).
  - O caminho base pode ser ajustado na variável `BASE`:
    ```python
    BASE = Path("C:/Users/Acer/Downloads")
    ```

---

## Exercício 3: Classificação de Números

- **Função:** [`classificar_numeros_em_arquivo`](c:/Users/Acer/Downloads/trabalho_aula_2-1.ipynb)
- **Descrição:** Classifica cada número do arquivo de entrada como "Positivo", "Negativo" ou "Zero" e escreve o resultado em um arquivo de saída.
- **Parâmetros alteráveis:**
  - Nome do arquivo de entrada (`arquivo_entrada`).
  - Nome do arquivo de saída (`arquivo_saida`).
  - O caminho base (`BASE`).

---

## Exercício 4: Processamento de Dados de Alunos

- **Função:** [`processar_dados_alunos`](c:/Users/Acer/Downloads/trabalho_aula_2-1.ipynb)
- **Descrição:** Lê dados de alunos (nome e três notas), calcula a média e determina se foi aprovado ou reprovado.
- **Parâmetros alteráveis:**
  - Nome do arquivo de entrada (`arquivo_entrada`).
  - O nome do arquivo de saída pode ser alterado na linha:
    ```python
    caminho_saida = BASE / "exercicio4_resultados_alunos.txt"
    ```
  - O caminho base (`BASE`).

---

## Exercício 5: Processamento Manual de Vendas

- **Função:** [`processar_vendas_manual`](c:/Users/Acer/Downloads/trabalho_aula_2-1.ipynb)
- **Descrição:** Lê dados de vendas de um arquivo CSV, calcula o valor total de cada venda e escreve em um novo arquivo CSV.
- **Parâmetros alteráveis:**
  - Nome do arquivo de entrada (`arquivo_entrada`).
  - Nome do arquivo de saída (`arquivo_saida`).
  - O caminho base (`BASE`).

---

## Observações Gerais

- **Caminho Base:** Todos os algoritmos usam a variável `BASE` para definir o diretório dos arquivos. Altere `BASE` conforme o local desejado.
- **Tratamento de Erros:** Os algoritmos tratam erros de arquivos não encontrados e dados inválidos, exibindo mensagens informativas.
- **Formato dos Arquivos:** Certifique-se de que os arquivos de entrada estejam no formato esperado (um número por linha, dados separados por vírgula, etc.).

---

**Para utilizar os algoritmos com outros arquivos ou diretórios, basta alterar os parâmetros indicados acima.**