# 🤖 AI Business Intelligence Assistant

An AI-powered business intelligence assistant that allows users to analyze e-commerce data using natural language.

Instead of writing SQL queries manually, users can simply ask questions such as:

- Which state has the highest number of orders?
- What is the average payment value?
- What are the top 5 payment methods?
- How many orders were placed each month?

The system uses a Gemini LLM to convert natural-language questions into SQL queries, executes the validated queries against a SQLite database, and presents the results through conversational responses, tables, and automatic visualizations.

## ✨ Features

- 💬 Natural-language conversational interface
- 🧠 AI-powered natural language to SQL generation
- 🗄️ SQLite relational database integration
- 🔒 Read-only database execution and SQL validation
- 📊 Automatic data visualizations
- 📋 Formatted query results
- 💡 AI-generated explanations of database results
- ⚠️ Handling of invalid, empty, and non-business questions
- 🔄 Conversational query history
- 🎨 Streamlit-based user interface

## 🏗️ Architecture

The application follows a natural-language-to-SQL pipeline:

```text
User Question
      ↓
Streamlit Chat Interface
      ↓
Gemini LLM
      ↓
SQL Generation
      ↓
SQL Validation
      ↓
Read-Only SQLite Database
      ↓
Query Results
      ↓
Result Processing
      ↓
Gemini Result Explanation
      ↓
Conversational Response
      ↓
Table / Visualization

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and data processing |
| Gemini LLM | Natural-language understanding, SQL generation, and result explanation |
| SQLite | Relational database and query execution |
| Pandas | Data processing and result formatting |
| Streamlit | Web interface and conversational UI |
| Matplotlib | Data visualization support |

## 📊 Dataset

This project uses the **Brazilian E-Commerce Public Dataset by Olist**, containing approximately 100,000 orders and related customer, product, seller, payment, review, and order-item data.

The dataset was used to build the SQLite relational database for business analysis.

Source: Brazilian E-Commerce Public Dataset by Olist — Kaggle

> Note: The dataset is subject to its original license and attribution requirements.

## 📁 Project Structure

```text
AI-Business-Assistant/
│
├── app.py                  # Streamlit application
├── generate_sql.py         # Natural language to SQL pipeline
├── gemini_client.py        # Gemini API client
├── result_explainer.py     # AI-generated result explanations
├── sql_validator.py        # SQL safety validation
├── chart_generator.py      # Automatic visualizations
├── schema_context.py       # Database schema for the LLM
├── database.py             # SQLite database creation
├── load_data.py            # Dataset loading
├── query_database.py       # Database querying utilities
├── schema.sql              # SQLite database schema
├── README.md
│
├── data/
│   └── raw/                # Source CSV files
│
└── .gitignore

## ⚙️ How It Works

1. The user asks a business question through the Streamlit chat interface.
2. The question and database schema are sent to the Gemini LLM.
3. Gemini generates a SQLite-compatible SQL query.
4. The SQL validator checks the generated query and allows only safe read-only operations.
5. The validated query is executed against the SQLite database in read-only mode.
6. The query results are processed and formatted using Pandas.
7. Gemini generates a concise natural-language explanation based only on the returned data.
8. The application displays the explanation, data table, and appropriate visualization when applicable.

## 🔒 Security & Safety

The application includes several safeguards around AI-generated SQL:

- Only `SELECT` and `WITH` queries are permitted.
- SQL statements containing write or schema-modifying operations such as `INSERT`, `UPDATE`, `DELETE`, `DROP`, and `ALTER` are rejected.
- SQL comments and multiple statements are rejected.
- Database access is performed using SQLite's read-only mode.
- Gemini API credentials are stored in environment variables and are not included in the source code.
- Non-database questions are handled without executing SQL.

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd AI-Business-Assistant

## 💬 Usage

Once the application is running, ask questions about the e-commerce database directly through the chat interface.

Example questions:

- Which state has the highest number of orders?
- What is the average payment value?
- What are the top 5 payment methods by number of transactions?
- How many orders were placed each month?
- Which product category generated the highest total sales?

The assistant generates the appropriate SQL query, retrieves the relevant data, and presents the result as a conversational response with a table or visualization when applicable.

## 🔮 Future Improvements

- 📈 Support for more advanced business analytics
- 🧩 Improved SQL generation for complex queries
- 📊 More visualization types
- 🔐 More advanced SQL parsing and validation
- ⚡ Query caching for frequently asked questions
- 🌐 Deployment as a publicly accessible web application

## 🔑 Configuration

The application requires a Gemini API key.

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here

## 🙏 Acknowledgements

- Google Gemini for the large language model used for natural-language understanding, SQL generation, and result explanation.
- Olist Brazilian E-Commerce Public Dataset for the e-commerce data used in this project.
- Streamlit for the application interface and visualization framework.