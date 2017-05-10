# Misha Ivkov
# Information Theory
# 21 April 2017

print "Please wait for initialization to finish.\n"

wordlist={}
with open("words.txt","r") as f:
    for line in f:
        line = line[0:len(line)-1].lower()
        if line.isalpha():
            wordlist[line]=0
with open("words2.txt","r") as f:
    for line in f:
        line = line[0:len(line) - 1].lower()
        if line.isalpha():
            wordlist[line]=0
with open("words3.txt","r") as f:
    for line in f:
        line = line[0:len(line) - 1].lower()
        if line.isalpha():
            wordlist[line]=0

with open("occurrences.txt","r") as f:
    for line in f:
        tup = line.split(' ')
        wordlist[str(tup[0])]+=int(tup[1])
with open("occurrences2.txt","r") as f:
    for line in f:
        tup = line.split(' ')
        wordlist[str(tup[0])]+=int(tup[1])
with open("occurrences3.txt","r") as f:
    for line in f:
        tup = line.split(' ')
        wordlist[str(tup[0])]+=int(tup[1])
with open("occurrences4.txt","r") as f:
    for line in f:
        tup = line.split(' ')
        wordlist[str(tup[0])]+=int(tup[1])
with open("occurrences5.txt","r") as f:
    for line in f:
        tup = line.split(' ')
        wordlist[str(tup[0])]+=int(tup[1])

allowed = ['a','i','o','u']
for word in wordlist.keys():
    if len(word)==1 and word not in allowed:
        wordlist.pop(word)

print 'Initialization done\n'


def makeGuess(letter,man):
    for i in xrange(0,len(man)):
        unk[man[i] - 1] = letter
    return

def done():
    for char in unk:
        if char=='.':
            return False
    return True

def majority():
    newunk = ''.join(unk).split(" ")
    majoryikes = ['' for i in xrange(len(newunk))]
    workingwords = [{} for i in xrange(len(newunk))]
    sl = [0 for i in xrange(len(newunk))]
    l = [0 for i in xrange(len(newunk))]
    for word in wordlist:
        for i in xrange(len(newunk)):
            if matches(word,newunk[i]):
                if len(newunk[i])==len(word):
                    workingwords[i][word]=wordlist[word]
                    if wordlist[word] > l[i]:
                        sl[i] = l[i]
                        l[i] = wordlist[word]
                        majoryikes[i] = word
                    elif wordlist[word] < l[i] and wordlist[word] > sl[i]:
                        sl[i] = wordlist[word]
    print [[majoryikes[i], l[i]] for i in xrange(len(newunk))]
    for i in xrange(len(newunk)):
        if sl[i]==0:
            continue
        if l[i] / sl[i] < 20:
            return 0
    if ' '.join(majoryikes) in guessedphrases:
        return 0
    return majoryikes



def matches(word,string):
    if len(word)!=len(string):
        return False
    for i in xrange(len(word)):
        if string[i] == '.':
            if guessed[ord(word[i])-97]:
                return False
            continue
        if word[i]!=string[i]:
            return False
    return True

def changeDict():
    newunk = ''.join(unk).split(" ")
    lens = [len(newunk[i]) for i in xrange(len(newunk))]
    keys = wordlist.keys()
    for word in wordlist.keys():
        if len(word) not in lens:
            wordlist.pop(word)
            i = 0
            continue
        match = False
        for string in newunk:
            match = match or matches(word,string)
        if not match:
            wordlist.pop(word)
            i = 0
            continue
    print "dictionary size is " + str(len(wordlist))
    if len(wordlist) < 100:
        print wordlist


n = int(raw_input("How many characters are in this phrase?\n"))
global unk
unk = ['.' for i in xrange(n)]

print "Guess #1: Is there a blank?"
l = str(raw_input()).split(', ')
man = [int(k) for k in l[1:]]
makeGuess(" ",man)
freq = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guessed = [False for i in xrange(26)]
guesses = [1,0]
guessedphrases = []

def findNext(unk):
    changeDict()
    newunk = ''.join(unk).split(" ")
    freqlist=[0 for i in xrange(26)]
    yike = majority()
    if yike != 0:
        print 'Guess #' + str(guesses[0] + 1) + ": is the phrase " + ' '.join(yike) + '?'
        s = str(raw_input())
        if s=='Y':
            finalyay = ' '.join(yike)
            for i in xrange(len(unk)):
                unk[i] = finalyay[i]
            guesses[0] +=1
        else:
            guessedphrases.append(' '.join(yike))
            guesses[0] +=3
            guesses[1] +=3
        return

    for word in wordlist:
        for char in word:
            freqlist[ord(char)-97]+=wordlist[word]
    maxvalue = -1
    maxind = -1
    #print freqlist
    for i in xrange(26):
        if guessed[i]:
            continue
        if freqlist[i]>maxvalue:
            maxvalue = freqlist[i]
            maxind = i
    print "Guess #"+str(guesses[0]+1)+": Is there a "+freq[maxind].upper()+"?"
    l = str(raw_input()).split(', ')
    if l[0]=='Y':
        man = [int(k) for k in l[1:]]
        makeGuess(freq[maxind],man)
    guessed[maxind]=True
    # print guessed
    oldunk = newunk
    newunk = ''.join(unk).split(" ")
    guesses[0]+=1
    if oldunk == newunk:
        guesses[1]+=1
    print newunk
    return
while not done():
    findNext(unk)
print 'Total number of guesses is ' + str(guesses[0])
print 'Number of incorrect guesses is ' + str(guesses[1])
print 'The phrase is ' + ''.join(unk)