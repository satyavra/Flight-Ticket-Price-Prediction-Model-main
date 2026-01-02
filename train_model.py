import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load and prepare data
df = pd.read_csv('Flight-Ticket-Price-Prediction-Model-main/flight ticket price prediciton dataset.csv')

# Drop unnecessary column
df = df.drop(columns=['Unnamed: 0'])

# Encode categorical features
label_encoders = {}
categorical_columns = ['airline', 'flight', 'source_city', 'departure_time', 'stops', 'arrival_time', 'destination_city', 'class']

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Split features and target
X = df.drop(columns=['price'])
y = df['price']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

model = LinearRegression()
model.fit(X_train, y_train)

# Save model and encoders
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('label_encoders.pkl', 'wb') as f:
    pickle.dump(label_encoders, f)

print("Model and encoders saved successfully!")
