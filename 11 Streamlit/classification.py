import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.title("Iris Plant Classifier 🌸")
st.write("Predict the Iris species from sepal/petal measurements.")

# ✅ Cache the dataset (fast reloads)
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = iris.target
    target_names = iris.target_names
    return df, target_names, iris.feature_names

df, target_names, feature_names = load_data()

# ✅ Cache the trained model (don’t retrain on every rerun)
@st.cache_resource
def train_model(df):
    model = RandomForestClassifier(random_state=42)
    X = df.iloc[:, :-1]   # all feature columns
    y = df["species"]     # target
    model.fit(X, y)
    return model

model = train_model(df)

st.subheader("Enter flower measurements")

# Sidebar inputs (nice UI)
sepal_length = st.sidebar.slider("Sepal length (cm)", 4.0, 8.0, 5.8, 0.1)
sepal_width  = st.sidebar.slider("Sepal width (cm)",  2.0, 4.5, 3.0, 0.1)
petal_length = st.sidebar.slider("Petal length (cm)", 1.0, 7.0, 4.3, 0.1)
petal_width  = st.sidebar.slider("Petal width (cm)",  0.1, 2.5, 1.3, 0.1)

# Create input row in same order as training data
input_df = pd.DataFrame(
    [[sepal_length, sepal_width, petal_length, petal_width]],
    columns=feature_names
)

st.write("### Your input")
st.dataframe(input_df)

# Predict
pred = model.predict(input_df)[0]
proba = model.predict_proba(input_df)[0]

st.write("### Prediction")
st.success(f"Predicted species: **{target_names[pred]}**")

# Show probabilities
proba_df = pd.DataFrame({"species": target_names, "probability": proba}).sort_values(
    by="probability", ascending=False
)
st.write("### Prediction probabilities")
st.dataframe(proba_df, use_container_width=True)

st.write("### Dataset preview")
st.dataframe(df.head(), use_container_width=True)
