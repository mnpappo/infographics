import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load the df
df = pd.read_csv("data.csv")
print(df.head())

month_labels = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

# 1. plot rain vs temp scatter plot

# Normalize the data for better color scaling
df["temp_norm"] = (df["tem"] - df["tem"].min()) / (df["tem"].max() - df["tem"].min())
df["rain_norm"] = (df["rain"] - df["rain"].min()) / (
    df["rain"].max() - df["rain"].min()
)
# Calculate a combined color intensity based on both normalized temperature and rain
df["color_intensity"] = df["temp_norm"] + df["rain_norm"]

scatter = plt.scatter(
    x=df["tem"], y=df["rain"], c=df["color_intensity"], cmap="coolwarm", alpha=0.7
)
plt.colorbar(scatter, label="Color Intensity (Temp + Rain)")

plt.title("Scatter Plot of Rain vs Temperature with Color Intensity")
plt.xlabel("Temperature (°C)")
plt.ylabel("Rainfall (mm)")
# plt.show()


# 2. boxplot of rainfall by month
plt.figure(figsize=(12, 6))
sns.boxplot(x="Month", y="rain", data=df)
plt.title("Monthly Rainfall Distribution")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.xticks(range(0, 12), labels=month_labels)
plt.show()

# 3. plot temperature by month
plt.figure(figsize=(12, 6))
sns.boxplot(x="Month", y="tem", data=df)
plt.title("Monthly Temperature Distribution")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.xticks(range(0, 12), labels=month_labels)
plt.show()

# 4. plot yearly trend of temperature and rainfall
# Calculate the yearly average for temperature and rainfall
yearly_summary = df.groupby("Year").agg({"tem": "mean", "rain": "mean"}).reset_index()

# Rename columns for clarity
yearly_summary = yearly_summary.rename(
    columns={"tem": "Average Temperature (°C)", "rain": "Average Rainfall (mm)"}
)
plt.figure(figsize=(14, 8))
sns.lineplot(
    x="Year",
    y="Average Temperature (°C)",
    data=yearly_summary,
    label="Average Temperature (°C)",
    marker="o",
)
sns.lineplot(
    x="Year",
    y="Average Rainfall (mm)",
    data=yearly_summary,
    label="Average Rainfall (mm)",
    marker="o",
)

plt.title("Yearly Trend of Average Temperature and Rainfall")
plt.xlabel("Year")
plt.ylabel("Average Value")
plt.legend(title="Metric")
plt.show()
