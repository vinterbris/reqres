import json
import os

from jsonschema import validate

import schemas

SCHEMA_INIT = os.path.abspath(schemas.__file__)
SCHEMA_DIR = os.path.dirname(SCHEMA_INIT)


def get_schema(name):
    return os.path.join(SCHEMA_DIR, name)


def validate_schema(body, schema_name):
    schema = get_schema(schema_name)
    with open(schema) as file:
        validate(body, schema=json.loads(file.read()))
