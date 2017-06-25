# transcript, smi word matching.

tt = "C'mon, you're going out with the guy! There's gotta be something wrong with him!"
 = "There's nothing to tell! He's just some guy I work with!"

ss = "You're going out with a guy.There's gotta be something wrong with him."

import string

def compare(s1, s2):
    remove = string.punctuation + string.whitespace
    return s1.translate(None, remove) == s2.translate(None, remove)

def main():
    matching = 0
    for trans in tt.split():
        for smi in ss.split():
            if compare(trans.lower().strip(), smi.lower().strip()):
                matching += 1
                print smi, trans

    unmatching = len(tt.split()) - matching

    print float(matching-unmatching) / float(len(tt.split()))

if __name__ == "__main__":
	main()

tt = "All right Joey, be nice. So does he have a hump? A hump and a hairpiece?"
ss = "All right, Joey, be nice.So does he have a hump and a hair piece?"
