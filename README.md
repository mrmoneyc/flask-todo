flask-todo
==============

Prerequisite
----------
```shell
pip install -r backend/requirements.txt
```


Initial Database
----------
Open MySQL shell:
```sql
CREATE DATABASE todo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
GRANT ALL ON todo.* TO 'todo'@'%' IDENTIFIED BY 'todo';
```

Open interactive Python shell and execute:
```python
from backend.app import db
db.create_all()
```


Usage
----------
```shell
python backend/app.py
```
