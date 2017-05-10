def stringify(x):
     print "length is " + str(len(x))
     blanks = []
     occ = [[] for i in xrange(26)]
     for i in xrange(len(x)):
             if x[i] == ' ':
                     blanks.append(i+1)
             else:
                     occ[ord(x[i])-97].append(str(i+1))
     print blanks
     for i in xrange(26):

         print str(chr(i+97)) + " Y, " + ', '.join(occ[i])
     return

stringify(str(raw_input("Enter a phrase\n")))