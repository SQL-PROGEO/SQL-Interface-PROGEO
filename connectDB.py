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
    pw = "soltec"

    connection = oracledb.connect(
        user="ELETROMAPA",
        password=pw,
        dsn="10.1.1.217:1521/SDEMP")

    cursor = connection.cursor()
    return connection, cursor

def conectar_PA():
    pw = "soltec"

    connection = oracledb.connect(
        user="ELETROMAPA",
        password=pw,
        dsn="10.130.3.17:1521/SDEMP")

    cursor = connection.cursor()
    return connection, cursor

def conectar_PI():
    pw = "soltec"

    connection = oracledb.connect(
        user="ELETROMAPA",
        password=pw,
        dsn="10.6.15.220:1521/SDEMP")

    cursor = connection.cursor()
    return connection, cursor

def conectar_AL():
    pw = "soltec"

    connection = oracledb.connect(
        user="ELETROMAPA",
        password=pw,
        dsn="10.6.11.11:1521/engpr")

    cursor = connection.cursor()
    return connection, cursor