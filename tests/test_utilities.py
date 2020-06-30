from io_.readers.json_reader import JsonReader
from json import JSONDecodeError

import pytest


class TestReaders:
    @pytest.mark.parametrize(
        "path, content",
        [
         ("tests/test_input.json", None),
         ("", None),
         ("non_existent_file", None),
         (123, None)
        ]
    )
    def test_json_reader(self, path, content):
        rdr = JsonReader().read(path)

        assert rdr == content, (
            f"Incorrect content for {path}"
        )


        

class TestWriters:
    
    def test_json_writer(self):
        pass

class TestPreprocess:
    
    def test_validate(self):
        pass

    def test_preprocess(self):
        pass