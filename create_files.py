import json
import os
dict_workers = {"worker1":10000, "worker2":40000, "worker3":45000, "worker4":32200, "worker5":100000, "worker6":70000, "worker7":60000, }
path = os.path.join('data', 'workers.json')
with open(path, 'w', encoding='utf-8') as file_workers:
    json.dump(dict_workers, file_workers, ensure_ascii=False, indent=4)
dict_hours_of = {"worker1":8, "worker2":9, "worker3":12, "worker4":4, "worker5":5, "worker6":0, "worker7":8, }
path1 = os.path.join('data', 'hours_of.json')
with open(path1, 'w', encoding='utf-8') as file_hours_of:
    json.dump(dict_hours_of, file_hours_of, ensure_ascii=False, indent=4)