from algosdk.v2client import algod
from algosdk import account, mnemonic
import os
from dotenv import load_dotenv

load_dotenv()

class AlgorandClient:
    def __init__(self):
        self.algod_address = os.getenv("ALGOD_ADDRESS", "http://localhost:4001")
        self.algod_token = os.getenv("ALGOD_TOKEN", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.client = algod.AlgodClient(self.algod_token, self.algod_address)
    
    def get_client(self):
        return self.client
    
    @staticmethod
    def create_account():
        private_key, address = account.generate_account()
        return {
            "address": address,
            "private_key": private_key,
            "mnemonic": mnemonic.from_private_key(private_key)
        }
    
    def get_account_info(self, address):
        return self.client.account_info(address)
    
    def get_suggested_params(self):
        return self.client.suggested_params()
    
    def get_asset_info(self, asset_id):
        return self.client.asset_info(asset_id)