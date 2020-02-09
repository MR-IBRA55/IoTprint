from flask import request, jsonify
from flask_restful import Resource
from marshmallow import ValidationError

from app.libs.file_handler import FileHandler
from app.models.sketch_model import SketchModel
from app.schemas import SketchSchema


class SketchUpload(Resource):
    def post(self):
        try:
            if "file" not in request.files:
                return {"msg": "Bad request"}, 400
            file = request.files["file"]
            if file.filename == "":
                return {"msg": "No file selected "}, 400
            if file and FileHandler.allowed_file(file.filename):
                random_name = FileHandler.random_name_gen()
                requested_data = {
                    "display_name": request.form["display_name"],
                    "filename": random_name
                    }
                sketch_schema = SketchSchema()
                result = sketch_schema.load(requested_data)
                SketchModel.add_sketch(**result)
                FileHandler.save_file(file, random_name)
                return {"msg": "Upload successful"}, 200
        except ValidationError as err:
            return jsonify(err.messages)
        return {"msg": "Bad request"}, 400
