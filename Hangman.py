# Misha Ivkov
# Information Theory
# 29 March 2017

wordlist=[]
with open("words.txt","r") as f:
    for line in f:
        line = line[0:len(line)-1].lower()
        if line.isalpha():
            wordlist.append(line)
with open("words2.txt","r") as f:
    for line in f:
        line = line[0:len(line) - 1].lower()
        if line.isalpha():
            wordlist.append(line)
with open("words3.txt","r") as f:
    for line in f:
        line = line[0:len(line) - 1].lower()
        if line.isalpha():
            wordlist.append(line)


s = str(raw_input())
unk = ['.' for char in s]

def makeGuess(letter):
    for i in xrange(0,len(s)):
        if s[i]==letter:
            unk[i]=letter
    return

def done():
    for char in unk:
        if char=='.':
            return False
    return True

makeGuess(" ")
freq = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guessed = [False for i in xrange(26)]
def findNext():
    newunk = ''.join(unk).split(" ")
    freqlist=[0 for i in xrange(26)]
    for guess in newunk:
        flag1 = False
        for char in guess:
            if char=='.':
                flag1=True
        if not flag1:
            continue
        for word in wordlist:
            if len(word) != len(guess):
                continue
            flag = False
            for i in xrange(0,len(word)):
                if guess[i]=='.':
                    continue
                if guess[i]!=word[i]:
                    flag = True
            if flag:
                continue
            for char in word:
                freqlist[ord(char)-97]+=1
    maxvalue = -1
    maxind = -1
    for i in xrange(26):
        if guessed[i]:
            continue
        if freqlist[i]>maxvalue:
            maxvalue = freqlist[i]
            maxind = i
    makeGuess(freq[maxind])
    guessed[maxind]=True
    newunk = ''.join(unk).split(" ")
    print newunk
    return
while not done():
    findNext()
