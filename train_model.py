import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

data = pd.read_csv("winequality.csv")

if "Id" in data.columns:
    data = data.drop("Id", axis=1)


X = data.drop("quality", axis=1)
y = data["quality"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

pickle.dump(model, open("wine_quality_model.pkl", "wb"))

pred = model.predict(X_test)

print("R2 Score :", r2_score(y_test, pred))
print("MAE :", mean_absolute_error(y_test, pred))
print("Model Saved Successfully!")