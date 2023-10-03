import json
annotate_path = "./coco2017/annotations/instances_val2017.json"

f = json.load(open(annotate_path))

category = f['categories']


ids_cat = {v['id']: v['name'] for v in category}
cats_ids = {v['name']: v['id'] for v in category}

Person_label = ids_cat[1]
#print(Person_label)