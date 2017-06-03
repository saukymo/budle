# -*- coding: utf-8 -*-

from typing import TypeVar, List, Dict
from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS

app = Sanic(__name__)
CORS(app)

app.static('/static', './static')

Request = TypeVar('request')
Response = TypeVar('response')


@app.route("/")
async def main(request: Request) -> Response:
    return json({"hello": "world"})


@app.route("/sample_list")
async def mock_list(request: Request) -> Response:
    response: List[Dist] = [{
        'name': 'Filco',
        'price': '1000',
        'color': 'black'
    }, {
        'name': 'Cherry',
        'price': '880',
        'color': 'white'
    }]
    return json(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
