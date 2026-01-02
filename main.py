from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

app = FastAPI(title="Flight Price Prediction API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and encoders
try:
    model = pickle.load(open('model.pkl', 'rb'))
    label_encoders = pickle.load(open('label_encoders.pkl', 'rb'))
except FileNotFoundError:
    raise HTTPException(status_code=500, detail="Model files not found. Please run train_model.py first.")

class FlightData(BaseModel):
    airline: str
    flight: str
    source_city: str
    departure_time: str
    stops: str
    arrival_time: str
    destination_city: str
    flight_class: str
    duration: float
    days_left: int

@app.get("/")
async def root():
    return {"message": "Flight Price Prediction API"}

@app.post("/predict")
async def predict_price(data: FlightData):
    try:
        # Convert input to DataFrame and rename class field
        input_dict = data.dict()
        input_dict['class'] = input_dict.pop('flight_class')
        input_data = pd.DataFrame([input_dict])
        
        # Encode categorical features
        for col, encoder in label_encoders.items():
            if col in input_data.columns:
                # Handle unseen labels
                if input_data[col].iloc[0] not in encoder.classes_:
                    # Use the most frequent class as fallback
                    input_data[col] = encoder.transform([encoder.classes_[0]])
                else:
                    input_data[col] = encoder.transform(input_data[col])
        
        # Ensure column order matches training data
        feature_order = ['airline', 'flight', 'source_city', 'departure_time', 'stops', 
                        'arrival_time', 'destination_city', 'class', 'duration', 'days_left']
        input_data = input_data[feature_order]
        
        # Make prediction
        prediction = model.predict(input_data)
        
        return {
            "predicted_price": float(prediction[0]),
            "currency": "INR"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.get("/airlines")
async def get_airlines():
    return {"airlines": list(label_encoders['airline'].classes_)}

@app.get("/cities")
async def get_cities():
    return {"cities": list(label_encoders['source_city'].classes_)}

@app.get("/departure_times")
async def get_departure_times():
    return {"departure_times": list(label_encoders['departure_time'].classes_)}

@app.get("/stops")
async def get_stops():
    return {"stops": list(label_encoders['stops'].classes_)}

@app.get("/arrival_times")
async def get_arrival_times():
    return {"arrival_times": list(label_encoders['arrival_time'].classes_)}

@app.get("/classes")
async def get_classes():
    return {"classes": list(label_encoders['class'].classes_)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
