

echo "Build start"

pip install -r requirements.txt

echo "Build start collectstatic"
ls -la
python manage.py collectstatic --no-input
echo " build end new"



#  {
#       "src": "/static/(.*)",
#       "dest": "/static/$1"
#     },