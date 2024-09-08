from flask import Blueprint, jsonify, request
from app.models import Job, db
from app.scheduler import schedule_job


app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/jobs', methods=['GET'])
def list_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs])

@app_routes.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job = Job.query.get_or_404(job_id)
    return jsonify(job.to_dict())

@app_routes.route('/jobs', methods=['POST'])
def create_job():
    data = request.get_json()
    job_name = data['name']
    cron_schedule = data['schedule']
    new_job = Job(name=job_name, schedule=cron_schedule)
    db.session.add(new_job)
    db.session.commit()
    schedule_job(job_name, cron_schedule)
    return jsonify(new_job.to_dict()), 201
