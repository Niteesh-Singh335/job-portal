# Job Portal API

Backend API for Job Portal - Candidates can apply, Recruiters can post jobs.

Tech: Python, Django, DRF, JWT, MySQL

Features:
- JWT Login/Register
- Role based - Candidate / Recruiter
- Job CRUD
- Apply for Job
- Throttling, Pagination & filtering

Run:
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
