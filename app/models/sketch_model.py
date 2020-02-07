from typing import Dict

from app import mongo


class SketchModel:

    @classmethod
    def add_sketch(cls, data: Dict) -> None:
        mongo.db.sketches.insert_one(data)

    @classmethod
    def get_all_sketches(cls):
        pass

    @classmethod
    def get_sketch_by_filename(cls):
        pass
