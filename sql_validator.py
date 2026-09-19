import re

def validate_sql(sql_query):
    sql_query = sql_query.strip()

    if not sql_query:
        return False

    # Allow only SELECT or WITH queries
    upper_query = sql_query.upper()

    if "--" in sql_query or "/*" in sql_query or "*/" in sql_query:
        return False

    if not (upper_query.startswith("SELECT") or upper_query.startswith("WITH")):
        return False

    # Allow only one SQL statement
    if ";" in sql_query[:-1]:
        return False

    forbidden_words = [
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "CREATE",
        "REPLACE",
        "ATTACH",
        "DETACH",
        "PRAGMA"
    ]

    for word in forbidden_words:
        if re.search(r"\b" + word + r"\b", upper_query):
            return False

    return True



