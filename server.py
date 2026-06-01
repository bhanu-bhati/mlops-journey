import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize the API
app = FastAPI()

# 2. Load the trained machine learning model brain into memory
with open("house_model.pkl", "rb") as file:
    model = pickle.load(file)


# 3. Define the exact structure of data the user must send us
class HouseFeatures(BaseModel):
    sqft: float
    rooms: int


# 4. Create an endpoint that accepts data and calculates predictions
@app.post("/predict")
def predict_price(features: HouseFeatures):
    # Format inputs into the shape our model expects: [[sqft, rooms]]
    input_data = [[features.sqft, features.rooms]]

    # Calculate the prediction
    predicted_array = model.predict(input_data)

    # Pull the first value out of the array using [0] to avoid TypeErrors
    final_scalar = float(predicted_array[0])

    # Return the result back as a clean JSON package
    return {
        "status": "success",
        "input_received": {"sqft": features.sqft, "rooms": features.rooms},
        "predicted_price_lakhs": round(final_scalar, 2),
    }
