from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TicketBase(BaseModel):
    event_name: str
    description: str
    venue: str
    event_date: datetime
    price: float
    max_supply: int
    image_url: Optional[str] = None

class TicketCreate(TicketBase):
    organizer_address: str

class TicketDB(TicketBase):
    id: int
    asset_id: Optional[int] = None
    ipfs_hash: Optional[str] = None
    created_at: datetime
    
    class Config:
        orm_mode = True

class TicketResponse(TicketDB):
    pass