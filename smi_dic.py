# -*- coding: utf-8 -*-
# input : "smi_cleaning.txt"
# output : data structure -[("smi", start_t,end_t),("smi", start_t, end_t)...]


import re
import pickle


def main():

    input_file_name = "smi_cleaning.txt"
    output_file_name = "smi_superset1.txt"

    # Initialize list
    myList = []
    myList2 = []

    with open(input_file_name) as f:
        s_content = f.readlines()

        # Remove whitespace character
        s_content = [x.strip() for x in s_content]

        for index, line in enumerate(s_content):
            if line.startswith('<p class=KRCC>'):
                # trans = line.strip('<p class=KRCC>')
                trans = re.sub('<.*?>', '', line)
                start_t = int(re.search(r'\d+', s_content[index -1]).group())
                end_t = int(re.search(r'\d+', s_content[index +1]).group())

                myTuple = (trans, start_t, end_t)
                myList.append(myTuple)

        # Combine tuple for making superset ex.) (1,2) (2,3) (3,4).....
        trans, start_t, end_t = zip(*myList)
        for i in range(len(myList)):
            if i == len(myList)-1:
                break;
            else:
                # print((' '.join((trans[i], trans[i+1])), start_t[i], end_t[i + 1]))
                new_trans = trans[i] + trans[i + 1]
                start_tt = int(start_t[i])
                end_tt = int(end_t[i + 1])

                myTuple2 = (new_trans, start_tt, end_tt)
                myList2.append(myTuple2)

        # concatenate two list
        myList = myList + myList2

        with open(output_file_name, 'wb') as fp:
            pickle.dump(myList, fp)

if __name__ == "__main__":
	main()