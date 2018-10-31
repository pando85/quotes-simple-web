import json
from typing import NewType


Json = NewType('Json', str)


def json_dump(response_json: Json) -> dict:
    if '_id' in response_json:
        del response_json['_id']
    return json.dumps(response_json, ensure_ascii=False)
