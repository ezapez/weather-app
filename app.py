import requests
import json
from flask import Flask, render_template, request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle

app=Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


assets = Environment(app)
js = Bundle('main.js', output='gen/test.js')
assets.register('js_all', js)


db = SQLAlchemy(app)
# this is the datebase model
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        new_city = request.form.get('city')
        if new_city:
            new_city_obj = City(name=new_city)
            db.session.add(new_city_obj)
            db.session.commit()
    cities = City.query.all()

    url = # this is where you place your api url









    weather_data = []
    Invalid_city = False

    for city in cities:

        r = requests.get(url.format(city.name)).json()

        if requests.get(url.format(city.name)).status_code == 404:
            Invalid_city = True



        else:
            Invalid_city = False
            weather = {
                'city' : city.name,
                'temperature' :  r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                }

    if Invalid_city == True:
        flash("Invalid city")

    weather_data.append(weather)





    return render_template("weather.html", weather_data=weather_data)
