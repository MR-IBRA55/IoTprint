from mongoengine import Document, StringField, DateField


class SketchModel(Document):
    display_name = StringField(max_length=32, required=True)
    filename = StringField(max_length=32, required=True)
    date = DateField(required=True)

    @classmethod
    def add_sketch(cls):
        pass

    @classmethod
    def get_all_sketches(cls):
        pass

    @classmethod
    def get_sketch_by_filename(cls):
        pass
