import os

from config import Configs
from flask import jsonify, send_from_directory
from flask_restful import Resource

UPLOAD_FOLDER = Configs.UPLOAD_FOLDER


class AllFiles(Resource):
    def get(self):
        """List file names on the server as JSON"""
        files = []
        for filename in os.listdir(UPLOAD_FOLDER):
            path = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.isfile(path):
                files.append(filename)
        return jsonify(files)  # return JSON file names


class DownloadFile(Resource):
    def get(self, filename):
        """Download a file."""
        download = send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
        return download
