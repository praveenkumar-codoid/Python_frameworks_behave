import requests
import unittest


class APITestCase(unittest.TestCase):

    def test_delete(self):
        url = "https://reqres.in/api/users?2"

        self.response = requests.delete(url)

        print( self.response.status_code)
        self.assertEqual(self.response.status_code, 204)
        # assert self.response.status_code == 200



if __name__ == "__main__":
    unittest.main()


