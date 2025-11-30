import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")  # FULL-SCREEN WIDTH DASHBOARD

# ---------------- DATA LOAD ---------------- #
df = pd.read_excel("forecast_results_2024_2029 (5) (1).xlsx")  # Your final dataset

st.title("🔋 Global Energy Forecast Interactive Dashboard")

# ---------------- SIDEBAR FILTERS ---------------- #
st.sidebar.header("Filter Controls")

country = st.sidebar.selectbox("Select Country", df["Area"].unique())
category = st.sidebar.selectbox("Select Category", df["Category"].unique())
subcat = st.sidebar.selectbox("Select Subcategory", df["Subcategory"].unique())
model = st.sidebar.selectbox("Select Model", df["Model"].unique())

# Year slider that controls graphs
year = st.sidebar.slider("Select Forecast Year", 2024, 2029, step=1)

# Filter according to selected options
data = df[
    (df.Area == country) &
    (df.Category == category) &
    (df.Subcategory == subcat) &
    (df.Model == model)
]

# ---------------- FIVE GRAPHS SECTION ---------------- #
st.subheader(f"📈 Forecast Visualization for {country} | {category} | {model}")

# Convert to series for plotting
years = [2024, 2025, 2026, 2027, 2028, 2029]
values = [data[f"pred_{y}"].values for y in years]

# Layout — 5 Graphs Visible at Once
colA, colB = st.columns(2)
colC, colD, colE = st.columns(3)

def plot_graph(axis, val, title):
    axis.plot(val)
    axis.set_title(title)
    axis.set_xlabel("Index")
    axis.set_ylabel("Forecast Value")

# GRAPH 1
fig1, ax1 = plt.subplots()
plot_graph(ax1, values[0], "Pred 2024")
colA.pyplot(fig1)

# GRAPH 2
fig2, ax2 = plt.subplots()
plot_graph(ax2, values[1], "Pred 2025")
colB.pyplot(fig2)

# GRAPH 3
fig3, ax3 = plt.subplots()
plot_graph(ax3, values[2], "Pred 2026")
colC.pyplot(fig3)

# GRAPH 4
fig4, ax4 = plt.subplots()
plot_graph(ax4, values[3], "Pred 2027")
colD.pyplot(fig4)

# GRAPH 5 (DEPENDENT SLIDER GRAPH)
fig5, ax5 = plt.subplots()
plot_graph(ax5, data[f"pred_{year}"].values, f"📌 Selected Year: {year}")
colE.pyplot(fig5)

# ---------------- DATA TABLE -------------------- #
st.subheader("📄 Full Forecast Data Table")
st.dataframe(data, height=350)
