# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("CGPA Calculator")

    # Get user input for grades and credits
    num_courses = st.number_input("Enter the number of courses completed:", min_value=1, value=5, step=1)

    grades = []
    credits = []
    for i in range(num_courses):
        grade = st.selectbox(f"Select grade for course {i+1}:", ["A", "B", "C", "D", "F"])
        credit = st.number_input(f"Enter credits for course {i+1}:", min_value=1, value=3, step=1)
        grades.append(grade)
        credits.append(credit)

    # Calculate CGPA
    total_credits = sum(credits)
    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    weighted_sum = sum(grade_points[grade] * credit for grade, credit in zip(grades, credits))
    cgpa = weighted_sum / total_credits

    # Display CGPA
    st.write(f"Your CGPA is: **{cgpa:.2f}**")

if __name__ == "__main__":
    main()
