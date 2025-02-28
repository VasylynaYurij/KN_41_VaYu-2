from flask import Flask, render_template
from jikanpy import Jikan

jikan = Jikan()
app = Flask(__name__)

@app.route('/')
def home():
    anime_data = jikan.anime(54595)  
    
    a = str()
    for episode in anime_data["episodes"]:  
        a += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {episode['score']}<p>"
    
    return a

if __name__ == '__main__':
    app.run(debug=True)
