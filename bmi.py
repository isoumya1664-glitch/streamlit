import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (m)", min_value=0.1)

if st.button("Calculate"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.write("Underweight")
    elif bmi < 25:
        st.write("Normal Weight")
    elif bmi < 30:
        st.write("Overweight")
    else:
        st.write("Obese")