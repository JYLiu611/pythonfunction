
words=open('CMG.txt')
new=open('145.txt','w')
for line in words:
	if line.startswith(" "):
		try:
			s=float(line)
		except:
			new.write(line)	
			continue
		s=str(round((s*145/135), 2))
		new.write("    "+s+"\n")
	else:
		new.write(line)
words.close()		
new.close()