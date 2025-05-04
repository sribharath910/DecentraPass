
# Simulates ticket validation at entry using wallet address match

def validate_ticket(owner_wallet_address, scanned_ticket_owner):
    if owner_wallet_address == scanned_ticket_owner:
        print("✅ Access Granted: Valid NFT Ticket")
    else:
        print("❌ Access Denied: Ticket does not belong to this user")

# Example usage
validate_ticket("YOUR_WALLET", "YOUR_WALLET")
