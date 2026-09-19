import streamlit as st
import pandas as pd
from generate_sql import ask_database
from chart_generator import generate_chart

st.set_page_config(
    page_title="AI Business Intelligence Assistant",
    page_icon="🤖",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.title("🤖 AI BI Assistant")

    st.caption("Natural-language analytics for e-commerce data.")

    st.divider()

    st.subheader("📌 About")

    st.write(
        "This AI Business Intelligence Assistant "
        "allows users to ask questions about e-commerce "
        "data using natural language."
    )

    with st.expander("🛠️ Technology"):
        st.write("• Python")
        st.write("• Gemini LLM")
        st.write("• SQLite")
        st.write("• Pandas")
        st.write("• Streamlit")

    with st.expander("📊 Capabilities"):
        st.write("• Natural language → SQL")
        st.write("• Database analysis")
        st.write("• Automatic visualizations")
        st.write("• AI-generated insights")

        with st.expander("📊 Capabilities"):
            st.write("• Natural language → SQL")
            st.write("• Database analysis")
            st.write("• Automatic visualizations")
            st.write("• AI-generated insights")

        with st.expander("💡 Example Questions"):
            st.write("• Which state has the highest number of orders?")
            st.write("• What is the average payment value?")
            st.write("• What are the top 5 payment methods?")
            st.write("• How many orders were placed each month?")
            st.write("• Which product category has the highest sales?")

st.title("🤖 AI Business Intelligence Assistant")

st.markdown(
    "Ask questions about your e-commerce data in natural language "
    "and get AI-powered insights, tables, and visualizations."
)


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("results"):
            df = pd.DataFrame(
                message["results"],
                columns=message["columns"]
            )

            df.columns = [
                f"{column}_{index}"
                if column in df.columns[:index]
                else column
                for index, column in enumerate(df.columns)
            ]

            for column_index in range(len(df.columns)):
                if df.dtypes.iloc[column_index] == "object":
                    series = df.iloc[:, column_index].astype(str)

                    df.isetitem(
                        column_index,
                        series.str.replace("_", " ", regex=False).str.title()
                    )

            float_columns = df.select_dtypes(include="float").columns

            if len(df) > 1000:
                st.dataframe(df)
            else:
                st.dataframe(
                    df.style.format(
                        {column: "{:.2f}" for column in float_columns}
                    )
                )

            if len(df.columns) == 2 and len(df) > 1:
                generate_chart(df)


question = st.chat_input(
    "Ask about your e-commerce data..."
)

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    try:
        with st.spinner("Analyzing your question..."):
            answer, results, columns = ask_database(question)


            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "results": results,
                "columns": columns
            })

    except Exception:
        st.error(
                "⚠️ I couldn't process your question. "
                "Please try rephrasing it."
            )

    with st.chat_message("assistant"):

        st.markdown(answer)

        if results:

            df = pd.DataFrame(results, columns=columns)

            df.columns = [
                f"{column}_{index}"
                if column in df.columns[:index]
                else column
                for index, column in enumerate(df.columns)
            ]

            for column_index in range(len(df.columns)):
                if df.dtypes.iloc[column_index] == "object":
                    series = df.iloc[:, column_index].astype(str)

                    df.isetitem(
                        column_index,
                        series.str.replace("_", " ", regex=False).str.title()
                    )

            float_columns = df.select_dtypes(include="float").columns

            if len(df) > 1000:
                st.dataframe(df)
            else:
                st.dataframe(
                    df.style.format(
                        {column: "{:.2f}" for column in float_columns}
                    )
                )

            if len(df.columns) == 2 and len(df) > 1:
                generate_chart(df)

            st.divider()

            st.caption("Built with Python • Gemini • SQLite • Streamlit")