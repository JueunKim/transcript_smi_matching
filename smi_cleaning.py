# -*- coding: utf-8 -*-
# Remove unnecessary lines and appended <br> tag.
# write it to new smi.file

import sys
import re
import pickle

def main():

    # Encoding Unicode to UTF-8
    reload(sys)
    sys.setdefaultencoding("utf-8")

    input_file_name = "friends.smi"
    output_file_name = "smi_superset.txt"

    # Output file
    f_out = open(output_file_name, 'w')

    # Initialize list
    myList = []
    myList2 = []

    # Process with opening the input file.
    with open(input_file_name) as f_in:

        # remove blank lines!
        lines = filter(None, (line.rstrip() for line in f_in))

        # remove unnecessary lines and write it to a new file
        for idx, line in enumerate(lines):
            if input_file_name.endswith('.smi'):
                if line.startswith('-->'):
                    continue
                # Merge two lines that were distinguished by a '<br>' tag
                if line.endswith('<br>'):
                    line = line[:-4]
                    line = line + ' '
                    continue
                if line.startswith('-'):
                    line = "\n"+ lines[idx + 1] + "\n" + lines[idx - 2] + "\n" + line.replace("-", "<p class=KRCC>")

            if line.startswith('<p class=KRCC>'):
                trans = re.sub('<.*?>', '', line)
                start_t = int(re.search(r'\d+', lines[idx - 1]).group())
                end_t = int(re.search(r'\d+', lines[idx + 1]).group())
                myTuple = (trans, start_t, end_t)
                myList.append(myTuple)


        # Combine two tuple for making superset ex.) (1,2) (2,3) (3,4).....
        trans, start_t, end_t = zip(*myList)
        for i in range(len(myList)):
            if i == len(myList)-1:
                break;
            else:
                new_trans = trans[i] + trans[i + 1]
                start_tt = int(start_t[i])
                end_tt = int(end_t[i + 1])

                myTuple2 = (new_trans, start_tt, end_tt)
                myList2.append(myTuple2)

        # concatenate two list
        myList = myList + myList2

        with open(output_file_name, 'wb') as fp:
            pickle.dump(myList, fp)

    f_in.close()
    f_out.close()

if __name__ == "__main__":
	main()