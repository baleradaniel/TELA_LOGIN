# IMPORTAR AS BIBLIOTECAS
from tkinter import * # Importa todos os módulos do tkinter
from tkinter import messagebox # IMporta o módulo de caixas de mensagens do tkinter
from tkinter import ttk # Importa o módulo de widgets temáticos do tkinter
from DataBase import Database # Importa a classe Database do módulo 'DataBase'

# CRIAR A JANELA
janela = Tk()
janela.title("KM Systems - Painel de Acesso") # Define o titulo da janela
janela.geometry("600x300") # Define o tamanho da janela
janela.configure(background="white") # Configura a cor de fundo da janela
janela.resizable(width=False, height=False) # Impede que a janea seja redimensonada

# COMANDO PARA DEIXA A TELA TRANSPARENTE
janela.attributes("-alpha", 0.9) # Define a transparencia da janela (0.0 a 1.0)

# CARREGAR IMAGEM
logo = PhotoImage(file="icons/kaiomazza.png") # Carrega a imagem da logo

# CRIAR FRAME
LeftFrame = Frame(janela, width=200, height=200, bg="MIDNIGHTBLUE", relief="raise") # Cria um frame à esquerda
LeftFrame.pack(side=LEFT) # Posiciona o frame à esquerda

RightFrame = Frame(janela, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise") # Cria um frame à esquerda
RightFrame.pack(side=RIGHT) # Posiciona o frame à esquerda

# ADICIONAR LOGO
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE") # Cria uma label que carrega a logo
LogoLabel.place(x=50, y=100) # Posiciona o label no frame esquerdo

# ADICIONAR CAMPOS DE USUARIO E SENHA
UsuarioLabel = Label(RightFrame, text="Usuario:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White") # Cria um label para o usuario
UsuarioLabel.place(x=5, y=100) # Posiciona o label o frame direito

UsuarioEntry = ttk.Entry(RightFrame, width=30) # Cria um campo de entrada para o usuario
UsuarioEntry.place(x=120, y=15) # Posiciona o campo de entrada

SenhaLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White") # Cria um label para a senha
SenhaLabel.place(x=5, y=150) # Posiciona o label no frame direito

SenhaEntry = ttk.Entry(RightFrame, width=30, show="*") # Cria um campo de entrada para a senha
SenhaEntry.place(x=120, y=165) # Posiciona o campo de entrada

# FUNCAO DE LOGIN
def Login():
    usuario = UsuarioEntry.get() # Obtem o valor do campo de entrada 'UsuarioEntry'
    senha = SenhaEntry.get() # Obtem o valor do campo de entrada 'SenhaEntry'

    # Conectar ao banco de dados
    db = Database() # Cria uma instancia da classe Database
    db.cursos.execute("""
    SELECT * FROM usuario
    WHERE usuario = %s AND senha = %s""",(usuario, senha)) # execulta a consulta SQL para verificar o usuario e a senha
    VerifyLogin = db.cursor.fetchone() # Obtem o resultado da consulta

    # Verificar se o usuario foi encontrado
    if VerifyLogin:
        messagebox.showinfo(title="INFO LOGIN", message="Acesso Confirmado. Bem Vindo!") # Exibe mensagem de sucesso
    else:
        messagebox.showinfo(title="INFO LOGIN", message="Acesso Negado. Verifique se está cadastrado no Sistema!") # Exibe mensagem de erro

# CRIANDO BOTOES
LoginButton = ttk.Button(RightFrame, text="LOGIN", width=15, command=Login) # Cria um botao de login
LoginButton.place(x=150, y=225) # Posiciona o botao de login

# FUNCAO PARA REGISTRAR NOVO USUARIO
def Registrar():
    # REMOVENDO BOTOES DE LOGIN DA TELA
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    # INSERINDO WIDGETS DE CADASTRO
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5) # Posiciona o label no frame direito

    NomeEntry = ttk.Entry(RightFrame, width=30) # Cria um campo de entrada para o nome
    NomeEntry.place(x=120, y=20)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White") # Cria um label para o email
    EmailLabel.place(x=5, y=40)

    EmailEntry = ttk.Entry(RightFrame, width=30) # Cria um campo de entrada para o email
    EmailEntry.place(x=120, y=55)