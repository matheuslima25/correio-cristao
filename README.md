# Correio Cristão
# Start the project

1. Create python 3 virtualenv
> virtualenv -p python3 correiocristao

2. Activate virtualenv
> cd correiocristao
> . bin/activate

3. Clone repository
> git clone <repo>

4. Go to repository
> cd correiocristao

5. Install libs
> pip install -r requirements.txt

6. Run migrate, to create a local database
> python manage.py migrate

7. Create a superuser
> python manage.py createsuperuser

8. Run test server
> python manage.py runserver