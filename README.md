# Psicare
## Installation

- Clone or [download](https://github.com/Iah-Uch/psicare/archive/refs/heads/main.zip) this repository;

- Change directory to the projects folder and create a virtual environment;
  - On `\psicare-repo`
    - `python -m venv psicare-env`
    - Activate the venv
      - `.\psicare-env\Scripts\activate`

- Install the dependencies;
  - On `\psicare-repo`
    - `pip install -r .\requirements.txt`

- Setup Environment Variables;

  - On `\psicare-repo\psicare\psicare`

    - Import or create a **.env** file

      - Variables needed for **this project**:

        - **SECRET_KEY**=<Django generated secret key ([not the default](https://humberto.io/blog/tldr-generate-django-secret-key/))>

          **ALLOWED_HOSTS**=<allowed hosts IP's and/or domain name>

          **CSRF_TRUSTED_ORIGINS**=< Trusted request origins full URL or IP>

          **DEBUG**=True (remove this one for production mode)

- Run initial management commands

  - On `\psicare-repo\psicare`
    - Create the database Migrations
      - `python python .\manage.py makemigrations` 
    - Run the Migrations
      - `python .\manage.py migrate`
    - Collect Static Files
      - `python .\manage.py collectstatic --noinput`

- Create a Super User for testing
  - On `\psicare-repo\psicare`
    - ` python .\manage.py createsuperuser` 

- Run the project
  - On `\psicare-repo\psicare`
    - ` python .\manage.py runserver`
- Access the admin panel
  - Go to http://localhost:8000
    - Port may differ if you change it on "runserver" command.
