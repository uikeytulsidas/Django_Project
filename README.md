## 📌 Project Description
Academic Portal is a Django-based web application that allows students and faculty to manage academic records, assignments, and other university-related data.

## 🚀 Features
- User authentication (students, teachers, and admins)
- Course and subject management
- Assignment submissions
- Grades and report generation
- Profile management
  
## 🛠️ Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python (>= 3.x)
- Django (>= 4.x)
- PostgreSQL or SQLite
  
  ###  Step 1: Clone the Repository
 -- git clone https://github.com/your-username/academic-portal.git
 cd myproject

 Step 2: Create & Activate Virtual Environment
 python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Step 3: Install Dependencies****
create requirement.txt file in django_project directory not in project file
 include this in requirement.txt file
Django>=3.2,<4.0
psycopg2>=2.8
python-dotenv>=0.15
requests>=2.25
djangorestframework>=3.12
django-cors-headers>=3.7

pip install -r requirements.txt 


Step 4: Configure Database
Update settings.py with your database credentials (PostgreSQL )

Step 5: Apply Migrations
python manage.py migrate

Step 6: Create Superuser
python manage.py createsuperuser

Step 7: Run the Server
python manage.py runserver , create virtual environment in Django_project directory then used  cd myproject after used  run command python manage.py runserver .
if it is get error then download pip install pillow 

Environment Variables
Create a .env file and add:
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-database-url

Technologies Used
Django
PostgreSQL
Bootstrap (for frontend)

✨ Author
Developed by uikeytulsidas


 
