# cmsproject

cmsproject is a content management system that allows users to create, view, edit, and delete content. 
It includes two types of user roles, admin and author, and allows users to search content by matching terms in title, body, summary, and categories.


Installation


git clone https://github.com/akshaytp103/cmsproject.git

pip install -r requirements.txt

python manage.py migrate


Usage
python manage.py runserver

http://localhost:8000/admin/

http://localhost:8000/register/

http://localhost:8000/api/content/
