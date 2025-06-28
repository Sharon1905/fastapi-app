from fastapi import FastAPI
from dotenv import load_dotenv
import users, gigs, applications, endorsements, nft, stat_verification, connect_stats, admin

load_dotenv()
app = FastAPI()

# Routers
app.include_router(users.router)
app.include_router(gigs.router)
app.include_router(applications.router)
app.include_router(endorsements.router)
app.include_router(nft.router)
app.include_router(stat_verification.router)
app.include_router(connect_stats.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "SkillLink Backend Running"}