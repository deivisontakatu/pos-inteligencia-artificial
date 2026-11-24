# Atividade 01 — MLOps e Deploy de Modelos em Produção

**Aluno:** Deivison Shindi Takatu  
**Projeto prático:** Pipeline de previsão de demanda de bicicletas  
**Repositório de implementação:** https://github.com/deivisontakatu/aula-mlops  
**Branch:** `desafio01-mlops`

---

## 1. Objetivo da atividade

O objetivo foi implementar um fluxo inicial de MLOps para organizar o ciclo de vida de um modelo de Machine Learning. O projeto utiliza dados históricos de demanda horária de bicicletas e integra duas ferramentas principais:

- **DVC (Data Version Control):** versionamento de dados e organização/execução do pipeline.
- **MLflow:** rastreamento de experimentos, registro de versões de modelos e gerenciamento de aliases.

O fluxo desenvolvido contempla preparação dos dados, divisão entre treino e teste, treinamento, avaliação, geração de gráfico e comparação de modelos.

## 2. Conceitos importantes

### 2.1. MLOps

MLOps reúne práticas de engenharia de software e operações aplicadas a projetos de Machine Learning. Busca tornar o desenvolvimento, treinamento, avaliação, implantação e manutenção de modelos mais organizados, reproduzíveis e rastreáveis.

### 2.2. Versionamento de dados

O resultado de um modelo depende não apenas do código, mas também dos dados utilizados. Por isso, é importante registrar qual conjunto de dados foi usado em cada experimento. O DVC registra os metadados e identificadores dos dados, enquanto o Git mantém o histórico dos arquivos de configuração e referências.

### 2.3. Pipeline

Um pipeline é uma sequência de etapas encadeadas. Cada etapa recebe dados ou artefatos, executa uma operação e produz saídas utilizadas pelas etapas seguintes. O DVC permite declarar esse fluxo em `dvc.yaml` e registrar o estado executado em `dvc.lock`.

### 2.4. Rastreamento de experimentos e Model Registry

O MLflow Tracking registra parâmetros, métricas, informações da execução e artefatos. O Model Registry organiza as versões dos modelos registrados e permite associar aliases a versões específicas.

### 2.5. Champion e Challenger

- **Champion:** versão de referência atualmente adotada.
- **Challenger:** versão candidata a substituir a referência.

Uma comparação válida exige duas versões distintas avaliadas sobre o mesmo conjunto de teste. Neste projeto, a regra definida considera o RMSE: o Challenger só é vencedor se apresentar RMSE estritamente menor que o Champion. O alias é apenas um nome associado a uma versão; dois aliases podem apontar para a mesma versão.

### 2.6. Métricas

- **RMSE:** raiz do erro quadrático médio; valores menores indicam menor erro, com penalização maior para erros grandes.
- **MAE:** erro absoluto médio; valores menores indicam menor erro absoluto médio.
- **R²:** coeficiente de determinação; indica quanto da variação do alvo é explicada pelo modelo. Em geral, quanto mais próximo de 1, melhor.

As métricas só podem ser comparadas adequadamente quando os modelos foram avaliados no mesmo conjunto de teste.

---

## 3. Repositório e ambiente

O desenvolvimento foi realizado em um GitHub Codespace. Para reproduzir em outro ambiente:

```bash
git clone https://github.com/deivisontakatu/aula-mlops.git
cd aula-mlops
git checkout desafio01-mlops
git branch --show-current
git status
```

A branch esperada é `desafio01-mlops`.

### 3.1. Ambiente Python

