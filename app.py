from flask import Flask, render_template

title = "Stepik Travel"
subtitle = "Для тех, кого отвлекают дома"
description = "Лучшие направления, где никто не будет вам мешать сидеть на берегу и изучать программирование, дизайн, разработку игр и управление продуктами"
departures = {"msk":"Из Москвы","spb":"Из Петербурга","nsk":"Из Новосибирска","ekb":"Из Екатеринбурга","kazan":"Из Казани"}

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/from/<direction>')
def directions():
    return render_template("directions.html")


@app.route('/tours/<id>')
def tours():
    return render_template("tour.html")


if __name__ == "__main__":
    app.run()
