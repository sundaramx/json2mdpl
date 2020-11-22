import os
import tempfile

from json2mdpl import convertJson2md


def test_convert():
    infile = os.path.join(os.path.dirname(__file__), '..', 'reports', 'sample.json')
    with tempfile.NamedTemporaryFile() as outfile:
        convertJson2md(infile, './reports/sample.md')