Criar e ativar um ambiente virtual:

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
```

Conferir a versão do Python:

```bash
python --version
```

Instalar as dependências conforme o arquivo de requisitos existente no repositório. Quando houver `requirements.txt`:

```bash
pip install -r requirements.txt
```

> A versão de Python e das bibliotecas deve ser compatível com os scripts do projeto. Caso não exista arquivo de dependências, consultar a configuração disponibilizada na disciplina antes de instalar versões arbitrárias.

## 4. Estrutura do projeto

| Arquivo/diretório | Finalidade |
|---|---|
| `data/raw/bike.csv` | Dados originais |
| `data/raw/bike.csv.dvc` | Metadados DVC do conjunto de dados |
| `src/bike.py` | Funções compartilhadas, características e métricas |
| `src/prepare.py` | Preparação dos dados |
| `src/split.py` | Separação entre treino e teste |
| `src/train.py` | Treinamento e registro do modelo |
| `src/evaluate.py` | Avaliação |
| `src/plot.py` | Geração do gráfico previsto versus real |
| `dvc.yaml` | Definição das etapas do pipeline |
| `dvc.lock` | Registro das dependências e saídas da execução |
| `params.yaml` | Parâmetros de divisão e treinamento |
| `desafio01/compare_models.py` | Comparação Champion/Challenger |
| `desafio01/RELATORIO.md` | Relatório da atividade |
| `metrics.json` | Métricas da avaliação |
| `reports/comparacao.json` | Resultado da comparação |
| `reports/previsto_vs_real.png` | Gráfico de avaliação |
| `models/` | Artefatos locais do treinamento |

---

## 5. Versionamento de dados com DVC

### 5.1. Verificar o DVC

No repositório utilizado, o DVC já estava inicializado. Conferir a instalação e o estado:

```bash
dvc --version
git status
```

Em um projeto novo, inicializar somente se ainda não houver configuração DVC:

```bash
dvc init
git add .dvc .dvcignore
git commit -m "Inicializa DVC no projeto"
```

### 5.2. Rastrear o conjunto de dados

O conjunto de dados foi adicionado ao DVC com:

```bash
dvc add data/raw/bike.csv
```

O comando cria ou atualiza `data/raw/bike.csv.dvc`, que contém os metadados necessários para identificar o conteúdo rastreado. O arquivo de dados é gerenciado pelo DVC e o arquivo de metadados é acompanhado pelo Git.

Registrar as alterações:

```bash
git add data/raw/bike.csv.dvc data/.gitignore .gitignore
git commit -m "Versiona dados com DVC"
```

### 5.3. Conferir hash e tags

Consultar o hash MD5 salvo no arquivo DVC:

```bash
grep md5 data/raw/bike.csv.dvc
```

Na versão `dados-v3` deste trabalho, o hash completo foi:

```text
7747b2efcdd3801b83c1cfce2d600c15
```

Os oito primeiros caracteres são `7747b2ef`.

A tag `dados-v3` aponta para o commit:

```text
ab489681e18ef330ccbf21612fa6842c8831bb10
```

Listar tags locais e tags publicadas no remoto:

```bash
git tag -l
git ls-remote --tags origin
```

### 5.4. Observação sobre dados-v1 e dados-v2

Durante a atividade, foram procuradas as tags `dados-v1` e `dados-v2` no fork pessoal e no repositório original consultado. A consulta ao histórico acessível não retornou essas tags. O modelo inicial do relatório apresentava o prefixo `fc7d423a` para `dados-v1`, mas a referência Git correspondente não foi encontrada. Portanto, não foram criadas tags retroativamente nem inventados hashes para as versões ausentes.

### 5.5. Remoto de armazenamento DVC

O versionamento de metadados no Git não equivale ao envio dos arquivos de dados a um remoto DVC. Para compartilhar os objetos de dados entre máquinas, é necessário configurar um storage remoto e então utilizar `dvc push`.

Nesta execução, não foi configurado um remoto DVC e, por isso, não foi executado `dvc push`. Em uma reprodução em outro computador, será necessário disponibilizar o arquivo original ou configurar o remoto de armazenamento correto antes de executar o pipeline.

---

## 6. Configuração e execução do pipeline

### 6.1. Parâmetros

O arquivo `params.yaml` centraliza os parâmetros utilizados:

```yaml
split:
  test_days: 28
train:
  learning_rate: 0.1
  max_iter: 300
  max_leaf_nodes: 31
  random_state: 42
mlflow:
  experiment: bike-demand-pipeline
