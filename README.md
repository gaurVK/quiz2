# quiz2
Employee Data Generation &amp; Visualization
Project Structure
quiz2/
├── .env                     # Environment variables
├── manage.py
├── requirements.txt
├── employee_analytics/       # Django project
│   ├── settings.py
│   ├── urls.py
├── employees/               # Employee app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── management/commands/generate_sample_data.py
└── analytics/               # Analytics app

Setup Instructions 
1. Clone the Repository


2. Create Virtual Environment


3. Install Dependencies


4. Configure .env File

Create .env in project root:




Save as UTF-8 encoding without quotes.

5. Apply Migrations


6. Create Superuser


7. Generate Sample Employee Data



Generates 5 employees with attendance, performance, and salary history.

8. Run the Server
python manage.py runserver


Open http://127.0.0.1:8000/swagger/
 for Swagger UI.





GitHub Repository

Make regular commits:

git add .
git commit -m "Initial setup with models, APIs, Swagger, CSV export"
git push origin main


