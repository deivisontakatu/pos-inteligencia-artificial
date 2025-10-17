from pathlib import Path
from typing import List

# Define os caminhos dos arquivos de entrada e saída
BASE = Path("C:/Users/Acer/Downloads")
ARQ = BASE / "242804-Atividade-Final/disney_plus_shows.csv"
ARQSaida = BASE / "242804-Atividade-Final/relatorio-disney.txt"

# Classe base para representar uma obra (filme ou série)


class Obra:
    def __init__(self, imdb_id, titulo, plot, rated, ano, lancamento, adicionado, duracao, genero, diretor, escritor, atores, idioma, pais, premios, metascore, imdb_rating, imdb_votes):
        self.set_imdb_id(imdb_id)
        self.set_titulo(titulo)
        self.set_plot(plot)
        self.set_rated(rated)
        self.set_ano(ano)
        self.set_lancamento(lancamento)
        self.set_adicionado(adicionado)
        self.set_duracao(duracao)
        self.set_genero(genero)
        self.set_diretor(diretor)
        self.set_escritor(escritor)
        self.set_atores(atores)
        self.set_idioma(idioma)
        self.set_pais(pais)
        self.set_premios(premios)
        self.set_metascore(metascore)
        self.set_imdb_rating(imdb_rating)
        self.set_imdb_votes(imdb_votes)

    def get_imdb_id(self): return self.imdb_id
    def set_imdb_id(
        self, imdb_id): self.imdb_id = imdb_id != "N/A" and imdb_id or None

    def get_titulo(self): return self.titulo
    def set_titulo(
        self, titulo): self.titulo = titulo != "N/A" and titulo or None

    def get_plot(self): return self.plot
    def set_plot(self, plot): self.plot = plot != "N/A" and plot or None
    def get_rated(self): return self.rated
    def set_rated(self, rated): self.rated = rated != "N/A" and rated or None
    def get_ano(self): return self.ano
    def set_ano(self, ano): self.ano = ano != "N/A" and ano or None
    def get_lancamento(self): return self.lancamento
    def set_lancamento(
        self, lancamento): self.lancamento = lancamento != "N/A" and lancamento or None

    def get_adicionado(self): return self.adicionado
    def set_adicionado(
        self, adicionado): self.adicionado = adicionado != "N/A" and adicionado or None

    def get_duracao(self): return self.duracao
    def set_duracao(
        self, duracao): self.duracao = duracao != "N/A" and duracao or None

    def get_genero(self): return self.genero
    def set_genero(
        self, genero): self.genero = genero != "N/A" and genero or None

    def get_diretor(self): return self.diretor
    def set_diretor(
        self, diretor): self.diretor = diretor != "N/A" and diretor or None

    def get_escritor(self): return self.escritor
    def set_escritor(
        self, escritor): self.escritor = escritor != "N/A" and escritor or None

    def get_atores(self): return self.atores
    def set_atores(
        self, atores): self.atores = atores != "N/A" and atores or None

    def get_idioma(self): return self.idioma
    def set_idioma(
        self, idioma): self.idioma = idioma != "N/A" and idioma or None

    def get_pais(self): return self.pais
    def set_pais(self, pais): self.pais = pais != "N/A" and pais or None
    def get_premios(self): return self.premios
    def set_premios(
        self, premios): self.premios = premios != "N/A" and premios or None

    def get_metascore(self): return self.metascore
    def set_metascore(
        self, metascore): self.metascore = metascore != "N/A" and metascore or None

    def get_imdb_rating(self): return self.imdb_rating
    def set_imdb_rating(
        self, imdb_rating): self.imdb_rating = imdb_rating != "N/A" and imdb_rating or None

    def get_imdb_votes(self): return self.imdb_votes
    def set_imdb_votes(
        self, imdb_votes): self.imdb_votes = imdb_votes != "N/A" and imdb_votes or None


class Serie(Obra):
    pass


class Filme(Obra):
    pass


Obras: List[Obra] = []
Filmes: List[Filme] = []
Series: List[Serie] = []


