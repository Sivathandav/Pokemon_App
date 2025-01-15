import psycopg2

# Pokémon data
pokemon_data = [{"id":1,"name":"bulbasaur","type":"grass","height":7,"weight":69,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"},{"id":2,"name":"ivysaur","type":"grass","height":10,"weight":130,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png"},{"id":3,"name":"venusaur","type":"grass","height":20,"weight":1000,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png"},{"id":4,"name":"charmander","type":"fire","height":6,"weight":85,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"},{"id":5,"name":"charmeleon","type":"fire","height":11,"weight":190,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/5.png"},{"id":6,"name":"charizard","type":"fire","height":17,"weight":905,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png"},{"id":7,"name":"squirtle","type":"water","height":5,"weight":90,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"},{"id":8,"name":"wartortle","type":"water","height":10,"weight":225,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/8.png"},{"id":9,"name":"blastoise","type":"water","height":16,"weight":855,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png"},{"id":10,"name":"caterpie","type":"bug","height":3,"weight":29,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10.png"},{"id":11,"name":"metapod","type":"bug","height":7,"weight":99,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/11.png"},{"id":12,"name":"butterfree","type":"bug","height":11,"weight":320,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/12.png"},{"id":13,"name":"weedle","type":"bug","height":3,"weight":32,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/13.png"},{"id":14,"name":"kakuna","type":"bug","height":6,"weight":100,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/14.png"},{"id":15,"name":"beedrill","type":"bug","height":10,"weight":295,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/15.png"},{"id":16,"name":"pidgey","type":"normal","height":3,"weight":18,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/16.png"},{"id":17,"name":"pidgeotto","type":"normal","height":11,"weight":300,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/17.png"},{"id":18,"name":"pidgeot","type":"normal","height":15,"weight":395,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/18.png"},{"id":19,"name":"rattata","type":"normal","height":3,"weight":35,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/19.png"},{"id":20,"name":"raticate","type":"normal","height":7,"weight":185,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/20.png"},{"id":21,"name":"spearow","type":"normal","height":3,"weight":20,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/21.png"},{"id":22,"name":"fearow","type":"normal","height":12,"weight":380,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/22.png"},{"id":23,"name":"ekans","type":"poison","height":20,"weight":69,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png"},{"id":24,"name":"arbok","type":"poison","height":35,"weight":650,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/24.png"},{"id":25,"name":"pikachu","type":"electric","height":4,"weight":60,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"},{"id":26,"name":"raichu","type":"electric","height":8,"weight":300,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/26.png"},{"id":27,"name":"sandshrew","type":"ground","height":6,"weight":120,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/27.png"},{"id":28,"name":"sandslash","type":"ground","height":10,"weight":295,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/28.png"},{"id":29,"name":"nidoran-f","type":"poison","height":4,"weight":70,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/29.png"},{"id":30,"name":"nidorina","type":"poison","height":8,"weight":200,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/30.png"},{"id":31,"name":"nidoqueen","type":"poison","height":13,"weight":600,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/31.png"},{"id":32,"name":"nidoran-m","type":"poison","height":5,"weight":90,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/32.png"},{"id":33,"name":"nidorino","type":"poison","height":9,"weight":195,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/33.png"},{"id":34,"name":"nidoking","type":"poison","height":14,"weight":620,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/34.png"},{"id":35,"name":"clefairy","type":"fairy","height":6,"weight":75,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/35.png"},{"id":36,"name":"clefable","type":"fairy","height":13,"weight":400,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/36.png"},{"id":37,"name":"vulpix","type":"fire","height":6,"weight":99,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/37.png"},{"id":38,"name":"ninetales","type":"fire","height":11,"weight":199,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png"},{"id":39,"name":"jigglypuff","type":"normal","height":5,"weight":55,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png"},{"id":40,"name":"wigglytuff","type":"normal","height":10,"weight":120,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/40.png"},{"id":41,"name":"zubat","type":"poison","height":8,"weight":75,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/41.png"},{"id":42,"name":"golbat","type":"poison","height":16,"weight":550,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/42.png"},{"id":43,"name":"oddish","type":"grass","height":5,"weight":54,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/43.png"},{"id":44,"name":"gloom","type":"grass","height":8,"weight":86,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/44.png"},{"id":45,"name":"vileplume","type":"grass","height":12,"weight":186,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/45.png"},{"id":46,"name":"paras","type":"bug","height":3,"weight":54,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/46.png"},{"id":47,"name":"parasect","type":"bug","height":10,"weight":295,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/47.png"},{"id":48,"name":"venonat","type":"bug","height":10,"weight":300,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/48.png"},{"id":49,"name":"venomoth","type":"bug","height":15,"weight":125,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/49.png"},{"id":50,"name":"diglett","type":"ground","height":2,"weight":8,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/50.png"},{"id":51,"name":"dugtrio","type":"ground","height":7,"weight":333,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/51.png"},{"id":52,"name":"meowth","type":"normal","height":4,"weight":42,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/52.png"},{"id":53,"name":"persian","type":"normal","height":10,"weight":320,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/53.png"},{"id":54,"name":"psyduck","type":"water","height":8,"weight":196,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/54.png"},{"id":55,"name":"golduck","type":"water","height":17,"weight":766,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/55.png"},{"id":56,"name":"mankey","type":"fighting","height":5,"weight":280,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/56.png"},{"id":57,"name":"primeape","type":"fighting","height":10,"weight":320,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/57.png"},{"id":58,"name":"growlithe","type":"fire","height":7,"weight":190,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/58.png"},{"id":59,"name":"arcanine","type":"fire","height":19,"weight":1550,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/59.png"},{"id":60,"name":"poliwag","type":"water","height":6,"weight":124,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/60.png"},{"id":61,"name":"poliwhirl","type":"water","height":10,"weight":200,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/61.png"},{"id":62,"name":"poliwrath","type":"water","height":13,"weight":540,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/62.png"},{"id":63,"name":"abra","type":"psychic","height":9,"weight":195,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/63.png"},{"id":64,"name":"kadabra","type":"psychic","height":13,"weight":565,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/64.png"},{"id":65,"name":"alakazam","type":"psychic","height":15,"weight":480,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png"},{"id":66,"name":"machop","type":"fighting","height":8,"weight":195,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/66.png"},{"id":67,"name":"machoke","type":"fighting","height":15,"weight":705,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/67.png"},{"id":68,"name":"machamp","type":"fighting","height":16,"weight":1300,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/68.png"},{"id":69,"name":"bellsprout","type":"grass","height":7,"weight":40,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/69.png"},{"id":70,"name":"weepinbell","type":"grass","height":10,"weight":64,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/70.png"},{"id":71,"name":"victreebel","type":"grass","height":17,"weight":155,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/71.png"},{"id":72,"name":"tentacool","type":"water","height":9,"weight":455,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/72.png"},{"id":73,"name":"tentacruel","type":"water","height":16,"weight":550,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/73.png"},{"id":74,"name":"geodude","type":"rock","height":4,"weight":200,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/74.png"},{"id":75,"name":"graveler","type":"rock","height":10,"weight":1050,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/75.png"},{"id":76,"name":"golem","type":"rock","height":14,"weight":3000,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/76.png"},{"id":77,"name":"ponyta","type":"fire","height":10,"weight":300,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/77.png"},{"id":78,"name":"rapidash","type":"fire","height":17,"weight":950,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/78.png"},{"id":79,"name":"slowpoke","type":"water","height":12,"weight":360,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/79.png"},{"id":80,"name":"slowbro","type":"water","height":16,"weight":785,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/80.png"},{"id":81,"name":"magnemite","type":"electric","height":3,"weight":60,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/81.png"},{"id":82,"name":"magneton","type":"electric","height":10,"weight":600,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/82.png"},{"id":83,"name":"farfetchd","type":"normal","height":8,"weight":150,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/83.png"},{"id":84,"name":"doduo","type":"normal","height":14,"weight":392,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/84.png"},{"id":85,"name":"dodrio","type":"normal","height":18,"weight":852,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/85.png"},{"id":86,"name":"seel","type":"water","height":11,"weight":900,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/86.png"},{"id":87,"name":"dewgong","type":"water","height":17,"weight":1200,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/87.png"},{"id":88,"name":"grimer","type":"poison","height":9,"weight":300,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/88.png"},{"id":89,"name":"muk","type":"poison","height":12,"weight":300,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/89.png"},{"id":90,"name":"shellder","type":"water","height":3,"weight":40,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/90.png"},{"id":91,"name":"cloyster","type":"water","height":15,"weight":1325,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/91.png"},{"id":92,"name":"gastly","type":"ghost","height":13,"weight":1,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/92.png"},{"id":93,"name":"haunter","type":"ghost","height":16,"weight":1,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/93.png"},{"id":94,"name":"gengar","type":"ghost","height":15,"weight":405,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png"},{"id":95,"name":"onix","type":"rock","height":88,"weight":2100,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/95.png"},{"id":96,"name":"drowzee","type":"psychic","height":10,"weight":324,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/96.png"},{"id":97,"name":"hypno","type":"psychic","height":16,"weight":756,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/97.png"},{"id":98,"name":"krabby","type":"water","height":4,"weight":65,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/98.png"},{"id":99,"name":"kingler","type":"water","height":13,"weight":600,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/99.png"},{"id":100,"name":"voltorb","type":"electric","height":5,"weight":104,"image_url":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/100.png"}]
# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="Pokemon",
    user="postgres",
    password="pongal@546",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Get type IDs from pokemon_type
cursor.execute("SELECT id, type_name FROM pokemon_type;")
type_mapping = {type_name: type_id for type_id, type_name in cursor.fetchall()}

# Insert Pokémon data
for pokemon in pokemon_data:
    cursor.execute(
        """
        INSERT INTO pokemon (id, name, type_id, height, weight, image_url)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
        """,
        (
            pokemon["id"],
            pokemon["name"],
            type_mapping[pokemon["type"]],
            pokemon["height"],
            pokemon["weight"],
            pokemon["image_url"],
        )
    )

# Commit and close
conn.commit()
cursor.close()
conn.close()
print("Data inserted successfully!")
