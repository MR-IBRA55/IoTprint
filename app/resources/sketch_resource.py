import os
from config import Configs
from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename

from app.models.sketch_model import SketchModel

ALLOWED_EXTENSIONS = {'gcode'}


class SketchAdd(Resource):
    def allowed_file(self, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def post(self):
        if request.method == 'POST':
            if 'file' not in request.files:
                return {"msg": "Bad request"}, 400
        file = request.files['file']
        if file.filename == '':
            return {"msg": "No file selected "}, 400
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(Configs.UPLOAD_FOLDER, filename))
            return {"msg": "Upload successful"}, 200
        return {"msg": "Bad request"}, 400
