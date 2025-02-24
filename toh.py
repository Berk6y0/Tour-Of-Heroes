from flask import jsonify,request,Flask # type: ignore
from flask_cors import CORS # type: ignore

app=Flask(__name__)
app.config["DEBUG"]=True
CORS(app)    
    
    
all_heroes = [
      { 'id': 12, 'name': 'Dr. Nice' ,'imageUrl':'https://imgs.search.brave.com/vpS04VvqX_1SELCvVLWoVNY9jrllSJP3GzSF_trb6gw/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9kb3hp/bWl0eS1yZXMuY2xv/dWRpbmFyeS5jb20v/aW1hZ2VzL2ZfYXV0/byxxX2F1dG8sdF9w/dWJsaWNfcHJvZmls/ZV9waG90b18zMjB4/MzIwL3BpM25udXRn/Y3k1eXZkZ3g5N3Z4/L2FudGhvbnktbWlu/aWFjaS1tZC1kZWVy/ZmllbGQtYmVhY2gt/ZmwuanBnP25vaW5k/ZXg9dHJ1ZQ' },
      { 'id': 13, 'name': 'Bombasto' ,'imageUrl':'https://imgs.search.brave.com/GYqTobzQOaZ-r2ugZstU6MyevAZu19KA_bgYw8DkAoo/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5mb3J0bml0ZWFw/aS5pby9pbWFnZXMv/MjEwZDJlNy1lMjQ0/OTJjLTg0ZGY5ZDgt/NzdmYWE1Ny90cmFu/c3BhcmVudC5wbmc' },
      { 'id': 14, 'name': 'Celeritas' ,'imageUrl':'https://imgs.search.brave.com/GsZXOnH_VpSSBFAGJe0beozCUTBo0h4cfcsGmMQZ_OY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNDY4/MzMyNjUyL3Bob3Rv/L3N1cGVyLWhlcm8u/anBnP3M9NjEyeDYx/MiZ3PTAmaz0yMCZj/PS1fWHkwaFdVTXlo/elIwR2NjQTQwMEFy/Ml90YkZOTWJiY3Y3/WThHUVNRSHc9'},
      { 'id': 15, 'name': 'Magneta','imageUrl':'https://imgs.search.brave.com/cfKLhfcKRS-6Ct2v9Ie6PZGM9yWvoaHJ2HmxfmenwR0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTY0/MDAzMzE1L3Bob3Rv/L3N1cGVyaGVyby5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/VWxYNnBsQUlrX3o0/YllTNnZaNHFWZTBF/NDlVU29kNkNqOXcz/TllkWUtTYz0'  },
      { 'id': 16, 'name': 'RubberMan','imageUrl':'https://imgs.search.brave.com/qEPBCL0LqM1LjP7jNRsa90VH4RMivXBZXSMAjA7MImY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL00v/TVY1Qk9ETmxORE5s/WmpBdE5tSTBNeTAw/WW1Nd0xUZzNZekF0/TVRZNU1qbGxOR000/TlRNNFhrRXlYa0Zx/Y0dkZVFYVnlOelUx/TnpFM05UZ0AuanBn' },
      { 'id': 17, 'name': 'Dynama' ,'imageUrl':'https://imgs.search.brave.com/eaNogmBC1M-TvNdJLY5-DBMvr0-yQ-buBeWRvjvJHes/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTYz/NjQwNTA4L3Bob3Rv/L2hlcm8tb2YtdGhl/LWNvcnBvcmF0aW9u/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz0wNklKYkxUQ2xx/VG90U3ZzVGZXTHU4/bVBQN2J0UHZNcUhD/YjE0LUhpbDNnPQ' },
      { 'id': 18, 'name': 'Dr. IQ' ,'imageUrl':'https://imgs.search.brave.com/UXdt7mquRnxd0SQQQ2buoVmHe_Tw99WFScMUQ3UvbBY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/cHJlbWl1bS1waG90/by9odW1hbi1icmFp/bi1pcS13b3JkLTNk/LXJlbmRlcmluZ184/MDgzMzctMTg0NDIu/anBnP3NlbXQ9YWlz/X2h5YnJpZA' },
      { 'id': 19, 'name': 'Magma' ,'imageUrl':'https://imgs.search.brave.com/JBAzjd3-PVBMEu3CV3E6hF9dyYCZ34T7vZmd_5rUoQg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cHJvZC53ZWJzaXRl/LWZpbGVzLmNvbS82/NjAwZTFlYWI5MGRl/MDg5YzJkOWM5Y2Qv/NjcwNTk5NjIyOWM1/ODE0YjA1NzEyZTc0/XzY2ZWU0OWIxNmQ3/ZTFhNjg4MmI2ZTY4/ZF9MQUlud0VsLmpw/ZWc' },
      { 'id': 20, 'name': 'Tornado','imageUrl':'https://imgs.search.brave.com/TV4Yo1V5jXnUPP92ZB1JWGbb7U40ar5a2UNuV4WHs7w/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAyMC8w/Ny8yMC8wNi80Mi9l/bmdsaXNoLWJ1bGxk/b2ctNTQyMjAxOF9f/MzQwLmpwZw'  }
    ]
@app.route('/heroes',methods=['GET'])
def heroes():
     return jsonify(all_heroes)

@app.route('/detail/<id>',methods=['GET'])
def detail(id):
     for x in all_heroes:
          if int(x ['id'])==int(id):
            return jsonify(x)
       
     return "Record not found",400;  
@app.route('/update',methods=['POST'])


def update():
    data = request.data
    string = data.decode('UTF-8')
    data = eval(string)  

    print(data)
    
    for x in all_heroes:
        if x['id'] == data['id']:
            x['name'] =data['name']  
            x['imageUrl']=data['imageUrl']
            return jsonify({"message": "New image changed successfully"}), 200 ,x

    return {"error": "Not found"}, 400  
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    data.setdefault('imageUrl', 'https://imgs.search.brave.com/5cAi-jXDh0PdCGuh2vvsggwMUWvGlmTFmbCQ7jYJ9OI/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzAyLzE1Lzg0LzQz/LzM2MF9GXzIxNTg0/NDMyNV90dFg5WWlJ/SXllYVI3TmU2RWFM/TGpNQW15NEd2UEM2/OS5qcGc')

    new_id = max(hero['id'] for hero in all_heroes) + 1 if all_heroes else 1
    data['id'] = new_id
    
    all_heroes.append(data)
    return jsonify({"message": "Hero added successfully", "hero": data}), 201

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    global all_heroes
    all_heroes = [hero for hero in all_heroes if hero['id'] != id]
    return jsonify({"message": "Hero deleted successfully"}), 200

@app.route('/search/<term>', methods=['GET'])
def search(term):
    term = term.lower()
    matching_heroes = [hero for hero in all_heroes if term in hero['name'].lower()]
    return jsonify(matching_heroes),200


app.run()
