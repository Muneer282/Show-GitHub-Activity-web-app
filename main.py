from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# للسماح للفرونت بالتواصل مع الباك
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/github/{username}")
async def get_github_user(username: str):
    url = f"https://api.github.com/users/{username}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        return {"error": "User not found"}

    data = response.json()

    return {
        "username": data.get("login"),
        "name": data.get("name"),
        "avatar": data.get("avatar_url"),
        "bio": data.get("bio"),
        "repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "profile_url": data.get("html_url")
    }
