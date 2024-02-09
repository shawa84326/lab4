from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

locations = {
    'New York': 'America/New_York',
    'India': 'Asia/Kolkata',
    'Tokyo': 'Asia/Tokyo',
    'London': 'Europe/London'
}

# Define a model for your table
class Timezone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    offset = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    current_time = datetime.utcnow()
    times = {location: current_time.astimezone(pytz.timezone(timezone)) for location, timezone in locations.items()}
    return render_template('index.html', times=times)

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
