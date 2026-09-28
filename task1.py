import streamlit as st
import pandas as pd

st.title("Student Performance Dashboard")

# Read CSV
df = pd.read_csv("student_performance.csv")

# Display complete dataset
st.subheader("Student Data")
st.dataframe(df)

# Statistics
st.write("Total Students:", len(df))
st.write("Average Marks:", df["Marks"].mean())
st.write("Average Attendance:", df["Attendance"].mean())

# Department filter
department = st.selectbox(
    "Select Department",
    ["All"] + list(df["Department"].unique())
)

# Marks filter
min_marks = st.slider(
    "Minimum Marks",
    int(df["Marks"].min()),
    int(df["Marks"].max()),
    int(df["Marks"].min())
)

# Attendance filter
attendance = st.checkbox("Attendance 75% or above")

# Apply filters
filtered = df.copy()

if department != "All":
    filtered = filtered[filtered["Department"] == department]

filtered = filtered[filtered["Marks"] >= min_marks]

if attendance:
    filtered = filtered[filtered["Attendance"] >= 75]

# Display filtered data
st.subheader("Filtered Data")
st.dataframe(filtered)

# Highest and lowest marks
if len(filtered) > 0:
    st.write("Highest Marks:", filtered["Marks"].max())
    st.write("Lowest Marks:", filtered["Marks"].min())

# Download CSV
csv = filtered.to_csv(index=False)

st.download_button(
    "Download Filtered Data",
    csv,
    "filtered_students.csv",
    "text/csv"
)

# Chart
st.subheader("Average Marks by Department")

avg_marks = df.groupby("Department")["Marks"].mean()

st.bar_chart(avg_marks)