symble = "+-*/"

import random

with open("ti.txt","w") as f,open("daan.txt","w") as f2:
	line = ""
	line2 = ""
	for i in range(1,100):
		a = round(random.random()*1000,1)
		b = round(random.random()*100,1)
		s = symble[random.randint(0,3)]
		line  = line+"  {} {} {} =          ".format(a,s,b)
		line2 = line2 + "{} {} {} = {}      ".format(a,s,b,round(eval(str(a)+s+str(b)),3))
		if i%2 == 0 :
			f.writelines(line)
			f.write("\n")
			f2.writelines(line2)
			f2.write("\n")
			line = ""
			line2 = ""
			
