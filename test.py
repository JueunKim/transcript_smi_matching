
import pickle
from fuzzywuzzy import fuzz

with open("t_sample_80.txt") as t, open("smi_superset.txt",'rb') as s:
    t_content = t.readlines()
    t_content = [y.strip() for y in t_content]
    s_content = pickle.load(s)

for idx, i in enumerate(range(len(t_content))):
    best_score = 0
    t_best = " "
    for j in range(len(s_content)):
        score = fuzz.ratio(t_content[i], s_content[j][0])
        if score > best_score:
            best_score = score
            t_best = j
    print idx
    print "trans :" + t_content[i]
    print "smi: " + s_content[t_best][0]
    print s_content[t_best][1], "- ", s_content[t_best][2]
    print best_score
    print "------------"
