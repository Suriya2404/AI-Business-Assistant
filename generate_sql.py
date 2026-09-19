import sqlite3
from dotenv import load_dotenv


from gemini_client import generate_response
from result_explainer import explain_result
from sql_validator import validate_sql
from schema_context import SCHEMA

load_dotenv()

def ask_database(question):
    prompt = f"""
    You are a SQL expert.
    
    Convert the user's question into a SQLite SQL query.
    
    DATABASE SCHEMA:
    {SCHEMA}
    
    USER QUESTION:
    {question}
    
    Rules:
    - Generate SQLite-compatible SQL.
    - Use only tables and columns from the schema.
    - Make sure the SQL fully answers the user's question.
    - For questions involving "most", "least", "highest", "lowest", "top", or "bottom", use appropriate aggregation and sorting.
    - Use COUNT for questions about number or frequency.
    - Use SUM for questions about total amounts.
    - Use AVG for questions asking for averages.
    - Use MAX or MIN when asking for the highest or lowest individual value.
    - When using COUNT, SUM, or AVG to determine a result, include the calculated value in the SELECT clause when it helps answer the question.
    - If the user's question is not related to the e-commerce database, do not generate SQL. Return exactly: NOT_A_DATABASE_QUESTION
    - Return ONLY the SQL query.
    - Do not explain the query.
    """

    sql_query = generate_response(prompt)
    sql_query = sql_query.strip()

    if sql_query == "NOT_A_DATABASE_QUESTION":
        return (
            "I'm designed to answer questions about the e-commerce database. "
            "Please ask a business or data-related question.",
            [],
            []
        )

    print("\nGenerated SQL:")
    print(sql_query)

    if sql_query.startswith("```"):
        sql_query = sql_query.replace("```sql", "")
        sql_query = sql_query.replace("```", "")
        sql_query = sql_query.strip()

    if not validate_sql(sql_query):
        return (
            "I couldn't safely process that query. Please try rephrasing your question.",
            [],
            []
        )
    else:
        try:
            connection = sqlite3.connect(
                "file:data/olist.db?mode=ro",
                uri=True
            )
            cursor = connection.cursor()

            try:
                cursor.execute(sql_query)

                columns = [description[0] for description in cursor.description]

                results = cursor.fetchall()

                if not results:
                    connection.close()

                    return (
                        "No matching data was found in the database.",
                        [],
                        columns
                    )

            except sqlite3.Error:
                connection.close()

                return (
                    "I couldn't execute the generated query. Please try rephrasing your question.",
                    [],
                    []
                )

            if not results:
                connection.close()
                return (
                    "No matching data was found in the database.",
                    [],
                    columns
                )

            connection.close()

        except sqlite3.Error:
            return (
                "I couldn't execute the generated query. Please try rephrasing your question.",
                [],
                []
            )

        try:
            explanation = explain_result(question, sql_query, results)
        except Exception:
            explanation = "The data was retrieved successfully, but I couldn't generate a natural-language explanation."

        return explanation, results, columns

if __name__ == "__main__":
        question = input("Ask a question about the database: ")
        answer, results, columns = ask_database(question)
        print(answer)
        print(results)
        print(columns)