def parse_csv_line(line: str, sep: str = ","):
    campos = []
    atual = []
    em_aspas = False
    i = 0
    while i < len(line):
        ch = line[i]
        if em_aspas:
            if ch == '"':
                if i + 1 < len(line) and line[i + 1] == '"':
                    atual.append('"')
                    i += 2
                else:
                    em_aspas = False
                    i += 1
            else:
                atual.append(ch)
                i += 1
        else:
            if ch == '"':
                em_aspas = True
                i += 1
            elif ch == sep:
                campos.append("".join(atual))
                atual = []
                i += 1
            else:
                if ch not in ("\r", "\n"):
                    atual.append(ch)
                i += 1
    campos.append("".join(atual))
    return campos


def abrir_filmes_disney():
    with open(ARQ, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip():
                colunas = parse_csv_line(linha)
                if colunas[3] == "movie":
                    filme = Filme(colunas[0], colunas[1], colunas[2], colunas[4], colunas[5], colunas[6], colunas[7], colunas[8], colunas[9],
                                  colunas[10], colunas[11], colunas[12], colunas[13], colunas[14], colunas[15], colunas[16], colunas[17], colunas[18])
                    Filmes.append(filme)
                    Obras.append(filme)
                elif colunas[3] == "series":
                    serie = Serie(colunas[0], colunas[1], colunas[2], colunas[4], colunas[5], colunas[6], colunas[7], colunas[8], colunas[9],
                                  colunas[10], colunas[11], colunas[12], colunas[13], colunas[14], colunas[15], colunas[16], colunas[17], colunas[18])
                    Series.append(serie)
                    Obras.append(serie)
    return Obras


def gerar_relatorio(Obras: List[Obra]):
    with open(ARQSaida, "w", encoding="utf-8") as file:
        file.write("Relatórios Disney\n")
        file.write("=================\n\n")
        file.write(f"Total de obras: {len(Obras)}\n")
        file.write(f"Total de filmes: {len(Filmes)}\n")
        file.write(f"Total de séries: {len(Series)}\n\n")

        # Média IMDB dos filmes
        imdb_media = sum(float(f.get_imdb_rating()) for f in Filmes if f.get_imdb_rating(
        ) is not None) / max(1, sum(1 for f in Filmes if f.get_imdb_rating() is not None))
        file.write(f"Média IMDB: {imdb_media:.2f}\n\n")

        # Média Metascore dos filmes
        metascore_media = sum(float(f.get_metascore()) for f in Filmes if f.get_metascore(
        ) is not None) / max(1, sum(1 for f in Filmes if f.get_metascore() is not None))
        file.write(f"Média Metascore: {metascore_media:.2f}\n\n")

        # Média de votos IMDB dos filmes
        votos_media = sum(float(f.get_imdb_votes().replace(',', '').replace('.', '')) for f in Filmes if f.get_imdb_votes(
        ) is not None) / max(1, sum(1 for f in Filmes if f.get_imdb_votes() is not None))
        file.write(f"Média de votos Imdb: {votos_media:.0f}\n\n")

        # Idiomas
        idiomas_count = {}
        for o in Obras:
            if o.get_idioma():
                for idioma in o.get_idioma().split(","):
                    idioma = idioma.strip()
                    idiomas_count[idioma] = idiomas_count.get(idioma, 0) + 1
        idiomas_ordenados = sorted(
            idiomas_count.items(), key=lambda x: x[1], reverse=True)
        file.write("3 idiomas que mais aparecem:\n")
        for idioma, qtd in idiomas_ordenados[:3]:
            file.write(f" - {idioma}: {qtd}\n")
        file.write("3 idiomas que menos aparecem:\n")
        for idioma, qtd in idiomas_ordenados[-3:]:
            file.write(f" - {idioma}: {qtd}\n")

        # Atores
        atores_count = {}
        for o in Obras:
            if o.get_atores():
                for ator in o.get_atores().split(","):
                    ator = ator.strip()
                    atores_count[ator] = atores_count.get(ator, 0) + 1
        atores_ordenados = sorted(
            atores_count.items(), key=lambda x: x[1], reverse=True)
        file.write("3 atores que mais aparecem:\n")
        for ator, qtd in atores_ordenados[:3]:
            file.write(f" - {ator}: {qtd}\n")
        file.write("3 atores que menos aparecem:\n")
        for ator, qtd in atores_ordenados[-3:]:
            file.write(f" - {ator}: {qtd}\n")

        # Diretores
        diretores_count = {}
        for f in Filmes:
            if f.get_diretor():
                for diretor in f.get_diretor().split(","):
                    diretor = diretor.strip()
                    diretores_count[diretor] = diretores_count.get(
                        diretor, 0) + 1
        diretores_ordenados = sorted(
            diretores_count.items(), key=lambda x: x[1], reverse=True)
        diretor_top, qtd_top = diretores_ordenados[0] if diretores_ordenados else (
            "-", 0)
        file.write(
            f"Diretor com mais filmes: {diretor_top} ({qtd_top} filmes)\n\n")

        # Diretor com filme mais popular IMDB
        filme_imdb_max = max(Filmes, key=lambda f: float(
            f.get_imdb_rating()) if f.get_imdb_rating() is not None else -1, default=None)
        if filme_imdb_max:
            file.write(
                f"Diretor do filme mais bem avaliado no IMDB: {filme_imdb_max.get_diretor()} (Filme: {filme_imdb_max.get_titulo()}, Nota: {filme_imdb_max.get_imdb_rating()})\n")
        # Diretor com filme mais popular Metascore
        filme_meta_max = max(Filmes, key=lambda f: float(
            f.get_metascore()) if f.get_metascore() is not None else -1, default=None)
        if filme_meta_max:
            file.write(
                f"Diretor do filme mais bem avaliado no Metascore: {filme_meta_max.get_diretor()} (Filme: {filme_meta_max.get_titulo()}, Nota: {filme_meta_max.get_metascore()})\n")

        # Ano com mais filmes lançados
        anos_count = {}
        for f in Filmes:
            ano = f.get_ano()
            if ano:
                anos_count[ano] = anos_count.get(ano, 0) + 1
        if anos_count:
            ano_top = max(anos_count.items(), key=lambda x: x[1])
            file.write(
                f"Ano com mais filmes lançados: {ano_top[0]} ({ano_top[1]} filmes)\n\n")

        # Pior série IMDB
        serie_imdb_min = min(Series, key=lambda s: float(s.get_imdb_rating(
        )) if s.get_imdb_rating() is not None else float('inf'), default=None)
        if serie_imdb_min:
            file.write(
                f"Pior série segundo IMDB: {serie_imdb_min.get_titulo()} (Nota: {serie_imdb_min.get_imdb_rating()})\n")
        # Pior série Metascore
        series_com_metascore = [
            s for s in Series if s.get_metascore() is not None]
        if series_com_metascore:
            serie_meta_min = min(series_com_metascore,
                                 key=lambda s: float(s.get_metascore()))
            file.write(
                f"Pior série segundo Metascore: {serie_meta_min.get_titulo()} (Nota: {serie_meta_min.get_metascore()})\n")
        else:
            file.write("Nenhuma série possui nota Metascore.\n")

        # Filmes com múltiplos lançamentos (remakes)
        titulosAnos = {}
        for f in Filmes:
            titulo = f.get_titulo()
            ano = f.get_ano()
            if titulo and ano:
                titulosAnos.setdefault(titulo, set()).add(ano)
        remakes = [(titulo, sorted(anos))
                   for titulo, anos in titulosAnos.items() if len(anos) > 1]
        if remakes:
            file.write("Filmes com múltiplos lançamentos (remakes):\n")
            for titulo, anos in remakes:
                file.write(f" - {titulo}: {', '.join(anos)}\n")
        else:
            file.write("Nenhum filme com múltiplos lançamentos encontrado.\n")


# Executa a leitura do arquivo e gera o relatório
if __name__ == "__main__":
    Obras = abrir_filmes_disney()
    gerar_relatorio(Obras)
    print("Relatório concluído.")
