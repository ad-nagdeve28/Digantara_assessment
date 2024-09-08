from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from app.models import Job, db

scheduler = BackgroundScheduler()

def job_function():
    print(f"Job executed at {datetime.now()}")

def schedule_job(job_id, cron_schedule):
    unique_job_id = f"job_{job_id}_{datetime.now().timestamp()}"
    trigger = CronTrigger.from_crontab(cron_schedule)
    job = scheduler.add_job(job_function, trigger, id=unique_job_id, replace_existing=False)
    scheduler.start()

    next_run_time = job.next_run_time
    
    update_next_run(job_id, next_run_time)

def update_next_run(job_id, next_run_time):
    job = Job.query.get(job_id)
    if job:
        job.next_run = next_run_time
        db.session.commit()
