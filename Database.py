import mysql.connector

class Database:
    def __init__(self):
        # Conecta ao banco de dados MySQL com as credenciais fornecidas
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "kaiomazza_db"
        )
        self.cursor = self.conn.cursor() # Cria um cursor para executar comandos mysql
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuario1(
                idusuario INT AUTO_INCREMENT PRIMARY KEY,
                nome TEXT(225),
                email TEXT(225),
                usuario TEXT(225),
                senha TEXT(225)
            );""")
        self.conn.commit() # Confirma a criacao da tabela

        print("conectado ao banco de dados") # Mensagem de confirmacao
    
    # Metodo para registrar um novo usuario no banco de dados
    def RegistrarNoBanco(self, nome, email, usuario, senha):
        self.cursor.execute("INSERT INTO usuario1 (nome, email, usuario, senha)VALUES(%s, %s, %s, %s)", (nome, email, usuario, senha)) # Insere os dados na tabela 
        self.conn.commit() # Confirma o processo
    
    # Metodo para alterar usuario no banco de dados
    def alterar(self, idusuario, nome, email, usuario, senha):
        self.cursor.execute("UPDATE usuario1 SET nome = %, email = %, usuario = %, senha = % WHERE idusuario = %s", (nome, email, usuario, senha, idusuario)) # Insere os dados na tabela 
        self.conn.commit() # Confirma o processo
    
    # Metodo para excluir usuario do banco de dados
    def excluir(self, idusuario):
        self.cursor.execute("DELETE FROM usuario1 WHERE idusuario = %s", (idusuario)) # Exclui o usuario conforme o id passado
        self.conn.commit() # Confirma o processo
    
    # Metodo para buscar usuario no banco de dados
    def buscar(self, idusuario):
        self.cursor.execute("SELECT * FROM usuario1 WHERE idusuario = %s", (idusuario,)) # Seleciona os dados do usuario conforme o id
        return self.conn.fetchone() # Retorna os dados do usuario

    # Metodo chamado quando a instancia da classe é destruida
    def __del__(self):
        self.conn.close() # Feha a conexao com o banco