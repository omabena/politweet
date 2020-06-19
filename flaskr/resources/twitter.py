from flask import (
    flash, g, redirect, render_template, request, url_for, Response
)
from werkzeug.exceptions import abort
from flask_restful import Resource


class TwitterApi(Resource):
    def get(self):
        return Response({'Hello': 'World'},
                        mimetype="application/json", status=200)
