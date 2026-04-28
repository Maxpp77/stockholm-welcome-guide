from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def get_sample_flights():
    return [
        {
            "flightNumber": "SK1234",
            "airline": "SAS Scandinavian Airlines",
            "origin": "London (LHR)",
            "scheduledTime": "07:45",
            "estimatedTime": "07:52",
            "status": "Landed",
            "gate": "F12",
            "terminal": "Terminal 5"
        },
        {
            "flightNumber": "DY4567",
            "airline": "Norwegian Air",
            "origin": "Oslo (OSL)",
            "scheduledTime": "08:10",
            "estimatedTime": "08:08",
            "status": "On time",
            "gate": "E18",
            "terminal": "Terminal 5"
        },
        {
            "flightNumber": "BA8901",
            "airline": "British Airways",
            "origin": "Manchester (MAN)",
            "scheduledTime": "08:30",
            "estimatedTime": "08:45",
            "status": "Delayed",
            "gate": "F05",
            "terminal": "Terminal 5"
        },
        {
            "flightNumber": "FR6723",
            "airline": "Ryanair",
            "origin": "Dublin (DUB)",
            "scheduledTime": "09:00",
            "estimatedTime": "09:00",
            "status": "On time",
            "gate": "G22",
            "terminal": "Terminal 4"
        }
    ]

def get_weather_info():
    return {
        "temperature": "8°C",
        "condition": "Partly Cloudy",
        "advice": "It's cool outside. Bring a light jacket and comfortable shoes for walking in the city."
    }

@app.route("/")
def index():
    arrivals = get_sample_flights()
    weather = get_weather_info()
    current_time = datetime.now().strftime("%H:%M")

    return render_template("index.html", 
                           arrivals=arrivals, 
                           weather=weather,
                           current_time=current_time)

if __name__ == "__main__":
    app.run(debug=True)