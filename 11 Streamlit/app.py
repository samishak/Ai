import streamlit as st
import pandas as pd
import numpy as np

# Title of app
st.title("Hello Streamlit")

# Display simple text
st.write("Simple text")

# Create a simple dataframe (same length columns)
df = pd.DataFrame({
    "first column": [1, 2, 3, 4, 5],
    "second column": [10, 20, 30, 40, 50]
})

# Display dataframe
st.write("Here is the dataframe:")
st.dataframe(df)   # nicer than st.write(df)

# Create line chart data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

# Display line chart
st.line_chart(chart_data)
