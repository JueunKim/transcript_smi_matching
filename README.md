install

    - https://github.com/seatgeek/fuzzywuzzy
    - pip install fuzzywuzzy

1. smi_cleaning.py
    - input : .smi file
    - output : smi_cleaning.txt
    - remove unnecessary lines and <br> tag from smi file.
    - seperate two conversation in one capture

2. json_cleaning.py
    - read ['transcript'] element from json file.
    - remove unnecessary line. ex) ( ) [ ] pattern

3. smi_superset.py
    - input : smi_cleaning.txt
    - output : smi_superset1.txt (Data structure: [("caption", start_t,end_t),("caption", start_t, end_t)...] )

4.trans_smi_matching.py
    - input : json_cleaning.txt, smi_cleaning.txt
    - fuzzy string matching: https://github.com/seatgeek/fuzzywuzzy
    - output: sample_result_ver_1.txt

5.trans_smi_matching2.py
    - output : sample_result_ver_2.txt
