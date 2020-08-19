list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]
min_did = list_departments[0]["did"]
for i in range(1, len(list_departments)):
    if list_departments[i]["did"] < list_departments[0]["did"]:
        min_did = list_departments[i]["did"]
print("编号最小的部门是%s" % list_departments[i]["title"])
