
import requests
import json

API_KEY = "YOUR_NFT_STORAGE_API_KEY"
headers = {
    "Authorization": f"Bearer {API_KEY}",
}

metadata = {
    "name": "DecentraFest 2025 VIP Ticket",
    "description": "VIP pass to DecentraFest 2025 with backstage access and perks",
    "image": "ipfs://your-image-cid",
    "attributes": [
        {"trait_type": "Event", "value": "DecentraFest 2025"},
        {"trait_type": "Seat", "value": "VIP-23"},
        {"trait_type": "Access", "value": "Backstage + Merch Drop"},
        {"trait_type": "Date", "value": "2025-06-20"}
    ]
}

files = {
    'file': ('ticket_metadata.json', json.dumps(metadata))
}

response = requests.post(
    'https://api.nft.storage/upload',
    headers=headers,
    files=files
)

print("✅ IPFS CID:", response.json()['value']['cid'])
