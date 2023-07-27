from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# importando Pil
from PIL import ImageTk, Image

# importando string
import string
import random


# Cores
cor0 = "#444466"  # Cor preta/black
cor1 = "#feffff"  # Cor branca/white
cor2 = "#f05a43"  # Cor vermelha/red
cor3 = "#008080"  # Cor Azul/blue

# Dimensoes da janela
janela = Tk()
janela.title('')
janela.geometry('295x350')
janela.configure(bg=cor1)

# Thema da janela
estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Tela Dividida
# Frame: Parte de Cima
frame_cima = Frame(janela, width=295, height=60, bg=cor1,
                   pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

# Frame parte de baixo
frame_baixo = Frame(janela, width=295, height=310,
                    bg=cor1, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Imagem
img = Image.open('img_01.png')
img = img.resize((35, 35), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

# Pocisionamento da imagem
app_logo = Label(frame_cima, height=60, image=img,
                 compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor1)
app_logo.place(x=2, y=0)

# logica de gerar senha


def criar_senha():
    alfa_maior = string.ascii_uppercase
    alfa_menor = string.ascii_lowercase
    numeros = '123456789'
    simbolos = "[]{}()@#$%&<>-_"

    global combinar

    # Condicao para maiuscula
    if estado_1.get() == alfa_maior:
        combinar = alfa_maior
    else:
        pass

    # Condicao para minuscula
    if estado_2.get() == alfa_menor:
        combinar = combinar + alfa_menor
    else:
        pass

    # Condicao para numero
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass

    # Condicao para simbolus
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass

    comprimento = int(spin.get())

    senha = "".join(random.sample(combinar, comprimento))

    app_senha['text'] = senha

    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo("Copiado!", " A senha foi copiada com sucesso!")

    # Botao Copiar

    botao_gerar_senha = Button(frame_baixo, command=copiar_senha, text='copiar', width=7, height=1, relief='raised',
                               overrelief='solid', anchor='center', font=('Ivy 10 bold'), bg=cor3, fg=cor1)
    botao_gerar_senha.grid(row=0, column=0,
                           sticky=NW, padx=5, pady=10, columnspan=1)
    botao_gerar_senha.place(x=200, y=0)


# nome do gerador de senhas
app_nome = Label(frame_cima, text='Gerador de Senhas', width=24, height=1,
                 padx=0, relief='flat', anchor='nw', font=('Ivy 16 bold'), bg=cor1, fg=cor0)
app_nome.place(x=40, y=10)

# Divisoria
app_linha = Label(frame_cima, text='', width=295, height=1,
                  padx=0, relief='flat', anchor='nw', font=('Ivy 1'), bg=cor3, fg=cor0)
app_linha.place(x=0, y=45)

# Frame: Parte de Baixo

# Parte de Gereciamento da senha
app_senha = Label(frame_baixo, text='- - -', width=16, height=2,
                  padx=0, relief='solid', anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_senha.grid(row=0, column=0, columnspan=1,
               sticky=NSEW, padx=5, pady=0)
app_senha.config(width=10)

# Informacao mostrada na janela
app_info = Label(frame_baixo, text='Numero total de caracteres na senha', height=2,
                 padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=5)


var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=1, to=24, width=5, textvariable=var)
spin.grid(row=2, column=2, columnspan=2, sticky=NW, padx=5, pady=0)
spin.place(x=5, y=62)

# caracteres
alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = "[]{}()@#$%&<>-_"

# Parte dos caracteres
frame_caracteres = Frame(frame_baixo, width=295, height=210, bg=cor1,
                         pady=10, padx=0, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

# Letras Maiusculas
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1,
                      onvalue=alfa_maior, offvalue='menor', relief='flat', bg=cor1)
check_1.grid(row=0, column=0, columnspan=2, sticky=NW, padx=2, pady=8)
check_1.place(x=5, y=10)
app_caracteres = Label(frame_caracteres, text='Letras maiusculas', height=1,
                       padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_caracteres.grid(row=0, column=1, sticky=NW, padx=2, pady=5)
app_caracteres.place(x=43, y=12)

# Letras minusculas
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2,
                      onvalue=alfa_menor, offvalue='menor', relief='flat', bg=cor1)
check_2.grid(row=1, column=0, columnspan=2, sticky=NW, padx=2, pady=8)
check_2.place(x=5, y=35)
app_caracteres = Label(frame_caracteres, text='Letras minusculas', height=1,
                       padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_caracteres.grid(row=1, column=1, sticky=NW, padx=2, pady=5)
app_caracteres.place(x=43, y=37)

# Letras Numeros
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3,
                      onvalue=numeros, offvalue='menor', relief='flat', bg=cor1)
check_3.grid(row=2, column=0, columnspan=2, sticky=NW, padx=2, pady=8)
check_3.place(x=5, y=60)
app_caracteres = Label(frame_caracteres, text='Numeros', height=1,
                       padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_caracteres.grid(row=2, column=1, sticky=NW, padx=2, pady=5)
app_caracteres.place(x=43, y=62)

# Letras Simbulos
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width=1, var=estado_4,
                      onvalue=simbolos, offvalue='menor', relief='flat', bg=cor1)
check_4.grid(row=3, column=0, columnspan=2, sticky=NW, padx=2, pady=8)
check_4.place(x=5, y=85)
app_caracteres = Label(frame_caracteres, text='Simbolos', height=1,
                       padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_caracteres.grid(row=3, column=1, sticky=NW, padx=2, pady=5)
app_caracteres.place(x=43, y=87)

# Botao do Pedro

botao_gerar_senha = Button(frame_caracteres, text='GERAR SENHA', width=32, height=2, relief='raised',
                           overrelief='solid', command=criar_senha, anchor='center', font=('Ivy 10 bold'), bg=cor3, fg=cor1)
botao_gerar_senha.grid(row=0, column=0,
                       sticky=NSEW, padx=1, pady=0, columnspan=5)
botao_gerar_senha.place(x=-15, y=140)


# Loop da janela
janela.mainloop()
