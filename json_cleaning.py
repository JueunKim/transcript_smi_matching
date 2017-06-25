# -*- coding: utf-8 -*-
# json data parsing/cleaning.

import json
import re

def main():

    # Output file
    f_out = open('json_cleaning.txt', 'w')

    with open('friends.json', 'r') as json_data:
        data = json.load(json_data)
        for r in data['episodes']:
            for s in r['scenes']:
                for u in s['utterances']:
                    # print u['with_description']['transcript']
                    str = u['with_description']['transcript']

                    # remove (...) or [...] pattern using Regular expression
                    if str.startswith('('):
                        str = re.sub('\(.*?\)','',str)
                    elif str.startswith('['):
                        str = re.sub(r'\[.*?\]','',str)
                    elif str.find('(') != -1:
                        str = re.sub('\(.*?\)','',str)

                    if len(str) > 1 :
                     f_out.write(str + '\r\n')

    f_out.close()

if __name__ == "__main__":
	main()
