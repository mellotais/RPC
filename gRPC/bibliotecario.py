import grpc
import sistema_pb2
import sistema_pb2_grpc

def executar():
    """Executa o bibliotecário """
    conexao = grpc.insecure_channel('localhost:50051')
    servico = sistema_pb2_grpc.ServicoBibliotecaStub(conexao)

    print("### ADICIONAR LIVRO ###")
    titulo = input("Título: ")
    autor = input("Autor: ")

    resposta = servico.AdicionarLivro(sistema_pb2.Livro(titulo=titulo, autor=autor))
    print(f"[BIBLIOTECÁRIO] {resposta.mensagem}")

if __name__ == '__main__':
    executar()