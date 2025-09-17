import streamlit as st
import pandas as pd
import numpy as np
import os

from utils import text_to_df_filter

CSV_FILEPATH = "data/Books_preprocessed.csv"

st.title("Books Recommendation!")

if os.path.exists(CSV_FILEPATH):
    df = pd.read_csv(CSV_FILEPATH)
    # st.dataframe(df)

    ### Step 1: Present the application
    st.subheader("Here your can select your next book to read!")
    st.text("For example: ")
    for book in np.random.choice(df['Book_Name'], size=5):
        st.markdown(f"- {book}")

    ### Step 2: Intoduct search bar
    st.subheader("You can find the book that you want here!")
    user_query = st.text_input("Search here ....")

    if st.button("Execute"):
        try:
            python_code_llm = text_to_df_filter(user_query, df)
            st.text(python_code_llm)
            filtered_df = eval(python_code_llm, {"df": df})
            st.dataframe(filtered_df.reset_index(drop=True))
        except Exception as e:
            st.text("Try to make another question")

