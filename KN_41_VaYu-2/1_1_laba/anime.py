from flask import Flask, render_template
from jikanpy import Jikan

jikan = Jikan()
app = Flask(__name__)

@app.route('/')
def home():
    # Відкриваємо anime ID 54595
    anime_data = jikan.anime(54595)  # Тепер без параметра extension='episodes'
    
    # Показуємо інформацію про епізоди
    a = str()
    for episode in anime_data["episodes"]:  # Взяти список епізодів
        a += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {episode['score']}<p>"
    
    return a

if __name__ == '__main__':
    app.run(debug=True)
