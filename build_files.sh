

echo "Build start"

pip install -r requirements.txt

echo "Build start collectstatic"
python3.9 manage.py collectstatic

echo " build end new"



#  {
#       "src": "/static/(.*)",
#       "dest": "/static/$1"
#     },