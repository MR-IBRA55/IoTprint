from datetime import datetime
from typing import List

from bson import ObjectId
from mongoengine import DateField, Document, ObjectIdField, StringField


class SketchModel(Document):
    _id = ObjectIdField(primary_key=True, default=ObjectId)
    display_name = StringField(required=True, max_length=32)
    filename = StringField(required=True)
    date = DateField(required=True, default=datetime.utcnow)
    meta = {"collection": "sketches"}

    @classmethod
    def add_sketch(cls, **kwargs):
        SketchModel(**kwargs).save()

    @classmethod
    def get_all_sketches(cls) -> List:
        sketches = []
        for sketch in SketchModel.objects():
            sketches.append(sketch)
        return sketches

    @classmethod
    def get_sketch_by_filename(cls):
        pass
