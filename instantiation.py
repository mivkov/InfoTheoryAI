# Misha Ivkov
# Information Theory
# 21 April 2017


import requests
import time

mini = int(raw_input("Enter the minimum fam: "))
maxi = int(raw_input("Enter the maximum fam: "))
write_file = str(raw_input("Enter the write-to file fam: "))

start = time.time()
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
print 'Time taken to complete step 1 is: ' + str(time.time()-start) + ' seconds.'
start = time.time()
sum = 0
for i in xrange(mini,maxi+1):
    filename = 'http://www.gutenberg.org/cache/epub/'+str(i)+'/pg'+str(i)+'.txt'
    try:
        r = requests.get(filename)
        page = r.text
        load_time = r.elapsed.total_seconds()
        sum += load_time
        words = page.split(' ')
        for word in words:
            if word in wordlist:
                wordlist[word] += 1
        if i%100==mini%100:
            print 'Done '+str(i-mini+1)+' and time taken is '+str(time.time()-start)+ ' seconds and average network load time is '+str(sum/(i-mini+1))+' seconds.'
            with open("temp.txt", "w+") as f:
                keyset = wordlist.keys()
                for key in keyset:
                    f.write(key + ' ' + str(wordlist[key]) + '\n')
            print 'Saved a backup to temp.txt.'
    except Exception:
        print "You Lose"
        continue
print 'Average website load time is: '+str(sum/(maxi-mini+1))+' seconds.'
print 'Time taken to complete step 2 is: ' + str(time.time()-start) + ' seconds.'
start = time.time()
with open(write_file,"w+") as f:
    keyset = wordlist.keys()
    for key in keyset:
        f.write(key+' '+str(wordlist[key])+'\n')
print 'Time taken to complete step 3 is: ' + str(time.time()-start) + ' seconds.'




