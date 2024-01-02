import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "CC GENERAL.csv"
data = pd.read_csv(file_path)

# Data Cleaning
data = data.dropna()

# Feature Selection
selected_features = ["BALANCE", "PURCHASES", "CASH_ADVANCE", "CREDIT_LIMIT", "PAYMENTS"]
X = data[selected_features]

# Sidebar
st.sidebar.title("Settings")
num_clusters = st.sidebar.slider("Select number of clusters", min_value=2, max_value=10, value=3)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)

# Streamlit App
st.title("Credit Card Clustering App")

# Display the clustered data
st.write("### Clustered Data")
st.write(data)


# Display cluster distribution
st.write("### Cluster Distribution")
cluster_distribution = data['Cluster'].value_counts().sort_index()
st.bar_chart(cluster_distribution)

# Display cluster centroids
st.write("### Cluster Centroids")
cluster_centroids = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=selected_features)
st.write(cluster_centroids)
