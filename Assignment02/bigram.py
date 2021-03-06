from __future__ import division
import string
import sys
# complain if we didn't get a filename
# as a command line argument
if len(sys.argv) < 2:
    print "Please enter the name of a corpus file as a command line argument."
    sys.exit()

# try opening file
# If the file doesn't exist, catch the error
try:
    f = open(sys.argv[1])
except IOError:
    print "Sorry, I could not find the file", sys.argv[1]
    print "Please try again."
    sys.exit()

# read the contents of the whole file into ''filecontents''
filecontents = f.read()

# count bigrams
bigrams = {}
words_punct = filecontents.split()
# strip all punctuation at the beginning and end of words, and
# convert all words to lowercase
words = [ w.strip(" ") for w in words_punct ]

# add special START, END tokens
words = ["START"] + words + ["END"]

for index, word in enumerate(words):
    if index < len(words) - 1:
        # we only look at indices up to the
        # next-to-last word, as this is
        # the last one at which a bigram starts
        w1 = words[index]
        w2 = words[index + 1]
        # bigram is a tuple,
        # like a list, but fixed.
        # Tuples can be keys in a dictionary
        bigram = (w1, w2)

        if bigram in bigrams:
            bigrams[ bigram ] = bigrams[ bigram ] + 1
        else:
            bigrams[ bigram ] = 1

# sort bigrams by their counts
sorted_bigrams = sorted(bigrams.items(), key = lambda pair:pair[1], reverse = True)
total=0
# f1 = open('Bi_try.txt', 'wa')

for bigram, count in sorted_bigrams:
# 	print bigram, ":", count
# 	for x in bigram:
# 		f1.write(x)
# 		f1.write(" ")
# 	f1.write(str(count) + "\n")
     	total+=count

#probability of the bigrams
print total
f2 = open('Bigram_probab.txt', 'wa')
for bigram, count in sorted_bigrams:
    for x in bigram:
        f2.write(x)
        f2.write(" ")
    f2.write(str((count/total)) + "\n")

f.close()
# f1.close()
f2.close()
