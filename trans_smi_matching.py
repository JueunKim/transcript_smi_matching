import pickle
import json
from fuzzywuzzy import fuzz


input_file_name = "t_sample_80.txt"
input_file_name2 = "smi_superset1.txt"
output_file_name = "sample_result_ver_1.txt"

# Output file
f_out = open(output_file_name, 'w')

with open(input_file_name) as t, open(input_file_name2,'rb') as s:
    t_content = t.readlines()
    t_content = [y.strip() for y in t_content]
    s_content = pickle.load(s)
    f_out.write("ver_1.0 \n ===============\n")

for idx, i in enumerate(range(len(t_content))):
    best_score = 0
    t_best = " "
    for j in range(len(s_content)):
        score = fuzz.ratio(t_content[i], s_content[j][0])
        if score > best_score:
            best_score = score
            t_best = j
    f_out.write("%d\n" % idx)
    f_out.write("transcript : " + t_content[i] + "\n")
    f_out.write("smi        :  " + s_content[t_best][0] + "\n")
    f_out.write("%d %d" %(s_content[t_best][1], s_content[t_best][2]))
    f_out.write("\n")
    f_out.write("score : " "%d" % best_score + "\n")
    f_out.write("===================\n")
    # print idx
    # print "transcript :" + t_content[i]
    # print "smi        :" + s_content[t_best][0]
    # print s_content[t_best][1], "- ", s_content[t_best][2]
    # print "score", + best_score
    # print "------------"

f_out.close()
