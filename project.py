from __future__ import division
import nltk
from nltk.corpus import stopwords
import operator
import string
import json
import wikipedia

'''
Purpose of this code segment is to cache the proper nouns. This has been executed just once.
Caching for the fact that POS tagging takes north of an hour on the texts

raw = []
raw.append(open('book1.txt').read())
raw.append(open('book2.txt').read())
raw.append(open('book3.txt').read())
raw.append(open('book4.txt').read())


tokens = []
for i in range(4):
	tokens.append(nltk.word_tokenize(raw[i]))
c=0
book = []
temp = []
for i in range(4):
	for j in tokens[i]:
		if j=="BOOK":
			book.append(temp)
			temp=[]
		else:
			temp.append(j)
book.append(temp)
l=[]
book=book[1:]

for i in book:
	l.append(nltk.pos_tag(i))

for x in l:
	print "Rohan Rocks"
	for i in x:
		if i[1]=="NNP":
			print i[0]
'''

with open('pnouns.txt') as f:
	content = f.readlines()

l = []
for i in content:
	l.append(i[0:len(i)-1])

d = []
temp=[]
for i in l:
	if i == "Rohan Rocks":
		d.append(temp)
		temp=[]
	else:
		temp.append(i)

d.append(temp)
temp = []
d=d[1:]

l = d
newl = []
for i in l:
	for j in i:
		j=j.lower()
		temp.append(j)
	newl.append(temp)
	temp=[]

l = newl
newl = []
imp = []
mystop = ['time','left','here','gods','o','indeed','hence','hills','human','kill','hell','heaven','heavens','hells','world','thee','thou','men','women','viz.','thee.','king.','race','come','unto','are.','one.','when']
for i in l:
	for j in i:
		if j not in stopwords.words('english') and j not in mystop and len(j)>=5:
			x = j.translate(None, string.punctuation)
			imp.append(x)
	newl.append(imp)
	imp = []

l = newl
#print l
final_imp = []
vals = []
big = {}
newl = []
for i in l:
	d={}
	store = []
	total=0
	unique = 0
	for j in i:
		d[j]=0
	for j in i:
		d[j]+=1
	sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1))
	sorted_d.reverse()
	for j in sorted_d:
		total+=1
		if big.get(j[0])==None:
			big[j[0]]=j[1]
			unique+=1
			store.append(j[0])
		else:
			big[j[0]]+=j[1]
	temp = unique,total
	vals.append(temp)
	if len(store) >=5:
		newl.append(store[0:5])
	else:
		newl.append(store)
		
print sorted_d
print vals
print newl
big_dumper = []
dumper = []
count = 1
for i in vals:
	dumper.append(dict(time=count,y=i[0]))
	count+=1
big_dumper.append(dumper)
dumper=[]
count = 1
for i in vals:
	dumper.append(dict(time=count,y=i[1]-i[0]))
	count+=1
big_dumper.append(dumper)
dumper=[]
count = 1
for i in vals:
	dumper.append(dict(time=count,y=0))
	count+=1
big_dumper.append(dumper)
'''
with open("final" + ".json",'w') as outfile:
	json.dump(big_dumper, outfile, sort_keys = True, indent = 4, ensure_ascii=False)
'''
for i in newl:
	for j in i:
		print wikipedia.summary(j,sentences = 5)