

echo "Build start"

pip install -r requirements.txt

echo "Build start collectstatic"
py manage.py collectstatic --no-inpiut

echo " build end new"



#  {
#       "src": "/static/(.*)",
#       "dest": "/static/$1"
#     },