#!/usr/bin/python3
"""A unittest for file file_storage.py"""


import unittest
import os
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """unittest class for FileStorage"""
    def setUp(self):
        """Ensures that the file.json is deleted before running any test"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.storage = FileStorage()

    def tearDown(self):
        """Ensures the file.json is deleted after running each test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_file_path(self):
        """Test the file path"""
        self.assertEqual(type(storage._FileStorage__file_path), str)
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_all_method(self):
        """Tests the all() method of FileStorage"""
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)
        all_objs = storage.all()
        self.assertIn(f"{type(obj).__name__}.{obj.id}", all_objs)

    def test_new_method(self):
        """Tests the new() method of FileStorage"""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn(f"{type(obj).__name__}.{obj.id}", all_objs)

    def test_save_method(self):
        """Tests the save() method of FileStoarge"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        file_path = self.storage._FileStorage__file_path
        self.assertTrue(os.path.exists(file_path))

    def test_reload_method(self):
        """Tests the reload() method of FileStorage"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(all_objs, {f"{type(obj).__name__}.{obj.id}": obj})


"""
    def test_save_reload(self):
        all_objs_before = storage.all()
        self.assertEqual(all_objs_before, {})
        my_model = BaseModel()
        my_model.save()
        all_objs_after = storage.all()
        self.assertNotEqual(all_objs_after, {})
"""

if __name__ == "__main__":
    unittest.main()
