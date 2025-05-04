# 🎟️ Community-Owned NFT Ticketing System – A Decentralized NFT Marketplace

A blockchain-based decentralized ticketing platform where event organizers, artists, and communities can mint, sell, and manage event tickets as NFTs on the Algorand blockchain.  
The system prevents ticket fraud, scalping, and enables fair revenue sharing through community governance.

---

## 🚀 Key Features

- **NFT Ticket Minting**: Organizers create verifiable NFT-based tickets.
- **Secure Marketplace**: Buy, sell, and resell tickets with enforced smart contract rules.
- **Scalping Prevention**: Fair resale pricing and royalty sharing with event creators.
- **Community Governance (DAO)**: Vote on pricing strategies, resale policies, and event rules.
- **Unlockable Perks**: NFT ticket holders get VIP access, merchandise discounts, and more!

---

## 🛠 Tech Stack

- **Blockchain**: Algorand Smart Contracts (ASC1) with ASA-based NFTs
- **Smart Contracts**: PyTeal (Python) / AlgoKit (TypeScript)
- **Frontend**: React.js / Next.js
- **Backend**: Flask / FastAPI
- **Storage**: IPFS / Arweave (for ticket metadata)
- **Payments**: Algo-based Atomic Swaps

---

## 📈 How It Works

1. **Event Organizer** mints NFT tickets with event details and rules.
2. **Users** buy and resell tickets through a decentralized marketplace.
3. **Smart Contracts** enforce resale price limits and revenue splits.
4. **Ticket Validation** happens at events via QR code scanning and blockchain verification.
5. **Community Governance** allows users to vote and share profits fairly.

---

## 🌟 Real-World Use Cases

- Concerts, Festivals, and Sports Events
- Conferences and Workshops
- Community-Led Local Events
- Fan Engagement Campaigns

---

## 🚀 Backend Setup & Installation

1. Setup Python virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Start the Algorand Sandbox:
```bash
cd sandbox
./sandbox up
```

4. Start the FastAPI server:
```bash
cd backend
uvicorn main:app --reload
```

The API will be available at http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative Documentation: http://localhost:8000/redoc

## 📡 API Endpoints

### Tickets
- `POST /api/v1/tickets/mint` - Mint new NFT ticket
- `GET /api/v1/tickets/validate/{asset_id}` - Validate ticket ownership
- `GET /api/v1/tickets/{asset_id}/metadata` - Get ticket metadata

---
