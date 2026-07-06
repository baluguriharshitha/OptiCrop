import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

import joblib


# Load Dataset

dataset = pd.read_csv("dataset/Crop_recommendation.csv")


X = dataset.drop("label", axis=1)

y = dataset["label"]


X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42

)


model = RandomForestClassifier(

    n_estimators=200,

    random_state=42

)


model.fit(

    X_train,

    y_train

)


prediction = model.predict(X_test)


accuracy = accuracy_score(

    y_test,

    prediction

)


print("Accuracy :", accuracy)


joblib.dump(

    model,

    "backend/app/ml/crop_model.pkl"

)


print("Model Saved Successfully!")
