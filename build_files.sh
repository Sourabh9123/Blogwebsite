

echo "Build start"

pip install -r requirements.txt
echo "Build start collectstatic"
python  manage.py collectstatic

echo " build end new"