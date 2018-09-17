import json


def json_dump(response_json):
    if '_id' in response_json:
        del response_json['_id']
    return json.dumps(response_json, ensure_ascii=False)
