from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError

from app.libs.file_handler import FileHandler
from app.models.sketch_model import SketchModel
from app.schemas import SketchSchema


class SketchUpload(Resource):
    def upload_and_save_file(self, file, fullname, display_name):
        requested_data = {
            "display_name": display_name,
            "filename": fullname
            }
        sketch_schema = SketchSchema()
        result = sketch_schema.load(requested_data)
        SketchModel.add_sketch(**result)
        FileHandler.save_file(file, fullname)

    def post(self):
        try:
            if "file" not in request.files or "display_name" not in request.form:
                return {"msg": "Missing data in the request"}, 400
            file = request.files["file"]
            display_name = request.form["display_name"]
            if file.filename == "":
                return {"msg": "No file selected "}, 400
            if file and FileHandler.allowed_file(file.filename):
                fullname = FileHandler.random_name_gen(file.filename)
                self.upload_and_save_file(file, fullname, display_name)
                return {"msg": "Upload successful"}, 200
        except ValidationError as err:
            return jsonify(err.messages)
        return {"msg": "Bad request"}, 400


class Sketches(Resource):
    def get(self):
        sketches = SketchModel.get_all_sketches()
        if sketches:
            sketches_schema = SketchSchema(many=True, only=("display_name", "date"))
            result: dict = sketches_schema.dump(sketches)
            return result, 200
        return {"msg": "No sketches found"}, 404
