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
        grade = st.selectbox(f"Select grade for course {i+1}:", ["S", "A", "B", "C", "D", "E", "U", "P", "F", "WA/WQ", "I"])
        if grade in ["P", "F", "WA/WQ", "I"]:
            st.warning(f"Course {i+1} with grade '{grade}' is not included in CGPA calculation.")
            continue
        credit = st.number_input(f"Enter credits for course {i+1}:", min_value=1, value=3, step=1)
        grades.append(grade)
        credits.append(credit)

    # Calculate CGPA
    total_credits = sum(credits)
    grade_points = {"S": 10.0, "A": 9.0, "B": 8.0, "C": 7.0, "D": 6.0, "E": 4.0}
    weighted_sum = sum(grade_points[grade] * credit for grade, credit in zip(grades, credits))
    cgpa = weighted_sum / total_credits if total_credits > 0 else 0

    # Display CGPA
    st.write(f"Your CGPA is: **{cgpa:.2f}**")

if __name__ == "__main__":
    main()
