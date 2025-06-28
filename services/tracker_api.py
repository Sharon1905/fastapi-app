import httpx

async def fetch_dota2_stats(steam32_id: str):
    url = f"https://api.opendota.com/api/players/{steam32_id}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code != 200:
                print("OpenDota API error:", response.status_code)
                return None
            return response.json()
    except Exception as e:
        print("Exception fetching from OpenDota:", e)
        return None
