import grpc
import sistema_pb2
import sistema_pb2_grpc

def executar():
    """Executa o usuário """
    conexao = grpc.insecure_channel('localhost:50051')
    servico = sistema_pb2_grpc.ServicoBibliotecaStub(conexao)

    print("### PEGAR LIVRO ###")
    livro = servico.PegarLivro(sistema_pb2.Vazio())
    print(f"[USUÁRIO] Livro retirado: '{livro.titulo}' por {livro.autor}")

if __name__ == '__main__':
    executar()