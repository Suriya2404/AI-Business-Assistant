import pandas as pd
import streamlit as st

def generate_chart(df):
    if len(df.columns) == 2 and len(df) > 1:

        first_column = df.iloc[:, 0]
        second_column = df.iloc[:, 1]

        if pd.api.types.is_numeric_dtype(second_column):

            first_values = first_column.astype(str)

            looks_like_date = first_values.str.match(
                r"^\d{4}-\d{2}(-\d{2})?$"
            ).all()

            if looks_like_date:
                date_values = pd.to_datetime(
                    first_column,
                    format="mixed",
                    errors="coerce"
                )

                if date_values.notna().all():
                    df[df.columns[0]] = date_values
                    st.line_chart(
                        df.set_index(df.columns[0])
                    )
                    return True

            st.bar_chart(
                df.set_index(df.columns[0])
            )
            return True

    return False

if __name__ == "__main__":
    data = {
        "payment_type": ["credit_card", "boleto", "voucher", "debit_card"],
        "transactions": [76795, 19784, 5775, 1529]
    }

    df = pd.DataFrame(data)

    generate_chart(df)