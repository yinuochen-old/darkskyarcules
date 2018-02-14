from flask import Flask, render_template, request
import darksky

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def index():
    if request.method == 'POST':
        darksky.getWeather(latitude=0,longitude=0)
    else:
        return render_template("index.html")

@app.route('/weather', methods=['POST'])

def weather():
    if request.method == 'POST':
        latitude = request.form["latitude"]
        longitude = request.form["longitude"]
        days, tempHigh, tempLow = darksky.getWeather(latitude,longitude)
        return render_template("weather.html", days=days, tempHigh=tempHigh, tempLow=tempLow)

if __name__ == "__main__":
    app.run(debug=True)
