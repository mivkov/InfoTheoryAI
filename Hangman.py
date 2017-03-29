# Misha Ivkov
# Information Theory
# 29 March 2017

wordlist=[]
with open("words.txt","r") as f:
    for line in f:
        line = line[0:len(line)-1].lower()
        if line.isalpha():
            wordlist.append(line[0:len(line)-1])
with open("words2.txt","r") as f:
    for line in f:
        line = line[0:len(line) - 1].lower()
        if line.isalpha():
            wordlist.append(line[0:len(line) - 1])
with open("words3.txt","r") as f:
    for line in f:
        line = line[0:len(line) - 1].lower()
        if line.isalpha():
            wordlist.append(line[0:len(line) - 1])


s = str(raw_input())
unk = list(str(raw_input()))

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
freq = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']
guessed = [False for i in xrange(26)]
def findNext():
    newunk = ''.join(unk).split(" ")
    freqlist=[0 for i in xrange(26)]
    for guess in newunk:
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
    maxvalue = 0
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
