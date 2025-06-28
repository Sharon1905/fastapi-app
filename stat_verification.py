from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user
from bson import ObjectId
from database import db
from services.tracker_api import fetch_dota2_stats

router = APIRouter()

@router.post("/verify-stats")
async def verify_stats(data: dict, current_user: dict = Depends(get_current_user)):
    game = data.get("game", "").lower()
    claimed_stats = data.get("claimed_stats")

    if not game or not claimed_stats:
        raise HTTPException(status_code=400, detail="Game and claimed_stats are required.")

    # ✅ Get full user from DB
    user = await db["users"].find_one({"_id": ObjectId(current_user["id"])})
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    external_ids = user.get("external_ids") or {}
    external_ids = {k.lower(): v for k, v in external_ids.items()}
    game_id = external_ids.get(game)

    if not game_id:
        raise HTTPException(status_code=400, detail=f"No external ID found for game '{game}' in profile.")

    # 🧪 Simulated stat fetch
    if game == "valorant":
        actual_stats = {
            "rank": "Ancient 2",
            "kd": 2.05
        }
    
    elif game == "dota2":
        raw_stats = await fetch_dota2_stats(game_id)
        if not raw_stats:
            raise HTTPException(status_code=404, detail="Failed to fetch stats from OpenDota")

        actual_stats = {
            "rank": str(raw_stats.get("rank_tier", "Unknown")),
            "kd": round(raw_stats.get("kda", 0), 2)
        }
    else:
        raise HTTPException(status_code=400, detail="Unsupported game.")

    # 📊 Compare claimed vs actual
    differences = {}
    for key, claimed_value in claimed_stats.items():
        actual_value = actual_stats.get(key)
        if actual_value != claimed_value:
            differences[key] = {
                "claimed": claimed_value,
                "actual": actual_value
            }

    verified = len(differences) == 0

    # ✅ If verified, mark user in DB
    if verified:
        await db["users"].update_one(
            {"_id": ObjectId(current_user["id"])},
            {"$set": {"is_verified": True}}
        )

    return {
        "verified": verified,
        "differences": differences
    }
