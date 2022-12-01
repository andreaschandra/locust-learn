import random
from locust import HttpUser, task, tag


class HelloWorldUser(HttpUser):

    @tag('general')
    @task
    def homepage(self):
        self.client.get("/")

    @tag('general')
    @task
    def createuser(self):
        self.client.get("/createuser")

    @tag('general')
    @task
    def createuser_json(self):
        self.client.post(
            "/createuserjson", json={"fullname": "John Doe", "gender": "Male"}
        )

    @tag('model')
    @task
    def predict(self):

        reviews = [
            'Perbanyak lagi item penjualannya, soale masih kalah jauh dengan olshop tetangga',
            'sebenarnya sangat mudah pengoperasiannya, tp untuk pemula mungkin agak bingung',
            'kerjasama promo dgn vendornya lbh variatif lagi dong, intip2 ecommerce sebelah',
            'ok bgt.. gratis ongkir.. cuma barang blm begitu banyak, blom begitu bervariasi',
            'aplikasi shoping trhancur yng pernah sya install... verifikasi hp bloon banget'
        ]

        self.client.post(
            "/predict", json={"review": random.choice(reviews)}
        )
