# import Libraries
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
import requests
import datetime

now = datetime.datetime.now()

# Init objects flask
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Init objects flask_restful
api = Api(app)

# Init objects flask_cors
CORS(app)

# init get data from api
json_data = {}
response = requests.get('https://data.covid19.go.id/public/api/update.json')
json_data = response.json()


@app.route('/')
def all_info():
    # return data
    return jsonify({
        "oke": True,
        "data": {
            "total_positive": json_data["update"]["total"]["jumlah_positif"],
            "total_recovered": json_data["update"]["total"]["jumlah_sembuh"],
            "total_deaths": json_data["update"]["total"]["jumlah_meninggal"],
            "total_active": json_data["update"]["total"]["jumlah_dirawat"],
            "new_positive": json_data["update"]["penambahan"]["jumlah_positif"],
            "new_recovered": json_data["update"]["penambahan"]["jumlah_sembuh"],
            "new_deaths": json_data["update"]["penambahan"]["jumlah_meninggal"],
            "new_active": json_data["update"]["penambahan"]["jumlah_dirawat"]
        },
        "message": "success"
    })


@app.route('/yearly')
def yearly_range():
    # assigned regular string date
    since = request.args.get('since', default=str(now.year), type=str)
    upto = request.args.get('upto', default=str(now.year), type=str)

    year_dict = []
    for x in range(int(since), int(upto)+1):
        year_dict.append(x)

    since_item = [item for item in json_data["update"]
                  ["harian"] if since in item['key_as_string']]
    total_death = sum(item['jumlah_meninggal']['value']
                      for item in since_item)
    total_recovered = sum(item['jumlah_sembuh']['value']
                          for item in since_item)
    total_positive = sum(item['jumlah_positif']['value']
                         for item in since_item)
    total_active = sum(item['jumlah_dirawat']['value']
                       for item in since_item)

    # return data
    return jsonify({
        "oke": True,
        "data": {
            "year": year_dict,
            "positive": total_positive,
            "recovered": total_recovered,
            "deaths": total_death,
            "active": total_active,
        },
        "message": "success"
    })


@app.route('/yearly/<year>')
def by_year(year):
    year = request.args.get('year', default=str(now.year), type=str)

    year_item = [item for item in json_data["update"]
                 ["harian"] if year in item['key_as_string']]
    total_death = sum(item['jumlah_meninggal']['value']
                      for item in year_item)
    total_recovered = sum(item['jumlah_sembuh']['value']
                          for item in year_item)
    total_positive = sum(item['jumlah_positif']['value']
                         for item in year_item)
    total_active = sum(item['jumlah_dirawat']['value']
                       for item in year_item)
    # return data
    return jsonify({
        "oke": True,
        "data": {
            "year": year,
            "positive": total_positive,
            "recovered": total_recovered,
            "deaths": total_death,
            "active": total_active,
        },
        "message": "success"
    })


if __name__ == '__main__':
    app.run(debug=True, port=5005)
