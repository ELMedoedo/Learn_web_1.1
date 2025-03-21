from flask import Flask, render_template
from weather import weather_by_city

app = Flask(__name__)


@app.route("/")
def index():
    title = "Прогноз Кекесов"  # Создание переменной для шаблона
    weather = weather_by_city("Moscow,Russia")
    return render_template(
        "index.html", page_title=title, weather=weather
    )  # Передаем в шаблон то, что мы присваеваем тут, а именно title и weather_text


if __name__ == "__main__":
    app.run(debug=True)
