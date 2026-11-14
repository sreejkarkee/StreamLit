import streamlit as st
import pandas as pd

st.title("Student Marks Explorer")

df = pd.read_csv("data/students.csv")

st.sidebar.header("Filters")
subjects = st.sidebar.multiselect(
    "Subject", df["subject"].unique(), default=list(df["subject"].unique())
)
min_marks = st.sidebar.slider("Minimum marks", 0, 100, 0)

filtered = df[(df["subject"].isin(subjects)) & (df["marks"] >= min_marks)]

st.write(f"Showing {len(filtered)} of {len(df)} rows")
st.dataframe(filtered)

st.subheader("Average marks by subject")
st.bar_chart(filtered.groupby("subject")["marks"].mean())

st.subheader("Study hours vs marks")
st.scatter_chart(filtered, x="study_hours", y="marks")
