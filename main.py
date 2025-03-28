from fastapi import FastAPI, Request
import pandas as pd
import joblib

app = FastAPI()

# Load ML Model (Train separately and save as toy_model.pkl)
model = joblib.load("toy_model.pkl")

@app.post("/webhook")
async def receive_form_data(request: Request):
    data = await request.json()
    print("Received Data:", data)

    # Process data using AI Model
    rotation_plan = generate_toy_rotation_plan(data)

    return {"status": "success", "rotation_plan": rotation_plan}

def generate_toy_rotation_plan(data):
    """AI Model to Generate Rotation Plan"""
    age_group = data['age_group']
    favorite_toys = data['favorite_toys'].split(", ")
    rotation_frequency = data['rotation_frequency']

    # Predict using ML model
    recommended_toys = model.predict([[age_group, rotation_frequency]])

    return {
        "child_name": data['child_name'],
        "rotation_schedule": f"Every {rotation_frequency}",
        "recommended_toys": list(set(recommended_toys + favorite_toys))
    }
