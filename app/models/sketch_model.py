from typing import Dict
from mongoengine import Document, StringField, DateField

from app import mongo


class SketchModel(Document):
    display_name = StringField(max_length=32, required=True)
    filename = StringField(max_length=32, required=True)
    date = DateField(required=True)

    @classmethod
    def add_sketch(cls, data: Dict) -> None:
        mongo.db.sketches.insert_one(data)

    @classmethod
    def get_all_sketches(cls):
        pass

    @classmethod
    def get_sketch_by_filename(cls):
        pass
