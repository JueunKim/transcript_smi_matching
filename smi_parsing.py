# -*- coding: utf-8 -*-
# Remove unnecessary lines and appended <br> tag.
# write it to new smi.file
import sys

def main():

    # Encoding Unicode to UTF-8
    reload(sys)
    sys.setdefaultencoding("utf-8")

    input_file_name = "friends.smi"
    output_file_name = "smi_cleaning.txt"

    # Output file
    f_out = open(output_file_name, 'w')

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
                    f_out.write(line)
                    continue
                if line.startswith('-'):
                    line = "\n"+ lines[idx + 1] + "\n" + lines[idx - 2] + "\n" + line.replace("-", "<p class=KRCC>")
                    # f_out.write(line)
                    print line
                    # print lines[idx - 2]
                    # print lines[idx - 1]
                    # print line
                    # print lines[idx + 1]
                    print "========="
            f_out.write(line + '\r\n')


    f_in.close()
    f_out.close()

if __name__ == "__main__":
	main()