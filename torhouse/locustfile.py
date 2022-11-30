from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def homepage(self):
        self.client.get("/")

    @task
    def createuser(self):
        self.client.get("/createuser")

    @task
    def createuser_json(self):
        self.client.post(
            "/createuserjson", json={"fullname": "John Doe", "gender": "Male"}
        )
