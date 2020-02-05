from flask import Flask, render_template
import data

app = Flask(__name__)
tours_info = list(data.tours.values())
for i, tour in enumerate(tours_info):
    tour['id'] = i+1

@app.route('/')
def main_page():
    tours_sorted = sorted(tours_info, key=lambda x: int(x['stars']), reverse=True)[:6]
    #print(sorted(tours, key=lambda x: int(x['stars']), reverse=True))
    return render_template("index.html", data=tours_sorted)


@app.route('/from/<direction>')
def directions(direction: str):
    tours_from = [tour for tour in tours_info if tour['departure'] == direction]
    min_price = min(tours_from, key=lambda x: x['price'])['price']
    max_price = max(tours_from, key=lambda x: x['price'])['price']
    min_nights = min(tours_from, key=lambda x: x['nights'])['nights']
    max_nights = max(tours_from, key=lambda x: x['nights'])['nights']
    print(max_nights)
    return render_template("directions.html", dep=data.departures, from_city=direction, tours=tours_from, city_name=data.departures[direction], min_price=min_price, max_price=max_price, min_nights=min_nights, max_nights=max_nights)


@app.route('/tours/<id>')
def tours(id: str):
    return render_template("tour.html", data=data.tours[int(id)], dep=data.departures)


if __name__ == "__main__":
    app.run()
