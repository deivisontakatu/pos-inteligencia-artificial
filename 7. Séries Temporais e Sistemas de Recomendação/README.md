# Séries Temporais e Sistemas de Recomendação

Materiais organizados por aula e atividade da disciplina da pós-graduação em Inteligência Artificial Aplicada (Machine Learning).

## Estrutura

- `Plano de Ensino/` — plano da disciplina e grade curricular.
- `Aula 01/` — fundamentos e análise de séries temporais, decomposição, estacionariedade, testes, modelos ARMA/ARIMA/SARIMA e Prophet.
- `Aula 02/` — redes neurais para previsão, MLP e LSTM, com notebooks e bases de dados de apoio.
- `Aula 03/` — sistemas de recomendação, KNN, filtragem colaborativa, K-Means, SVD/FunkSVD e ALS.
- `Aula 04/` — métricas para avaliar sistemas de recomendação.
- `Atividade 01/` — exercícios introdutórios de séries temporais.
- `Atividade 02/` — atividade prática complementar.
- `Atividade 03/` — exercícios de clustering e sistemas de recomendação.
- `Atividade 04/` — métricas e implementação de recomendação.
- `Quiz/` — questionários de séries temporais e sistemas de recomendação.
- `Referência/` — artigos e materiais complementares; verificar pertinência temática dos documentos incluídos.

## Convenção de nomes

Use nomes em `snake_case`, sem espaços no final, com extensões corretas e sem sufixos de download como `(1)` ou `(2)`, a menos que sejam necessários para distinguir versões diferentes. Prefira prefixos sequenciais somente quando a ordem fizer parte da atividade, por exemplo `01_`, `02_`.

## Como usar os notebooks

1. Abra os arquivos `.ipynb` no Jupyter Notebook, JupyterLab ou Google Colab.
2. Confira as dependências e caminhos dos arquivos de dados antes de executar.
3. Execute as células na ordem e valide os resultados.
4. Se um notebook depender de um CSV, mantenha a base na pasta correspondente e documente o caminho utilizado.

## Pontos a revisar

- Alguns nomes no acervo original têm erros de digitação, extensões duplicadas ou sufixos de cópia. A padronização dos nomes deve ser feita após conferir possíveis dependências e arquivos com nomes parecidos.
- A pasta `Atividade 03/` mistura exemplos de KNN, classificação, K-Means, filtragem por conteúdo e modelos SVD/ALS; considere subdividi-la por tema ou preservar nela apenas as entregas cobradas na atividade.
- A pasta `Referência/` contém trabalhos sobre acidentes envolvendo caminhões. Confirme se são fontes da disciplina ou material de outro projeto antes de manter esses arquivos aqui.
- Verifique se a Atividade 02 está identificada com título e instruções suficientes, pois o nome atual do notebook é genérico.
- Recomenda-se adicionar dependências por atividade (por exemplo, um `requirements.txt`) apenas depois de inspecionar todos os imports utilizados.