from flask import Flask
from app.database import db, init_db
from app.routes import app_routes  # Import Blueprint from routes.py
from config import config
from apscheduler.schedulers.background import BackgroundScheduler

# Initialize Flask app
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(config)

# Initialize database
db.init_app(app)
with app.app_context():
    init_db()

# Register the Blueprint (app_routes)
app.register_blueprint(app_routes)

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=config.DEBUG)