```

O parâmetro `test_days` define o período reservado para teste. Os parâmetros em `train` controlam a configuração do treinamento. O `random_state` ajuda a controlar a aleatoriedade quando aplicável.

### 6.2. Etapas definidas no dvc.yaml

O pipeline foi organizado nas etapas:

| Etapa | Comando | Responsabilidade |
|---|---|---|
| `prepare` | `python src/prepare.py` | Preparar os dados |
| `split` | `python src/split.py` | Separar treino e teste |
| `train` | `python src/train.py` | Treinar e registrar o modelo |
| `evaluate` | `python src/evaluate.py` | Calcular métricas |
| `plot` | `python src/plot.py` | Gerar gráfico de previsto versus real |
| `compare` | `python desafio01/compare_models.py` | Comparar os aliases registrados |

O DVC acompanha as dependências e parâmetros declarados. Quando uma dependência muda, ele identifica quais etapas precisam ser executadas novamente.

### 6.3. Visualizar o grafo

```bash
dvc dag
```

Esse comando apresenta as dependências entre as etapas e permite conferir a ordem lógica do pipeline.

### 6.4. Reproduzir o treinamento inicial

Com os dados disponíveis e o servidor MLflow ativo, executar:

```bash
dvc repro train
```

Na execução realizada, o pipeline preparou 17.379 registros, sem remoção de linhas, e gerou:

- Treino: 16.709 linhas.
- Teste: 670 linhas.
- Período de teste: 04/12/2012 a 31/12/2012.

O treinamento registrou a primeira versão do modelo `bike-demand` no MLflow Registry.

### 6.5. Definir o alias Champion

Depois do primeiro treinamento, a versão 1 foi definida como Champion. O comando utilizado foi:

```bash
python -c "import json,sys; sys.path.insert(0,'src'); from bike import MODEL_NAME,tracking_uri; import mlflow; from mlflow import MlflowClient; mlflow.set_tracking_uri(tracking_uri()); v=str(json.load(open('models/run.json'))['model_version']); c=MlflowClient(); c.set_registered_model_alias(MODEL_NAME,'champion',v); print(f'{MODEL_NAME} champion -> versão {v}')"
```

Resultado obtido:

```text
bike-demand champion -> versão 1
```

O comando consulta a versão registrada em `models/run.json` e associa o alias `champion` a ela.

---

## 7. Inicialização e uso do MLflow

### 7.1. Iniciar o servidor

Foi utilizado o script disponibilizado no projeto:

```bash
bash scripts/start_mlflow.sh
```

Manter o terminal do servidor aberto enquanto o pipeline é executado. No Codespaces, verificar a aba **Ports** e disponibilizar a porta 5000 quando necessário.

O endereço local padrão utilizado pela configuração do projeto é:

```text
http://127.0.0.1:5000
```

No Codespaces, abrir a URL encaminhada pelo próprio ambiente para acessar a interface no navegador.

### 7.2. Consultar os experimentos

Na interface do MLflow, localizar o experimento `bike-demand-pipeline`. Cada execução registrada apresenta informações como parâmetros, métricas, identificador da execução e artefatos.

O modelo foi registrado com o nome `bike-demand`. O Registry organiza suas versões, e aliases como `champion` e `challenger` permitem referenciá-las sem depender de números fixos no código consumidor.

---

## 8. Avaliação, gráfico e comparação

### 8.1. Executar o pipeline completo

Com o servidor MLflow em execução:

```bash
dvc repro
```

Esse comando executa as etapas necessárias do pipeline, respeitando as dependências definidas em `dvc.yaml`.

Na execução registrada, a avaliação produziu:

| Métrica | Resultado |
|---|---:|
| RMSE | 62,8937 |
| MAE | 41,5057 |
| R² | 0,8478 |

O gráfico `reports/previsto_vs_real.png` foi gerado e associado à execução do MLflow.

### 8.2. Arquivo de comparação

O script `desafio01/compare_models.py` carrega os modelos apontados pelos aliases e calcula as métricas para o mesmo conjunto de teste. A decisão de vitória utiliza a condição:

```python
venceu = chall["rmse"] < champ["rmse"]
```

Ou seja, a versão Challenger só vence se o RMSE for estritamente menor que o do Champion.

O resultado estruturado é salvo em:

```text
reports/comparacao.json
```

### 8.3. Resultado observado nesta execução

A execução gerou:

| Alias | Versão | RMSE | MAE | R² |
|---|---:|---:|---:|---:|
| Champion | 1 | 62,8937 | 41,5057 | 0,8478 |
| Challenger | 1 | 62,8937 | 41,5057 | 0,8478 |

Os dois aliases apontaram para a mesma versão 1. Portanto, os números confirmam que o fluxo de comparação foi executado, mas **não representam uma competição real entre dois modelos diferentes**.

O script informou que o Challenger não venceu, pois as métricas eram idênticas. Não foi realizada promoção de modelo.

### 8.4. Como realizar uma comparação real entre versões

Para avaliar a política Champion/Challenger de forma efetiva, é necessário treinar e registrar uma segunda versão com uma configuração diferente, mantendo o mesmo conjunto de teste. Uma sequência conceitual é:

1. Manter o alias `champion` associado à versão de referência.
2. Alterar um parâmetro de treinamento em `params.yaml` (por exemplo, `max_iter`) para criar uma nova configuração experimental.
3. Executar novamente o treinamento para registrar uma nova versão no Model Registry.
4. Associar o alias `challenger` à nova versão, conforme a lógica do script.
5. Executar a comparação e verificar `reports/comparacao.json`.
6. Promover o Challenger somente se o RMSE for estritamente menor e após validar os resultados.

**Atenção:** os passos acima descrevem a continuação necessária para uma comparação real; ela não foi concluída na execução documentada. Antes de alterar os parâmetros ou aliases, conferir o comportamento atual de `src/train.py` e `desafio01/compare_models.py` para evitar sobrescrever a referência Champion ou apontar ambos os aliases para a mesma versão.

---

## 9. Versionamento e publicação no GitHub

Depois de executar o pipeline, conferir os arquivos modificados e gerados:

```bash
git status
```

Adicionar os arquivos de configuração e resultados que fazem parte da entrega:

```bash
git add .gitignore data/.gitignore dvc.lock metrics.json reports/
```

Conferir o que será incluído no commit:

```bash
git diff --cached --stat
```

Registrar o resultado:

```bash
git commit -m "Executa pipeline MLOps com DVC e MLflow"
```

Enviar a branch ao GitHub:

```bash
git push origin desafio01-mlops
```

No trabalho realizado, o envio da branch foi concluído com sucesso. O relatório específico da atividade foi mantido em `desafio01/RELATORIO.md`, no repositório do projeto.

---

## 10. Principais resultados e limitações

### Resultados alcançados

- DVC inicializado e utilizado para rastrear o conjunto de dados.
- Versão `dados-v3` confirmada, com hash MD5 iniciado por `7747b2ef`.
- Pipeline estruturado com preparação, divisão, treinamento, avaliação, geração de gráfico e comparação.
- MLflow iniciado e utilizado para registrar o experimento e a versão 1 do modelo `bike-demand`.
- Alias `champion` associado à versão 1.
- Métricas de avaliação geradas e artefatos publicados no repositório.
- Alterações e resultados enviados para a branch `desafio01-mlops`.

### Limitações identificadas

- As tags `dados-v1` e `dados-v2` não foram encontradas no histórico Git acessível.
- Não foi configurado um remoto DVC para compartilhamento dos objetos de dados.
- Champion e Challenger apontaram para a mesma versão (1), portanto a comparação registrada não comprova superioridade de uma nova versão.
- Uma segunda versão precisa ser treinada e avaliada para concluir a demonstração de comparação e promoção de modelos.

---

## 11. Comandos de referência

A sequência resumida para uma reprodução, considerando ambiente já configurado e dados disponíveis, é:

```bash
# Clonar e acessar a branch
git clone https://github.com/deivisontakatu/aula-mlops.git
cd aula-mlops
git checkout desafio01-mlops

