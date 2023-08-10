

echo "Build start"

pip install -r requirements.txt
python  manage.py collectstatic

echo " build end new"