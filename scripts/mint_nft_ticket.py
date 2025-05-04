
from algosdk.v2client import algod
from algosdk.transaction import AssetConfigTxn
from algosdk import account, mnemonic

# Algorand setup
algod_address = "https://testnet-api.algonode.cloud"
algod_token = ""
client = algod.AlgodClient(algod_token, algod_address)

creator_mnemonic = "your 25-word mnemonic goes here"
creator_private_key = mnemonic.to_private_key(creator_mnemonic)
creator_address = mnemonic.to_public_key(creator_mnemonic)

# Transaction params
params = client.suggested_params()
txn = AssetConfigTxn(
    sender=creator_address,
    sp=params,
    total=1,
    default_frozen=False,
    unit_name="VIP23",
    asset_name="DecentraFest 2025 VIP Ticket",
    manager=creator_address,
    reserve=creator_address,
    freeze=None,
    clawback=None,
    url="ipfs://your-ipfs-cid",
    decimals=0
)

# Sign and send
signed_txn = txn.sign(creator_private_key)
txid = client.send_transaction(signed_txn)
print("✅ Transaction ID:", txid)
