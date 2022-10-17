# chicken-feeding-system
# Installation:
  pip install requirements.txt

# to start the server:
  python manage.py runserver

# to handle migrations run:
  python manage.py makemigrations
  python manage.py migrate


# To run cron job
  cd feeder
  python worker.py
