from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user
from bson import ObjectId
from database import db

router = APIRouter()

@router.post("/connect-stats")
async def connect_stats(data: dict, current_user: dict = Depends(get_current_user)):
    game = data.get("game", "").lower()
    external_id = data.get("id")

    if not game or not external_id:
        raise HTTPException(status_code=400, detail="Game and ID required.")

    # Check if user exists
    user = await db["users"].find_one({"_id": ObjectId(current_user["id"])})
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    # Normalize & update external_ids
    external_ids = user.get("external_ids") or {}
    external_ids[game] = external_id

    await db["users"].update_one(
        {"_id": ObjectId(current_user["id"])},
        {"$set": {"external_ids": external_ids}}
    )

    return {"message": f"{game.capitalize()} ID linked successfully."}
