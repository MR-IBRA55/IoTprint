from app.models.sketch_model import SketchModel
from tests.base_test import BaseTest


class SketchTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            data = {"display_name": "Box",
                    "filename": "4f7c298051f8328f3f208f0cd35fb7c5.gcode"}
            sketch = SketchModel.add_sketch(**data)
            sketch = SketchModel.get_sketch_by_id(sketch.id)
            self.assertIsNotNone(sketch)
