# fila_livros.py
fila_livros = []

def adicionar_livro(titulo, autor):
    livro = {"titulo": titulo, "autor": autor}
    fila_livros.append(livro)
    return f"Livro '{titulo}' adicionado com sucesso!"

def retirar_livro():
    if fila_livros:
        return fila_livros.pop(0)
    else:
        return {"titulo": "Nenhum livro disponível", "autor": "-"}
