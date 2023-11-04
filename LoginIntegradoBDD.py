import customtkinter as Ct
import mysql.connector as msql
from ConectMySQL import *
from tkinter import *
import webbrowser as wb


def inst():
    var = wb.open("https://www.instagram.com/_yg.oliveira/")

def port():
    var = wb.open('https://github.com/YagoOlivDev')

def dln():
    var = wb.open('https://www.linkedin.com/in/yago-de-oliveira-barbosa-12525b259')


def Lerlogin():
    #Função na qual é chamadada quando o usuário aperta o botão "Entrar"
    #essa função, absorve os dados digitados pelo usuário e verifica se
    #são válidos e existentes no banco de dados.
    lb3 = Ct.CTkLabel(janela,
                       text='                                         ')
    lb3.place(x=80, y=270)
    cpf= (ed1.get())
    user= (ed2.get())
    senha= (ed3.get())

    cursor.execute(
    "select cpf from usuarios where nome = '{}' and senha = '{}'"
    .format(user, senha))
    cpfbdd= cursor.fetchall()

    try:        
        if cpf == cpfbdd[0][0]:
            Logado()

        elif cpf != cpfbdd[0][0]:
            lb3 = Ct.CTkLabel(janela, text=
                              '         Dados incorretos!!!', 
                              text_color='red')
        return lb3.place(x=80, y=270)
    
    except IndexError:
        lb3 = Ct.CTkLabel(janela, text='         Dados incorretos!!!',
                          text_color='red')
        return lb3.place(x=80, y=270)
    

def Logado():
    #Função onde é criado a nova janela após os dados de login serem
    #verificados e existirem no banco de dados.
    cursor.close()
    conexao.close()
    novajanela = Ct.CTk()
    novajanela.geometry('320x300')
    novajanela.title('Minha Conta')
    Ct.set_appearance_mode('dark')
    Ct.set_default_color_theme('dark-blue')

    texto = Ct.CTkLabel(novajanela, text='Perfil Profissional')
    texto.pack(padx=12, pady=12)

    btl1 = Ct.CTkButton(novajanela, text='Meu Linkedln', command= dln)
    btl1.pack(padx=12, pady=12)

    btl2 = Ct.CTkButton(novajanela, text='Meu Portfolio', command= port)
    btl2.pack(padx=12, pady=12)

    btl3 = Ct.CTkButton(novajanela, text='Meu Instagram', command= inst)
    btl3.pack(padx=12, pady=12)
 
    janela.destroy()
    novajanela.mainloop()


def LerCadastro():
    #Função na qual é chamada quando o usuário aperta o botão "registrar"
    #Os dados digitados pelo usuário são extraidos e verificados se podem
    #ser válidos para um registramento, se for o usuário é registrado no
    #banco de dados.
    lb3 = Ct.CTkLabel(janela, text=
                      '                                               ')
    lb3.place(x=80, y=270)
    cpf= (ed1.get())
    user= (ed2.get())
    senha= (ed3.get())
    lendonome = len(user)
    lendosenha= len(str(senha))
    lendocpf = len(str(cpf))



    try:
        if lendocpf != 11:
            invalid=  Ct.CTkLabel(janela, text='     ERROR! CPF Inválido.',
                                  text_color='red')
            return invalid.place(x=80, y=270)
        
        if lendonome > 19 or lendonome < 4:
            lb3 = Ct.CTkLabel(janela, text=' Digite seu 1º nome apenas. ',
                              text_color='red')
            return lb3.place(x=80, y=270)

        if lendosenha > 11 or lendosenha < 4:
            lb3 = Ct.CTkLabel(janela, text='    Senha de 4 a 12Digitos.',
                              text_color='red')
            return lb3.place(x=80, y=270)

        if lendocpf == 11:
            sql = "INSERT INTO usuarios (cpf, nome, senha) VALUES (%s, %s, %s)"
            cursor.execute(sql, (cpf, user, senha))
            conexao.commit()
            lb3 = Ct.CTkLabel(janela, text='      Usuário Registrado!!',
                              text_color='green')
            return lb3.place(x=80, y=270)   
        

    except msql.errors.IntegrityError:
        lb3 = Ct.CTkLabel(janela, text='CPF já está cadastrado.',
                          text_color='red')
        cursor.close()
        conexao.close()
        return lb3.place(x=80, y=270, )

    except msql.errors.DatabaseError:
        lb3 = Ct.CTkLabel(janela, text=
                          'Ocorreu algum erro ao registrar.',
                          text_color='red')
        return lb3.place(x=80, y=270, )
        
    
janela = Ct.CTk()

Ct.set_appearance_mode('dark')
Ct.set_default_color_theme('dark-blue')


texto = Ct.CTkLabel(janela, text='Fazer Login')
texto.pack()

ed1 = Ct.CTkEntry(janela, placeholder_text='Digite seu CPF')
ed1.pack(padx=10, pady=10)

ed2 = Ct.CTkEntry(janela, placeholder_text='Digite seu nome')
ed2.pack(padx=10, pady=10)

ed3 = Ct.CTkEntry(janela, placeholder_text='Digite sua senha', show='*')
ed3.pack(padx=10, pady=10)

bt1 = Ct.CTkButton(janela, text='Entrar', width=8, command=Lerlogin)
bt1.pack(padx=10, pady=10)

bt2 = Ct.CTkButton(janela, text='Registrar', width=8, command=LerCadastro)
bt2.pack(padx=10, pady=10)

janela.title('Login')

janela.geometry('320x300')
janela.mainloop()