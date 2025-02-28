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
UsuarioLabel = Label(RightFrame, text="Usuario:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white") # Cria um label para o usuario
UsuarioLabel.place(x=5, y=100) # Posiciona o label o frame direito
UsuarioEntry = ttk.Entry(RightFrame, width=30) # Cria um campo de entrada para o usuario