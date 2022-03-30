from csv import DictReader

from django.core.management import BaseCommand

from result.models import Students



ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from studentdata.csv into our student mode"

    def handle(self, *args, **options):
        
        print("Loading student  data for student available for result")
        for row in DictReader(open('./studentdata.csv')):
            student=Students()
            student.Sr_No=row["Sr_No"]
            student.Division=row['Division']
            student.RollNO=row["RollNo"]
            student.Name=row['Name']
            student.Accountancy=row['Accountancy']
            student.English=row['English']
            student.Maths=row['Maths']
            student.Economics=row['Economics']
            student.Business_Studies=row['Business_Studies']
            student.Total=row['Total']
            student.Average=row['Average']
            student.Grade=row['Grade']
            student.Result=row['Result']
            
           
            student.save()