# Conferir ambiente e DVC
python --version
dvc --version
git status

# Conferir os metadados dos dados
cat data/raw/bike.csv.dvc
git tag -l

# Visualizar o pipeline
dvc dag

# Em um terminal, iniciar o MLflow
bash scripts/start_mlflow.sh

# Em outro terminal, treinar e executar as etapas
dvc repro train
dvc repro

# Conferir os resultados
cat metrics.json
cat reports/comparacao.json
ls -lh reports/

# Conferir alterações e publicar
git status
git add .gitignore data/.gitignore dvc.lock metrics.json reports/
git diff --cached --stat
git commit -m "Executa pipeline MLOps com DVC e MLflow"
git push origin desafio01-mlops
```

Se o DVC indicar que os dados não estão disponíveis, primeiro recuperar o arquivo original ou configurar o remoto DVC apropriado. O comando `dvc repro` não substitui a obtenção dos dados de entrada.

---

## 12. Conclusão

A atividade permitiu estruturar um fluxo de Machine Learning com foco em rastreabilidade e reprodutibilidade. O DVC foi utilizado para versionar os dados e organizar as etapas do pipeline, enquanto o MLflow registrou o experimento e a primeira versão do modelo.

A execução confirmou o funcionamento das etapas de preparação, treinamento, avaliação e geração de artefatos. Também evidenciou um cuidado importante na governança de modelos: aliases Champion e Challenger só permitem uma comparação significativa quando apontam para versões distintas avaliadas nas mesmas condições. Assim, o projeto possui a estrutura inicial implementada, mas a comparação efetiva entre duas versões e a promoção de um Challenger permanecem como próximos passos técnicos.
