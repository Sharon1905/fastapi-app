from fastapi import APIRouter
from database import db

router = APIRouter()

@router.get("/admin/stats")
async def get_admin_stats():
    player_count = await db["users"].count_documents({"user_type": "player"})
    org_count = await db["users"].count_documents({"user_type": "org"})
    gig_count = await db["gigs"].count_documents({})
    application_count = await db["applications"].count_documents({})
    endorsement_count = await db["endorsements"].count_documents({})
    nft_count = await db["soulbound_nfts"].count_documents({})

    return {
        "total_players": player_count,
        "total_organizations": org_count,
        "total_gigs": gig_count,
        "total_applications": application_count,
        "total_endorsements": endorsement_count,
        "nfts_minted": nft_count
    }

@router.get("/admin/users")
async def get_all_users():
    users = []
    cursor = db["users"].find()
    async for user in cursor:
        user["_id"] = str(user["_id"])
        users.append(user)
    return {"total": len(users), "users": users}

@router.get("/admin/endorsements")
async def get_all_endorsements():
    endorsements = []
    cursor = db["endorsements"].find()
    async for e in cursor:
        e["_id"] = str(e["_id"])
        endorsements.append(e)
    return {"total": len(endorsements), "endorsements": endorsements}

@router.get("/admin/nfts")
async def get_all_nfts():
    nfts = []
    cursor = db["soulbound_nfts"].find()
    async for nft in cursor:
        nft["_id"] = str(nft["_id"])
        nfts.append(nft)
    return {"total": len(nfts), "nfts": nfts}
