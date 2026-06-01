import pickle
from sklearn.linear_model import LinearRegression

print("🤖 Training your first Machine Learning model...")

# 1. Training Data: [Size in sqft, Number of Rooms]
X_train = [
    [500, 1],
    [1000, 2],
    [1500, 3],
    [2000, 4],
    [2500, 5]
]

# 2. Target Labels: Price of the houses (in Lakhs)
y_train = [25, 50, 75, 100, 125]

# 3. Initialize and train the mathematical model
model = LinearRegression()
model.fit(X_train, y_train)

print("✅ Model training complete!")

# 4. Save the trained model weights as a permanent file using Pickle
with open("house_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("💾 Model securely saved as 'house_model.pkl'")

