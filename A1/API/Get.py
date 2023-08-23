import unittest
import requests


class APITestCase(unittest.TestCase):
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def test_get_user(self):
        user_id = 1
        response = requests.get(f"{self.BASE_URL}/users/{user_id}")
        json_data = response.json()
        print(json_data)
        print(response)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        user_data = response.json()

    def test_get_nonexistent_user(self):
        user_id = 1000
        response = requests.get(f"{self.BASE_URL}/users/{user_id}")
        json_data = response.json()
        print(json_data)
        print(response)

        self.assertEqual(response.status_code, 404, "Expected status code 404")


if __name__ == "__main__":
    unittest.main()
