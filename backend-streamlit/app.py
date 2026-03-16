import streamlit as st
import pandas as pd

st.title("Smart Financial Advisor")

st.write("Upload your financial CSV file to analyze expenses.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    if "Category" in df.columns and "Amount" in df.columns:

        summary = df.groupby("Category")["Amount"].sum()

        st.subheader("Expense Analysis")
        st.bar_chart(summary)

        total = df["Amount"].sum()

        st.write("Total Spending:", total)

        if total > 5000:
            st.warning("Your spending is high. Consider reducing unnecessary expenses.")
        else:
            st.success("Your spending is under control.")

    else:
        st.error("CSV must contain 'Category' and 'Amount' columns.")
