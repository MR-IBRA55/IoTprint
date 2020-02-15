"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.

"""
import os
from unittest import TestCase
from app import app, db


class BaseTest(TestCase):
    def setUp(self) -> None:
        # Make sure database exist
        app.config['MONGODB_SETTINGS'] = {
            'db': 'tests',
            'host': "127.0.0.1",
            }
        with app.app_context():
            db.init_app(app)
        # Get a test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self) -> None:
        # Database is blank
        with app.app_context():
            db.disconnect()

