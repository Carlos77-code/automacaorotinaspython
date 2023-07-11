import pyodbc
import pandas as pd
import os

class BuscarDados:
    def __init__(self, servidor, banco_dados):
        self.servidor = servidor
        self.banco_dados = banco_dados
        self.conexao = None

    def conectar_banco_dados(self):
        dados_conexao = (
            f"Driver={{SQL Server}};"
            f"Server={self.servidor};"
            f"Database={self.banco_dados};"
        )
        self.conexao = pyodbc.connect(dados_conexao)
        print("Conexão Bem Sucedida")

    def buscar_dados_vendas(self):
        query = "SELECT * FROM Vendas"
        cursor = pd.read_sql(query, self.conexao)
        return cursor

    def salvar_em_excel(self, cursor, nome_arquivo):
        cursor.to_excel(nome_arquivo, index=False)

    def fechar_conexao(self):
        self.conexao.close()

# Exemplo de uso da classe PageObject
servidor = "DESKTOP-5EN21VC\\SQLEXPRESS"
banco_dados = "Nome_Banco_Dados"

page = BuscarDados(servidor, banco_dados)
page.conectar_banco_dados()

dados_vendas = page.buscar_dados_vendas()

diretorio = "planilha_dados"

if not os.path.exists(diretorio):
    os.makedirs(diretorio)

page.salvar_em_excel(dados_vendas, "planilha_dados\saida.xlsx")



page.fechar_conexao()
