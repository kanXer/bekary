echo "BUILD START"
python3.12 -m pip install Django -r requirements.txt
python3.12 manage.py collectstatic --noinput --clear
python3.12 manage.py runserver 0.0.0.0:80
echo "BUILD END"