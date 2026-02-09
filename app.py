
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TripRequest(BaseModel):
    prompt: str

@app.post("/plan-trip")
def plan_trip(req: TripRequest):
    return {
        "itinerary": [
            {"day": 1, "activity": "City sightseeing", "cost": 2000},
            {"day": 2, "activity": "Local experiences", "cost": 2500},
            {"day": 3, "activity": "Relaxation & shopping", "cost": 1500}
        ],
        "total_cost": 6000
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
