from datetime import datetime
from typing import List

from bson import ObjectId
from mongoengine import Document, ObjectIdField, StringField, DateTimeField


class SketchModel(Document):
    _id = ObjectIdField(primary_key=True, default=ObjectId)
    display_name = StringField(required=True, max_length=32)
    filename = StringField(required=True)
    date = DateTimeField(required=True, default=datetime.utcnow)
    meta = {"collection": "sketches"}

    @classmethod
    def add_sketch(cls, **kwargs) -> "SketchModel":
        return SketchModel(**kwargs).save()

    @classmethod
    def get_all_sketches(cls) -> List:
        sketches = SketchModel.objects()
        return sketches

    @classmethod
    def get_sketch_by_id(cls, _id):
        for sketch in SketchModel.objects(_id=_id):
            return sketch
