from django.core.management.base import BaseCommand
from employees.models import Employee, Attendance, Performance, SalaryHistory
from faker import Faker
import random
from datetime import date, timedelta

fake = Faker()

class Command(BaseCommand):
    help = "Generate sample employee data"

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=5)

    def handle(self, *args, **options):
        count = options['count']
        for _ in range(count):
            emp = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                department=fake.job(),
                joining_date=fake.date_between(start_date='-3y', end_date='today'),
                position=fake.job(),
                salary=random.randint(30000, 150000)
            )
            for i in range(5):
                Attendance.objects.create(employee=emp, date=date.today() - timedelta(days=i), status=random.choice(['Present','Absent']))
                Performance.objects.create(employee=emp, rating=random.randint(1,5), review_date=date.today() - timedelta(days=i), comments=fake.sentence())
                SalaryHistory.objects.create(employee=emp, amount=emp.salary, effective_date=date.today() - timedelta(days=i))
        self.stdout.write(self.style.SUCCESS(f'{count} employees created with related data'))
