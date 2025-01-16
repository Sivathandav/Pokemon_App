from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Get environment-specific variables
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://pokemon:af6Ad2z30j3VbnLYtnAPq4owlPq5QdPY@dpg-cu4dp0bqf0us738068p0-a.oregon-postgres.render.com/pokemon_kd3l')

# DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/pokemon_kd3l')
is_deployment = os.getenv('IS_DEPLOYMENT', 'false') == 'true'  # Set this environment variable to 'true' when deploying

# Set sslmode based on the environment (disable locally, require on deployment)
sslmode = 'require' if is_deployment else 'disable'

# Database connection
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
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
    app.run(debug=False)
