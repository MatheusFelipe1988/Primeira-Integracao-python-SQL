from ast import If
from optparse import Values
from sqlite3 import Cursor
import sqlite3
import mysql.connector
import getpass
from mysql.connector import (connection)

pip1_connection = connection.MySQLConnection(host='localhost', user='root', password='senha', database='pip1')
#senha = getpass.getpass('Digite a senha: ')


if pip1_connection.is_connected():
    pip1 = pip1_connection.get_server_info()
    print("Conectado ao servidor MySQL versão ",pip1)
    cursor = pip1_connection.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)

if pip1_connection.is_connected():
    cursor.close()
    pip1_connection.close()
    print("Conexão ao MySQL foi encerrada")