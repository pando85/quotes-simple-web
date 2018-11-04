import bson
from typing import NamedTuple


class Quote(NamedTuple):
    id: bson.objectid.ObjectId
    quote: str
    author: str
