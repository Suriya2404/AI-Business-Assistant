from gemini_client import generate_response


def explain_result(question, sql_query, results):
    prompt = f"""
You are a business intelligence assistant.

The user asked:
{question}

The SQL query used was:
{sql_query}

The database returned:
{results}

Explain the result clearly in natural language.

Rules:
- Answer the user's question directly.
- Use only the information contained in the database result.
- Do not invent or estimate any numbers.
- Keep the explanation concise.
"""

    return generate_response(prompt)