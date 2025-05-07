from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

fila_livros = []

class BibliotecaService(ServiceBase):

    @rpc(Unicode, Unicode, _returns=Unicode)
    def AdicionarLivro(ctx, titulo, autor):
        livro = {"titulo": titulo, "autor": autor}
        fila_livros.append(livro)
        print(f"[Servidor] Livro adicionado: {livro}")
        return f"Livro '{titulo}' adicionado com sucesso!"

    @rpc(_returns=Unicode)
    def PegarLivro(ctx):
        if fila_livros:
            livro = fila_livros.pop(0)
            print(f"[Servidor] Livro retirado: {livro}")
            return f"{livro['titulo']}|{livro['autor']}"
        else:
            return "Nenhum livro disponível|-"

app = Application([BibliotecaService],
                  tns='biblioteca.soap',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11())

wsgi_app = WsgiApplication(app)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print("Servidor SOAP rodando em http://localhost:8000")
    server = make_server('127.0.0.1', 8000, wsgi_app)
    server.serve_forever()
