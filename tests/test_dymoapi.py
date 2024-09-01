import unittest
from dymoapi.dymoapi import DymoAPI

class TestUrlEncrypt(unittest.TestCase):
    def setUp(self):
        self.config = {
            # "api_key": "PRIVATE_TOKEN_HERE"
        }
        self.client = DymoAPI(self.config)
    
    def test_features(self):
        assert self.client.new_url_encrypt("https://example.com").encrypt.startswith("https://api.tpeoficial.com/public/url-encrypt/")

class TestPasswordValidation(unittest.TestCase):
    def setUp(self):
        self.config = {
            # "api_key": "PRIVATE_TOKEN_HERE"
        }
        self.client = DymoAPI(self.config)
    
    def test_features(self):
        assert self.client.is_valid_pwd({
                "password": "123456",
                "min": 16
            })["valid"] == False, "Password is valid, expected invalid."
        assert self.client.is_valid_pwd({
                "email": "username@test.com",
                "password": "Username123",
            })["valid"] == False, "Password is valid, expected invalid."
        assert self.client.is_valid_pwd({
                "email": "username@test.com",
                "password": "TheMegaPassword_safe512*",
                "min": 16
            })["valid"] == True, "Password is invalid, expected valid."
        assert self.client.is_valid_pwd({
                "email": "username@test.com",
                "password": "TheMegaPassword_safe512*UltraLongPassword",
                "max": 32   
            })["valid"] == False, "Password is valid, expected invalid."
        

class TestInputSatinizer(unittest.TestCase):
    def setUp(self):
        self.config = {
            # "api_key": "PRIVATE_TOKEN_HERE"
        }
        self.client = DymoAPI(self.config)
    
    def test_features(self):
        assert self.client.satinizer({"input": "' OR '1'='1' --"})["includes"]["hasSql"] == True, "Input is not sanitized."
        assert self.client.satinizer({"input": '{"id": {"$eq": 1}}'})["includes"]["hasNoSql"] == True, "Input is not sanitized."
        assert self.client.satinizer({"input": "https://example.com"})["formats"]["url"] == True, "Input is not sanitized."
        assert self.client.satinizer({"input": "192.168.100.1"})["formats"]["ip"] == True, "Input is not sanitized."
if __name__ == "__main__": unittest.main()