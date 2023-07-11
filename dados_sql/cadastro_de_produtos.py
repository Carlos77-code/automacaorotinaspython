import pyodbc

class CadastroProduto:
    def __init__(self, servidor, banco_dados):
        self.servidor = servidor
        self.banco_dados = banco_dados
        self.conexao = None
        self.cursor = None

    def conectar_banco_dados(self):
        dados_conexao = (
            f"Driver={{SQL Server}};"
            f"Server={self.servidor};"
            f"Database={self.banco_dados};"
        )
        self.conexao = pyodbc.connect(dados_conexao)
        self.cursor = self.conexao.cursor()
        print("Conexão Bem Sucedida")

    def adicionar_venda(self, id, cliente, produto, data, preco, quantidade):
        comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
                    VALUES
                        ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""
        self.cursor.execute(comando)
        self.cursor.commit()

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()

# Exemplo de uso da classe CadastroProduto
servidor = "DESKTOP-5EN21VC\\SQLEXPRESS"
banco_dados = "Nome_Banco_Dados"

page = CadastroProduto(servidor, banco_dados)
page.conectar_banco_dados()

id = 5
cliente = "Gilson"
produto = "Fretes"
data = "1970/01/13"
preco = 500
quantidade = 10

page.adicionar_venda(id, cliente, produto, data, preco, quantidade)

page.fechar_conexao()
