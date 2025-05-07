from zeep import Client

client = Client('http://localhost:8000/?wsdl')

titulo = input("Título do livro: ")
autor = input("Autor do livro: ")

resposta = client.service.AdicionarLivro(titulo, autor)
print(f"[Bibliotecário] {resposta}")
