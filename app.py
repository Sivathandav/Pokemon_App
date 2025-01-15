from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Database connection
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:pongal%40546@localhost:5432/Pokemon')  # Corrected URL
conn = psycopg2.connect(DATABASE_URL, sslmode='disable')
cursor = conn.cursor()

@app.route('/', methods=['GET', 'POST'])

def index():
    search_term = request.form.get('search_term', '')  # Search term from form
    type_filter = request.form.get('type_filter', '')  # Type filter from form
    sort_order = request.form.get('sort_order', 'id')  # Sort order, default by id

    # Start building the SQL query
    query = "SELECT * FROM pokemon WHERE 1=1"  # This ensures we can always add additional filters

    # Initialize parameters with search_term (if provided)
    params = []
    
    if search_term:  # If there's a search term, add to the query
        query += " AND name LIKE %s"
        params.append(f"%{search_term}%")
    
    if type_filter:  # Filter by type if selected
        query += " AND type_id = %s"  # Adjusted column name to type_name
        params.append(type_filter)

    query += f" ORDER BY {sort_order}"  # Order by selected field

    # Execute the query
    try:
        cursor.execute(query, tuple(params))
        pokemon = cursor.fetchall()
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of error
        print(f"Error: {e}")
        pokemon = []

    # Fetch the unique types for filter dropdown
    cursor.execute("SELECT DISTINCT type_id FROM pokemon")  # Adjusted column name to type_name
    types = cursor.fetchall()

    return render_template('index.html', pokemon=pokemon, types=types)


if __name__ == "__main__":
    app.run(debug=True)
