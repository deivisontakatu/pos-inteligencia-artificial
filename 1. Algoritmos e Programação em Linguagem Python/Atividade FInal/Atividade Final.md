# Projeto: Análise Manual do Dataset Disney+

## Descrição

Este projeto realiza a análise manual do dataset de filmes e séries da Disney+, utilizando apenas funcionalidades básicas de manipulação de arquivos em Python. O objetivo é extrair informações relevantes do arquivo CSV e gerar um relatório estatístico detalhado, sem o uso de bibliotecas como `csv` ou `pandas`.

## Estrutura do Projeto

- `abrir_filmes_disney.py`: Código principal que contém as classes, funções de leitura do dataset e geração do relatório.
- `disney_plus_shows.csv`: Arquivo de dados com informações dos filmes e séries da Disney+.
- `relatorio-disney.txt`: Relatório gerado automaticamente com estatísticas e informações extraídas do dataset.
- `TrabalhoFinal.ipynb`: Notebook com instruções e enunciado do exercício.

## Funcionalidades

- Leitura manual do arquivo CSV, ignorando linhas vazias.
- Criação das classes `Filme` e `Serie` para representar cada obra.
- Conversão de campos "N/A" para `None`.
- Cálculo de estatísticas:
  - Média das notas IMDB e Metascore dos filmes.
  - Média de votos IMDB dos filmes.
  - Idiomas mais e menos usados.
  - Atores mais e menos presentes.
  - Diretor com mais filmes.
  - Diretor com o filme mais bem avaliado (IMDB e Metascore).
  - Ano com mais lançamentos.
  - Pior série segundo IMDB e Metascore.
  - Lista de filmes com múltiplos lançamentos (remakes).

## Como Executar

1. Certifique-se de que o arquivo `disney_plus_shows.csv` está presente na pasta correta.
2. Execute o script principal:

   ```bash
   python abrir_filmes_disney.py