import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

model = None
scaler = None

def train_model():
    global model, scaler

    df = pd.read_csv("bitcoin.csv")

    # Features
    X = df[['Open', 'High', 'Low', 'Close']]
    y = df['Close']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LinearRegression()
    model.fit(X_scaled, y)

def load_model():
    global model, scaler
    if model is None:
        train_model()
    return model, scaler

def predict(open_p, high_p, low_p, close_p, month):
    model, scaler = load_model()

    data = [[open_p, high_p, low_p, close_p]]
    data_scaled = scaler.transform(data)

    pred = model.predict(data_scaled)[0]

    # simple direction logic
    direction = "UP 📈" if pred > close_p else "DOWN 📉"
    confidence = abs(pred - close_p)

    return {
        "price": round(pred, 2),
        "direction": direction,
        "confidence": round(confidence, 2)
    }