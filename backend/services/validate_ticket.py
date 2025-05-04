from utils.algo_client import AlgorandClient
import json

class TicketValidator:
    def __init__(self):
        self.algo_client = AlgorandClient()

    async def validate_ticket(self, asset_id: int, holder_address: str):
        try:
            client = self.algo_client.get_client()
            
            # Get asset info
            asset_info = client.asset_info(asset_id)
            
            # Get account info
            account_info = client.account_info(holder_address)
            
            # Check if account holds the asset
            assets_held = account_info.get("assets", [])
            for asset in assets_held:
                if asset["asset-id"] == asset_id and asset["amount"] > 0:
                    return {
                        "valid": True,
                        "asset_info": asset_info,
                        "balance": asset["amount"]
                    }
            
            return {
                "valid": False,
                "message": "Address does not hold the ticket NFT"
            }

        except Exception as e:
            return {
                "valid": False,
                "message": f"Error validating ticket: {str(e)}"
            }

    async def get_ticket_metadata(self, asset_id: int):
        try:
            client = self.algo_client.get_client()
            asset_info = client.asset_info(asset_id)
            
            # Extract IPFS hash from asset URL
            ipfs_url = asset_info["params"].get("url", "")
            if ipfs_url.startswith("ipfs://"):
                ipfs_hash = ipfs_url.replace("ipfs://", "")
                return {
                    "success": True,
                    "ipfs_hash": ipfs_hash,
                    "asset_info": asset_info
                }
            
            return {
                "success": False,
                "message": "Invalid asset URL format"
            }

        except Exception as e:
            return {
                "success": False,
                "message": f"Error fetching ticket metadata: {str(e)}"
            }