import mysql.connector
from mysql.connector.constants import ClientFlag
import os

config = {
    'user': 'admin',
    'password': 's1a2n3y4a5',
    'host': '35.192.218.150',
    'database': 'rzfm_app',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': '/app/src/database/ssl/server-ca.pem',
    'ssl_cert': '/app/src/database/ssl/client-cert.pem',
    'ssl_key': '/app/src/database/ssl/client-key.pem'
}

class SQLConnector:
    def __init__(self):
        cwd = os.getcwd()
        self.cnxn = mysql.connector.connect(**config)
        self.cursor = self.cnxn.cursor()


    def execute_query(self, command):
        self.cursor.execute(command)
        return self.cursor


    def execute_insert_update(self, command):
        self.cursor.execute(command)
        self.cnxn.commit()
        return self.cursor