from locust_plugins import run_single_user
from locust_plugins.hive import HiveUser
from locust import task


class MyUser(HiveUser):

    @task
    def t(self):
        self.execute("show databases")


if __name__ == "__main__":
    print("run")
    run_single_user(MyUser)
