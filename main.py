from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import uvicorn
import time

app = FastAPI(title="Zyra API", description="Backend for Zyra Branding Automation")

# Allow CORS so the frontend can talk to us
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class BrandRequest(BaseModel):
    industry: str
    vibe: str = "Modern"

# Routes
@app.get("/")
def read_root():
    print("Hit root endpoint")
    return {"message": "Welcome to Zyra API. Status: Online"}

@app.post("/api/generate-name")
def generate_name(req: BrandRequest):
    print(f"Generating name for: {req.industry}, Vibe: {req.vibe}")
    # Simulation logic
    prefixes = ["Nova", "Lumina", "Apex", "Zenith", "Flux", "Velvet", "Aura", "Prisma"]
    suffixes = ["Works", "Labs", "Flow", "Sphere", "Mind", "Pulse", "Gen", "X"]
    
    # Generate 4 random names
    names = []
    for _ in range(4):
        p = random.choice(prefixes)
        s = random.choice(suffixes)
        names.append(f"{p}{s}")
    time.sleep(1) # Simulate think time
    return {"names": names}

@app.post("/api/generate-logo")
def generate_logo(req: BrandRequest):
    print(f"Generating logo for: {req.industry}")
    # Return a placeholder that looks good
    colors = ["7C3AED", "DB2777", "0EA5E9", "10B981"]
    color = random.choice(colors)
    # Using a reliable placeholder service
    return {"url": f"https://placehold.co/400x400/{color}/FFFFFF?text={req.industry}+Logo"}

@app.post("/api/content")
def generate_content(req: BrandRequest):
    print("Generating content")
    time.sleep(1.5)
    return {
        "tagline": f"Redefining {req.industry} with {req.vibe} innovation.",
        "social_post": f"Excited to unveil our new {req.vibe} approach to {req.industry}! #FutureReady"
    }

@app.get("/api/ethics-check")
def ethics_check(text: str = "Brand Content"):
    print("Checking ethics")
    return {
        "score": 98, 
        "status": "Pass", 
        "message": "No inclusivity issues detected."
    }

if __name__ == "__main__":
    print("Zyra Backend Starting...")
    print("Usage: 1. Ensure 'pip install fastapi uvicorn' is run.")
    print("       2. Keep this window open.")
    print("       3. Open brand.html in your browser.")
    # Run on 8000 matching the frontend URL
    # host="0.0.0.0" can help if localhost issues arise on some configs, but 127.0.0.1 is standard.
    uvicorn.run(app, host="127.0.0.1", port=8000)
