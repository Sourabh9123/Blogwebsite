

echo "Build start"

pip install -r requirements.txt
python 3.9  manage.py collectstatic

echo " build end new"