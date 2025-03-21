from flask import Flask, render_template
from weather import weather_by_city

app= Flask(__name__)

@app.route('/')
def index():
    title = "Прогноз погоды" # Создание переменной для шаблона
    weather=weather_by_city("Moscow,Russia")
    if weather:
        weather_text = f"Погода: {weather["temp_C"]}, ощущается как: {weather["FeelsLikeC"]}"  # внутри f строки - Показывание только нескольких ключей из словаря
    else:
        weather_text = "Сервис погоды временно недоступен"
    return render_template("index.html", page_title=title, weather=weather_text) # Передаем в шаблон то, что мы присваеваем тут, а именно title и weather_text


if __name__ == '__main__':
    app.run(debug=True)