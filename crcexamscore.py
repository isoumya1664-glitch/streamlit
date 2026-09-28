import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Student Exam Score Predictor",
    layout="wide"
)

df = pd.read_csv("linear_regression_student_performance_1000_scaled.csv")



with open("exam_score_model.pkl", "rb") as file:
    model = pickle.load(file)



st.title("Student Exam Score Prediction")
st.subheader("Linear Regression Machine Learning Project")

st.header("Dataset")

st.write(f"Dataset Shape: **{df.shape[0]} rows × {df.shape[1]} columns**")

st.dataframe(df, use_container_width=True)


st.header("Machine Learning Model")

st.write("**Algorithm:** Linear Regression")

st.subheader("Model Parameters")

col1, col2 = st.columns(2)

with col1:
    st.write("**Intercept:**")
    st.write(model.intercept_)

with col2:
    st.write("**Number of Features:**")
    st.write(len(model.coef_))


st.write("**Coefficients:**")

coefficients = pd.DataFrame({
    "Feature": [
        "study_hours",
        "attendance",
        "assignment_score",
        "previous_score",
        "sleep_hours",
        "practice_tests"
    ],
    "Coefficient": model.coef_
})

st.dataframe(coefficients, use_container_width=True)



st.header("Predict Exam Score")

st.write("Enter the student's details below.")

col1, col2, col3 = st.columns(3)

with col1:
    study_hours = st.number_input(
        "Study Hours",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01
    )

    attendance = st.number_input(
        "Attendance",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01
    )

with col2:
    assignment_score = st.number_input(
        "Assignment Score",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01
    )

    previous_score = st.number_input(
        "Previous Score",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01
    )

with col3:
    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01
    )

    practice_tests = st.number_input(
        "Practice Tests",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01
    )



if st.button("Predict Exam Score", use_container_width=True):

    input_data = pd.DataFrame([[
        study_hours,
        attendance,
        assignment_score,
        previous_score,
        sleep_hours,
        practice_tests
    ]], columns=[
        "study_hours",
        "attendance",
        "assignment_score",
        "previous_score",
        "sleep_hours",
        "practice_tests"
    ])

    prediction = model.predict(input_data)[0]

    st.success("Prediction Generated Successfully!")

    st.metric(
        label="Predicted Exam Score",
        value=f"{prediction:.4f}"
    )