"""
SERVIDOR DA BIBLIOTECA

Funcionamento:
1. Guarda livros numa fila (o primeiro que chega é o primeiro que sai)
2. Escuta na porta 50051
3. Tem duas funções:
   - Cadastrar livro novo
   - Emprestar livro mais antigo
"""


import grpc
from concurrent import futures
import sistema_pb2
import sistema_pb2_grpc

class ServicoBiblioteca(sistema_pb2_grpc.ServicoBibliotecaServicer):
    
    def __init__(self):
        self.fila_livros = []

    def AdicionarLivro(self, requisicao, contexto):
        """Adiciona um livro novo no final da fila"""
        novo_livro = {"titulo": requisicao.titulo, "autor": requisicao.autor}
        self.fila_livros.append(novo_livro)
        print(f"[SERVIDOR] Livro adicionado: {novo_livro}")
        return sistema_pb2.Resposta(mensagem=f"Livro '{novo_livro['titulo']}' adicionado!")

    def PegarLivro(self, requisicao, contexto):
        """Entrega o livro mais antigo"""
        if self.fila_livros:
            livro = self.fila_livros.pop(0)
            print(f"[SERVIDOR] Livro emprestado: {livro}")
            return sistema_pb2.Livro(titulo=livro['titulo'], autor=livro['autor'])
        return sistema_pb2.Livro(titulo="Nenhum livro disponível", autor="-")

def iniciar_servidor():
    """Inicia o servidor"""
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sistema_pb2_grpc.add_ServicoBibliotecaServicer_to_server(ServicoBiblioteca(), servidor)
    servidor.add_insecure_port('[::]:50051')
    servidor.start()
    print("[SERVIDOR] Pronto para receber livros na porta 50051...")
    servidor.wait_for_termination()

if __name__ == '__main__':
    iniciar_servidor()