import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load dataset
def load_data():
    try:
        return pd.read_csv("fitness_log.csv", parse_dates=["Date"])
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date","Steps","Workout","Calories"])

df = load_data()

st.title("🏋️ Fitness Tracker App")

# Add new entry
st.subheader("➕ Log Fitness Activity")
date = st.date_input("Date", datetime.today())
steps = st.number_input("Steps Walked", min_value=0, step=100)
workout = st.text_input("Workout Type (e.g. Running, Yoga)")
calories = st.number_input("Calories Burned", min_value=0)

if st.button("Add Entry"):
    new_row = {"Date": date, "Steps": steps, "Workout": workout, "Calories": calories}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv("fitness_log.csv", index=False)
    st.success("Entry Added!")

# Show data
st.subheader("📊 Your Fitness Log")
st.dataframe(df)

# Summary & Charts
if not df.empty:
    st.subheader("📈 Progress Over Time")

    # Steps Trend
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Steps"], marker="o", label="Steps")
    ax.set_xlabel("Date")
    ax.set_ylabel("Steps")
    ax.legend()
    st.pyplot(fig)

    # Calories Trend
    fig2, ax2 = plt.subplots()
    ax2.plot(df["Date"], df["Calories"], color="red", marker="o", label="Calories")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Calories Burned")
    ax2.legend()
    st.pyplot(fig2)
