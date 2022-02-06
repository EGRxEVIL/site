import flask
import data

app = flask.Flask(__name__)


@app.route("/")
def start():
    return flask.render_template("index.html")


@app.route("/departures/<departure>/")
def depart_page(departure):
    print(departure)
    return flask.render_template("departure.html")


@app.route("/tours/<int:id>/")
def tour_page(id):
    print(id)
    return flask.render_template("tour.html")


@app.route("/data")
def data_page():
    total_info = ""
    for el in data.tours:
        total_info = total_info + f'<p>{data.tours[el]["country"]}: <a href="/data/tours/{el}/">{data.tours[el]["title"]} {data.tours[el]["price"]} {data.tours[el]["stars"]}* </a></p>\n'
    return flask.render_template("all_tours.html", info=data.tours, title=data.title)


@app.route("/data/departures/<departure>")
def data_depart_page(departure):
    total_info = f'<h1>Туры по направлению {data.departures[departure][2:]}:</h1>\n'
    for el in data.tours:
        if data.tours[el]["departure"] == departure:
            total_info = total_info + f'<p>{data.tours[el]["country"]}: <a href="/tours/{el}/">{data.tours[el]["title"]} {data.tours[el]["price"]} {data.tours[el]["stars"]}* </a></p>'
    return flask.render_template("data_depart.html", info=total_info, title=data.title, description=data.description)


@app.route("/data/tours/<int:id>/")
def data_tour_page(id):
    if data.tours.get(id)== None:
        flask.abort(404)
    else:
        total_info = (
            f"<h1>{data.tours[id]['country']}: {data.tours[id]['title']} {data.tours[id]['price']}:</h1>"
            f"<p>{data.tours[id]['nights']} ночей</p>"
            f"<p>Стоимость: {data.tours[id]['price']} Р</p>"
            f"<p>{data.tours[id]['description']}</p>"
        )
        anus = 1337
        return flask.render_template("data_tours.html", info=total_info, title=data.title, anus=anus)

"""
    <h1>Куба: Marina Lake Hotel & Spa 62000:</h1>
    <p>6 ночей</p>
    <p>Стоимость: 62000 Р</p>
    <p>Отель выглядит уютно. Он был построен из красного соснового дерева и украшен синими камнями. Высокие округлые окна добавляют общий стиль дома и были добавлены в дом в довольно симметричном образце.</p>
"""


@app.route('/anus')
def anus_page():
    return flask.render_template("anus.html")

@app.route('/test')
def test_page():
    descript = "You stand in a flat area spotted with trees, shrubs, and small grass. You can see a small body of water to the north and a city to the north. The temperature is somewhat warm and the sky is partially cloudy."
    links = ["/test", "/anus", "/data", "http://127.0.0.1:5000/tours", 'http://127.0.0.1:5000/departure']
    return flask.render_template("test page.html", links=links)



if __name__ == '__main__':
    app.run()