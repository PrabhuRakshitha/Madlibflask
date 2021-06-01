import unittest
from madlib import app

class testClass(unittest.TestCase):
    app = app.test_client()
    def test_madlib_response(self):

        response =self.runmadlib()
        self.assertEqual(response.status_code, 200)

    def test_madlib_random(self):
        result = set()
        for i in range(5):
            response = self.runmadlib()
            result.add(response)

        self.assertEqual(len(result),5)

    def runmadlib(self):
         return self.app.get("/madlib/")

if __name__ == "__main__":
    unittest.main()
