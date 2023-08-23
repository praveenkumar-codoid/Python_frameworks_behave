import unittest
import requests


class APITestCase(unittest.TestCase):
    BASE_URL = "http://gorest.co.in"
    auth_token = "0eebbd3dd679aa7badfde5c41e5be11660a8227688ec50280a23a52398e7546c"

    def test_create_user(self):
        new_user_data = {
            "name": "Giri Abbott",
            "email": "giri_abbott123@oberbrunner.example",
            "gender": "male",
            "status": "inactive"
        }

        response = requests.post(f"{self.BASE_URL}/users", json=new_user_data)

        self.assertEqual(response.status_code, 201, "Expected status code 201")
        created_user_data = response.json()
        print(created_user_data)

        self.assertEqual(created_user_data["name"], new_user_data["name"], "Name mismatch")
        self.assertEqual(created_user_data["username"], new_user_data["username"], "Username mismatch")
        self.assertEqual(created_user_data["email"], new_user_data["email"], "Email mismatch")


if __name__ == "__main__":
    unittest.main()
