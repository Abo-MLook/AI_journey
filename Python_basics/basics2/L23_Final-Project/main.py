from flask import Flask,render_template, request
from weather import get_weather
from waitress import serve
# Flask is a web framework for Python.
# Flask – to create the app.
# render_template – to render HTML pages (not used here yet).
# request – to handle form or URL input from users
# waitress: A production-ready server used instead of the default Flask dev server.




app = Flask(__name__) # This line creates the Flask application.

# Both / and /index will trigger the same function below.
@app.route("/")
@app.route("/index")

def index():
    return render_template("index.html")
@app.route("/weather")

def app_getWeather():
    city = request.args.get('city')
    if not bool(city.strip()):
        city = "Buraidah"

    weather_data = get_weather(city)

    if weather_data["cod"] == "404":
        return render_template(
            "city-not-found.html"
        )

    return render_template(
        "weather.html",
        title=weather_data["name"],
        name=weather_data["name"],
        status=weather_data["weather"][0]["description"],
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


if __name__ == "__main__":
    serve(app,host="0.0.0.0",port=8000)