# -*- coding: utf-8 -*-

import pickle
import json
from fuzzywuzzy import fuzz


def main():

    input_file_name = "t_sample_80.txt"
    input_file_name2 = "smi_superset1.txt"
    output_file_name = "friends.json"

    # Output file
    f_out = open(output_file_name, 'w')

    with open(input_file_name) as t, open(input_file_name2,'rb') as s:
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
        print "transcript :" + t_content[i]
        print "smi        :" + s_content[t_best][0]
        print s_content[t_best][1], "- ", s_content[t_best][2]
        print "score", + best_score
        print "------------"


    with open('friends.json', 'r') as json_data:
        data = json.load(json_data)
        for r in data['episodes']:
            for s in r['scenes']:
                for u in s['utterances']:
                    # print u['with_description']['transcript']
                    str = u['with_description']['transcript']



                    if len(str) > 1 :
                     f_out.write(str + '\r\n')

    f_out.close()

if __name__ == "__main__":
	main()
