import os
import time

from pyhive import hive
from locust import User


class HiveUser(User):
    abstract = True

    def __init__(self, environment):
        super().__init__(environment)
        host = os.getenv("LOCUST_HIVE_HOST")
        username = os.getenv("LOCUST_HIVE_USERNAME")
        database = os.getenv("LOCUST_HIVE_DATABASE")
        print("Abrindo conexao")
        self.client = hive.connect(host=host, username=username, database=database)
        print("Conexao ok")

    def on_stop(self):
        self.client.close()


    def execute(self, query):
        print("Execute query")
        cursor = self.client.cursor()
        cursor.execute(query)
        cursor.close()
