from app import app
import unittest


class AppIndexTest(unittest.TestCase):
    def test_index_get(self):
        """Testing display index page"""
        client = app.test_client(self)
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_index_content(self):
        client = app.test_client(self)
        response = client.get("/")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")


class AppGetCityTest(unittest.TestCase):
    def test_invalid_city(self):
        client = app.test_client(self)
        response = client.get("/city/?title=zealkhjrb")
        assert b"No matching found" in response.data
        self.assertEqual(response.status_code, 200)

    def test_valid_city(self):
        client = app.test_client(self)
        response = client.get("/city/?title=paris")
        assert b"Paris" in response.data
        self.assertEqual(response.status_code, 200)

    def test_error_route_city(self):
        client = app.test_client(self)
        response = client.get("/citi/?title=paris")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        assert b"not found" in response.data


class AppSendTest(unittest.TestCase):
    def test_send_datas(self):
        client = app.test_client(self)
        response = client.post(
            "/send/",
            data={
                "id": 3,
                "title": "Marseille",
                "address": "5 rue Reno",
                "zip": "13001",
                "service": "hebergement",
                "client": "id684",
            },
        )
        self.assertEqual(response.status_code, 200)
        assert b"sent" in response.data


if __name__ == "__main__":
    unittest.main()
