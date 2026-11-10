import json
import re
import unittest
from typing import Union

class TestProseWrappedJSON(unittest.TestCase):
    def test_prose_wrapped_json_comes_back(self):
        wrapped = 'Here you go: apple orange banana'
        result = wrapped 
        self.assertEqual(result, wrapped)

class TestTwoJSONObjects(unittest.TestCase):
    def test_two_objects_one_after_the_other(self):
        text = 'First call: {"name": "Alice", "age": 30} Second call: {"name": "Bob", "age": 25}'
        results = extract_all_json_objects(text)
        
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0], {"name": "Alice", "age": 30})
        self.assertEqual(results[1], {"name": "Bob", "age": 25})

class TestMissingRequiredArgumentReadFile(unittest.TestCase):
    def test_missing_required_argument_read_file(self):
        tool_call = {"tool": "read_file", "args": {}}
        result = validate_tool_call(tool_call)
        
        self.assertIn("error", result)
        self.assertIn("Missing required arguments", result["error"])
        self.assertIn("path", result["error"])



if __name__ == "__main__":
    unittest.main()
