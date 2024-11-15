# prompt: use streamlit to create an interactive dashboard

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
import streamlit as st

# Load the data
data = pd.read_csv('IBES_updated.csv')

st.title("Interactive Data Exploration Dashboard")

# Sidebar for user selections
st.sidebar.header("Select Options")
selected_columns = st.sidebar.multiselect("Select Columns for Analysis", data.columns)

# Histograms
if not selected_columns:
    st.write("Please select at least one column from the sidebar to view the plots.")
else:
    for column in selected_columns:
        if pd.api.types.is_numeric_dtype(data[column]):
            st.subheader(f"Histogram of {column}")
            fig, ax = plt.subplots()
            ax.hist(data[column], bins=20)
            ax.set_xlabel(column)
            ax.set_ylabel('Frequency')
            st.pyplot(fig)

# Box plots
for column in selected_columns:
    if pd.api.types.is_numeric_dtype(data[column]):
        st.subheader(f"Box Plot of {column}")
        fig, ax = plt.subplots()
        ax.boxplot(data[column])
        ax.set_ylabel(column)
        st.pyplot(fig)

# Scatter Matrix
if len(selected_columns) > 0:
    numeric_cols = [col for col in selected_columns if pd.api.types.is_numeric_dtype(data[col])]
    if len(numeric_cols) > 0:
        st.subheader("Scatter Matrix")
        fig, ax = plt.subplots(figsize=(10, 10))
        scatter_matrix(data[numeric_cols], alpha=0.2, figsize=(10, 10), diagonal='hist', ax=ax)
        st.pyplot(fig)

# Correlation Heatmap
if len(selected_columns) > 0:
    numeric_cols = [col for col in selected_columns if pd.api.types.is_numeric_dtype(data[col])]
    if len(numeric_cols) > 0:
        correlation_matrix = data[numeric_cols].corr()
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        st.pyplot(fig)
