import random
from locust import HttpUser, task, between

class MLOpsLoadTester(HttpUser):
    wait_time = between(0.1, 0.5)

    @task
    def mock_prediction_request(self):
        payload = {
            "sqft": float(random.randint(800, 5000)),
            "rooms": int(random.randint(1, 6))
        }
        self.client.post("/predict", json=payload)
