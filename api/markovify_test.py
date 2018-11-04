import json
import markovify

from quotes.config import QUOTES_FILE_PATH


path = QUOTES_FILE_PATH
with open(path) as f:
    data = json.load(f)

combined_model = None
for quote in data:
    model = markovify.Text(quote['quote'], retain_original=False)
    if combined_model:
        combined_model = markovify.combine(models=[combined_model, model])
    else:
        combined_model = model

[combined_model.make_sentence(max_overlap_ratio=0.30) for i in range(10)]
