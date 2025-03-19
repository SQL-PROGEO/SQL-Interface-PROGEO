import getpass
import oracledb
import os
import sys

#oracle_client_path = "\\oracle\\instantclient_19_26"
#oracledb.init_oracle_client(lib_dir = oracle_client_path)

base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
oracle_client_path = os.path.join(base_path, "oracle", "instantclient_19_26")
oracledb.init_oracle_client(lib_dir=oracle_client_path)

def conectar_MA():

    return connection, cursor

def conectar_PA():

    cursor = connection.cursor()
    return connection, cursor

def conectar_PI():

    cursor = connection.cursor()
    return connection, cursor

def conectar_AL():

    cursor = connection.cursor()
    return connection, cursor
