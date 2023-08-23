import unittest

import requests
import json
import jsonpath


class APITestCase(unittest.TestCase):

    def test_put(self):
        self.URL = "https://reqres.in/api/users/2"
        file = open("C:\\Users\\codoid\\Desktop\\createuser.json", "r")
        self.json_input = file.read()
        self.request_json = json.loads(self.json_input)
        self.response = requests.put(self.URL, self.request_json)
        assert self.response.status_code == 200
        self.response_json = json.loads(self.response.text)
        updated_li = jsonpath.jsonpath(self.response_json, "updatedAt")
        print(updated_li[0])


if __name__ == "__main__":
    unittest.main()
