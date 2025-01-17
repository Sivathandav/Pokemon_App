import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from flask import Flask, render_template, request
import psycopg2
import os
import requests

app = Flask(__name__)

# Get environment-specific variables
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql://pokemon:af6Ad2z30j3VbnLYtnAPq4owlPq5QdPY@dpg-cu4dp0bqf0us738068p0-a.oregon-postgres.render.com/pokemon_kd3l'
)

is_deployment = os.getenv('IS_DEPLOYMENT', 'false') == 'true'
sslmode = 'require' if is_deployment else 'disable'

# Database connection
conn = psycopg2.connect(
    DATABASE_URL,
    sslmode='require'
)

cursor = conn.cursor()

# Function to generate radar chart for Pokémon stats
def generate_radar_chart(stats):
    labels = list(stats.keys())
    values = list(stats.values())

    num_vars = len(labels)

    # Compute angle for each axis of the radar chart
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Close the circle
    values += values[:1]
    angles += angles[:1]

    # Create radar chart
    fig, ax = plt.subplots(figsize=(7,5), dpi=150, subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='skyblue', alpha=0.25)
    ax.plot(angles, values, color='blue', linewidth=2)

    ax.set_yticklabels([])  # Hide the radial labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color='grey', fontsize=15,fontweight='bold', ha='center',)

     # Adjust label positions to avoid overlap
    for label, angle in zip(ax.get_xticklabels(), angles[:-1]):
            angle_deg = np.degrees(angle)
            if 90 <= angle_deg <= 270:
                label.set_horizontalalignment('right')
            else:
                label.set_horizontalalignment('left')
            label.set_y(label.get_position()[1] + 0.05)

    ax.set_title(f"Pokémon Stats", size=15, color='blue', pad=30)

    # Ensure chart is centered
    fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1) 

    # Save to BytesIO and return base64 encoded image
    img_stream = io.BytesIO()
    plt.savefig(img_stream, format='png',bbox_inches='tight')
    img_stream.seek(0)

    chart_url = base64.b64encode(img_stream.read()).decode('utf-8')
    plt.close()

    return chart_url

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    page = int(request.args.get('page', 1))
    per_page = 10

    search_term = request.args.get('search_term', '')
    type_filter = request.args.get('type_filter', '')
    sort_order = request.args.get('sort_order', 'id')

    valid_sort_columns = ['id', 'name', 'weight', 'height']
    if sort_order not in valid_sort_columns:
        sort_order = 'id'

    query = """
        SELECT p.id, p.name, t.type_name, p.image_url, p.weight, p.height
        FROM pokemon p
        JOIN pokemon_type t ON p.type_id = t.id
        WHERE 1=1
    """
    params = []

    if search_term:
        query += " AND p.name ILIKE %s"
        params.append(f"%{search_term}%")

    if type_filter:
        query += " AND t.type_name = %s"
        params.append(type_filter)

    offset = (page - 1) * per_page
    query += f" ORDER BY {sort_order} LIMIT %s OFFSET %s"
    params.extend([per_page, offset])

    try:
        cursor.execute(query, tuple(params))
        pokemon = cursor.fetchall()
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        pokemon = []

    cursor.execute("SELECT DISTINCT type_name FROM pokemon_type")
    types = [row[0] for row in cursor.fetchall()]

    count_query = """
        SELECT COUNT(*)
        FROM pokemon p
        JOIN pokemon_type t ON p.type_id = t.id
        WHERE 1=1
    """
    count_params = []
    if search_term:
        count_query += " AND p.name ILIKE %s"
        count_params.append(f"%{search_term}%")
    if type_filter:
        count_query += " AND t.type_name = %s"
        count_params.append(type_filter)

    cursor.execute(count_query, tuple(count_params))
    total_pokemon = cursor.fetchone()[0]
    total_pages = (total_pokemon + per_page - 1) // per_page

    return render_template(
        'index.html',
        pokemon=pokemon,
        types=types,
        search_term=search_term,
        type_filter=type_filter,
        sort_order=sort_order,
        page=page,
        total_pages=total_pages
    )

# Pokémon details route
@app.route("/pokemon/<int:poke_id>")
def pokemon_details(poke_id):
    # Fetch Pokémon details from the database, including the type name
    cursor.execute("""
        SELECT 
            p.id, 
            p.name, 
            pt.type_name,  -- Fetch type name from pokemon_type
            p.height, 
            p.weight, 
            p.image_url 
        FROM 
            pokemon p
        JOIN 
            pokemon_type pt 
        ON 
            p.type_id = pt.id
        WHERE 
            p.id = %s
    """, (poke_id,))
    pokemon = cursor.fetchone()
    if pokemon is None:
        return "Pokémon not found", 404

    # Fetch Pokémon stats from PokéAPI
    pokemon_name = pokemon[1].lower()  # Use name to fetch data
    pokeapi_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    try:
        response = requests.get(pokeapi_url)
        response.raise_for_status()
        api_data = response.json()
        stats = {
            "HP": api_data['stats'][0]['base_stat'],
            "Attack": api_data['stats'][1]['base_stat'],
            "Defense": api_data['stats'][2]['base_stat'],
            "Special Attack": api_data['stats'][3]['base_stat'],
            "Special Defense": api_data['stats'][4]['base_stat'],
            "Speed": api_data['stats'][5]['base_stat'],
        }
    except requests.RequestException as e:
        print(f"Error fetching data from PokéAPI: {e}")
        stats = None

    # Get the type(s) of the selected Pokémon
    cursor.execute(""" 
        SELECT t.type_name 
        FROM pokemon_type t
        JOIN pokemon p ON p.type_id = t.id
        WHERE p.id = %s
    """, (poke_id,))
    pokemon_types = [row[0] for row in cursor.fetchall()]

    # Pagination for similar Pokémon
    page = int(request.args.get('page', 1))
    per_page = 5

    # Query similar Pokémon based on the type(s)
    type_filter = " OR ".join([f"t.type_name = %s" for _ in pokemon_types])
    query = f"""
        SELECT p.id, p.name, t.type_name, p.height, p.weight, p.image_url
        FROM pokemon p
        JOIN pokemon_type t ON p.type_id = t.id
        WHERE ({type_filter}) AND p.id != %s
        ORDER BY p.id
        LIMIT %s OFFSET %s
    """
    params = pokemon_types + [poke_id, per_page, (page - 1) * per_page]
    cursor.execute(query, tuple(params))
    similar_pokemon = cursor.fetchall()

    # Count the total number of similar Pokémon
    count_query = f"""
        SELECT COUNT(*)
        FROM pokemon p
        JOIN pokemon_type t ON p.type_id = t.id
        WHERE ({type_filter}) AND p.id != %s
    """
    cursor.execute(count_query, tuple(pokemon_types + [poke_id]))
    total_similar = cursor.fetchone()[0]
    total_pages = (total_similar + per_page - 1) // per_page

    # Generate the radar chart
    chart_url = generate_radar_chart(stats) if stats else None

    return render_template(
        'details.html',
        pokemon=pokemon,
        stats=stats,
        similar_pokemon=similar_pokemon,
        chart_url=chart_url,
        page=page,
        total_pages=total_pages
    )


if __name__ == "__main__":
    app.run(debug=True)
