from flask import Flask
from helper import pets # helper contains dictionary with pet information

# Creating an instance of the Flask class, passing in __name__, and saving the object to a variable called app

app = Flask(__name__)


# index function returns an HTML
# route() decorator to bind the URL path '/' to the index() function.

@app.route('/')
def index():
    return f"<h1>Adopt a pet!</h1><p>Browse through the links below to find your new furry friend:</p><ul><li><a " \
           f"href=' / animals / dogs'>Dogs</a></li><li><a href=' / animals / cats'>Cats</a></li><li><a href=' / " \
           f"animals / rabbits'>Rabbits</a></li></ul> "


# animal route creates individual pages for each animal type and links them in the bulleted list.

@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f"<h1>List of {pet_type}</h1>"
    html += "<ul>"

    for idx, item in enumerate(pets[pet_type]):
        html += f"""
        <li><a href="/animals/{pet_type}/{idx}">{item['name']}</a></li>
        """
    html += "</ul>"
    return html


# takes you to each pet's profile page
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]

    return f"""
  <h1>{pet['name']}</h1>
  <img src="{pet['url']}"/>
  <p>Description: {pet['description']}</p>
  <ul>
  <li>Breed: {pet['breed']}</li>
  <li>Age: {pet['age']}</li>
  </ul>
  """


if __name__ == '__main__':
    app.run(debug=True)
