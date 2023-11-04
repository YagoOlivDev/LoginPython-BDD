import mysql.connector as msql
from tkinter import *

#Está é a conexão com o banco de dados MySQL.
conexao = msql.connect(
    host='localhost',
    user='root',
    password='Yago1234',
    database= 'pessoas',
    port='3306'
)

cursor = conexao.cursor()
consulta_sql = 'select * from usuarios'
#cursor.execute(consulta_sql)

#cursor.execute("Create table usuarios (cpf varchar (11) primary key, nome varchar(20), senha varchar (12))")
