alphabets = "abcdefghijklmnopqrstuvwxyz"
def decrypt(c, k):
    p = ""
    kpos = []
    for x in k:
        kpos.append(alphabets.find(x))
    i = 0
    for x in c:
      if x==":":
	  p+=":"
      else:
	      if i == len(kpos):
		  i = 0
	      pos = alphabets.find(x.lower()) - kpos[i]
	      if pos < 0:
		  pos = pos + 26
	      p += alphabets[pos].lower()
	      i +=1
      
    return p[:len(c)-1]
print "Listen Deeper for the Key!!"
print "Enter the Key:"
key=raw_input()
f=open("DecodeMe", "r")
contents=f.read()
print decrypt(contents,key)
