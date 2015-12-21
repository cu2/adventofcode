import json
import os
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


def get_doc_sum(doc, ignore_red=False):
    doc_sum = 0
    try:
        keys = doc.keys()
    except AttributeError:
        keys = None
    if keys:
        if ignore_red:
            for key in keys:
                if doc[key] == 'red':
                    return 0
        return sum([get_doc_sum(doc[key], ignore_red) for key in keys])
    if isinstance(doc, list):
        return sum([get_doc_sum(item, ignore_red) for item in doc])
    try:
        return int(doc)
    except ValueError:
        return 0


with open(input_filename, 'r') as f:
    doc = json.load(f)

print get_doc_sum(doc)
print get_doc_sum(doc, ignore_red=True)
