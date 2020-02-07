from flask import request
from flask_restful import Resource

from app.libs.file_handler import FileHandler

from app.models.sketch_model import SketchModel


class SketchUpload(Resource):
    def post(self):
        if "file" not in request.files:
            return {"msg": "Bad request"}, 400
        file = request.files["file"]
        if file.filename == "":
            return {"msg": "No file selected "}, 400
        if file and FileHandler.allowed_file(file.filename):
            random_name = FileHandler.save_file(file)
            return {"msg": "Upload successful"}, 200
        return {"msg": "Bad request"}, 400
