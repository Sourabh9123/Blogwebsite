

echo "Build start"

pip install -r requirements.txt
echo "Build start runserver "
python3.9 manage.py runserver
echo "Build start collectstatic"
python3.9 manage.py collectstatic

echo " build end new"



#  {
#       "src": "/static/(.*)",
#       "dest": "/static/$1"
#     },