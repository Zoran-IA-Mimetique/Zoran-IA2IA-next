import csv,json
def load_matrix(path="test_matrix.csv"):
    return [r for r in csv.DictReader(open(path,encoding="utf-8"))]
def score():
    rows=load_matrix(); total=0; count=0
    for r in rows:
        if r.get("pass"): total+=1
        count+=1
    return total/count if count else 0
if __name__=="__main__": print(json.dumps({"score":score()},indent=2,ensure_ascii=False))
