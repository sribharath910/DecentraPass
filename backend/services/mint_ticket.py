from algosdk.future.transaction import AssetConfigTxn
from utils.algo_client import AlgorandClient
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class NFTMinter:
    def __init__(self):
        self.algo_client = AlgorandClient()
        self.pinata_api_key = os.getenv("PINATA_API_KEY")
        self.pinata_secret_key = os.getenv("PINATA_SECRET_KEY")

    async def upload_to_ipfs(self, metadata):
        url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
        headers = {
            "pinata_api_key": self.pinata_api_key,
            "pinata_secret_api_key": self.pinata_secret_key,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(url, json=metadata, headers=headers)
            if response.status_code == 200:
                return response.json()["IpfsHash"]
            return None
        except Exception as e:
            print(f"Error uploading to IPFS: {str(e)}")
            return None

    async def mint_nft_ticket(self, creator_private_key, ticket_data):
        try:
            # Upload metadata to IPFS
            metadata = {
                "name": ticket_data.event_name,
                "description": ticket_data.description,
                "image": ticket_data.image_url,
                "properties": {
                    "venue": ticket_data.venue,
                    "event_date": ticket_data.event_date.isoformat(),
                    "price": str(ticket_data.price)
                }
            }
            
            ipfs_hash = await self.upload_to_ipfs(metadata)
            if not ipfs_hash:
                raise Exception("Failed to upload metadata to IPFS")

            client = self.algo_client.get_client()
            params = client.suggested_params()
            
            # Create NFT
            txn = AssetConfigTxn(
                sender=ticket_data.organizer_address,
                sp=params,
                total=ticket_data.max_supply,
                default_frozen=False,
                unit_name="TICKET",
                asset_name=f"{ticket_data.event_name}_TICKET",
                manager=ticket_data.organizer_address,
                reserve=ticket_data.organizer_address,
                freeze=ticket_data.organizer_address,
                clawback=ticket_data.organizer_address,
                url=f"ipfs://{ipfs_hash}",
                decimals=0
            )

            # Sign transaction
            signed_txn = txn.sign(creator_private_key)
            
            # Submit transaction
            tx_id = client.send_transaction(signed_txn)
            
            # Wait for confirmation
            try:
                confirmed_txn = client.wait_for_confirmation(tx_id, 4)
                asset_id = confirmed_txn["asset-index"]
                return asset_id, ipfs_hash
            except Exception as e:
                print(f"Error waiting for confirmation: {str(e)}")
                return None, None

        except Exception as e:
            print(f"Error minting NFT: {str(e)}")
            return None, None