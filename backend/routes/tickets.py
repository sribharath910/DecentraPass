from fastapi import APIRouter, HTTPException, Depends
from models.ticket import TicketCreate, TicketResponse
from services.mint_ticket import NFTMinter
from services.validate_ticket import TicketValidator
from typing import List, Optional
import os

router = APIRouter()
nft_minter = NFTMinter()
ticket_validator = TicketValidator()

@router.post("/tickets/mint", response_model=dict)
async def mint_ticket(ticket: TicketCreate):
    creator_mnemonic = os.getenv("CREATOR_MNEMONIC")
    if not creator_mnemonic:
        raise HTTPException(status_code=500, message="Creator mnemonic not configured")
    
    try:
        # Convert mnemonic to private key
        from algosdk import mnemonic
        creator_private_key = mnemonic.to_private_key(creator_mnemonic)
        
        # Mint NFT ticket
        asset_id, ipfs_hash = await nft_minter.mint_nft_ticket(creator_private_key, ticket)
        
        if not asset_id:
            raise HTTPException(status_code=500, detail="Failed to mint NFT ticket")
        
        return {
            "success": True,
            "asset_id": asset_id,
            "ipfs_hash": ipfs_hash
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/tickets/validate/{asset_id}")
async def validate_ticket(asset_id: int, holder_address: str):
    result = await ticket_validator.validate_ticket(asset_id, holder_address)
    if not result["valid"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@router.get("/tickets/{asset_id}/metadata")
async def get_ticket_metadata(asset_id: int):
    result = await ticket_validator.get_ticket_metadata(asset_id)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result