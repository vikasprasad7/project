from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from langgraph.graph import Graph
from langgraph.nodes import LLMNode

app = Flask(__name__)
CORS(app)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="healthcare_db"
)
cursor = db.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS communications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255),
    professional_name VARCHAR(255),
    date VARCHAR(50),
    time VARCHAR(50),
    sentiment VARCHAR(50)
)
""")

# LangGraph LLM node
llm_extract = LLMNode(
    name="extract_form",
    model="gpt-4",  # or any LLM you prefer
    prompt_template="""
    Extract the following fields from the user's message:
    - Healthcare professional name
    - Date
    - Time
    - Sentiment (positive/neutral/negative)

    Return as JSON:
    {
      "professional_name": "...",
      "date": "...",
      "time": "...",
      "sentiment": "..."
    }
    """
)

graph = Graph()
graph.add_nodes([llm_extract])

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_name = data["user_name"]
    message = data["message"]

    # Run through LLM
    result = graph.run({"message": message})
    form_data = result["extract_form"]

    # Save to MySQL
    cursor.execute("""
        INSERT INTO communications (user_name, professional_name, date, time, sentiment)
        VALUES (%s, %s, %s, %s, %s)
    """, (user_name, form_data["professional_name"], form_data["date"], form_data["time"], form_data["sentiment"]))
    db.commit()

    return jsonify(form_data)
