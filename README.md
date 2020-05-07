# Flask-Blog-App

My first Flask application. Created using this [tutorial](https://www.youtube.com/watch?v=3mwFC4SHY-Y).<br>
The app contain model for Post. All DB interactions is performed using flask-sqlalchemy.<br>
Front is created using templates with jinja2 and bootstrap 4.<br>

Run:
1. clone the repo
2. create venv `python3 -m venv venv`
3. activate venv `source venv/bin/activate`
4. install requirements `pip install -r requirements.txt`
5. create DB 

  * run python REPL `python`
   
  * import db `from app import db`
   
  * create DB `db.create_all()`
   
  * exit `exit()`
   
6. run `python app.py`
