#cssCompacteur.py

#####################
#
#
#	UTILISATION
#	python3 fichierCss1 fichierCss2 fichierCss3 ....
#
#####################
import sys
import cssutils
from pprint import pprint


files = sys.argv
files.pop(0)
dct = {}
for file in files:
	#print(file)
	days_file = open(file,'r')
	c = days_file.read()
	css = "".join(c.split()) 
	#print(css)

	sheet = cssutils.parseString(css)

	for rule in sheet:
		selector = rule.selectorText
		styles = rule.style.cssText.split(";")

		if not selector in dct:
			dct[selector] = {}
		for style in styles:
			s = style.split(':')
			s[0] = s[0].strip()
			dct[selector][s[0]] = s[1]

#pprint(dct)
ret = ""
for s in dct:
	ret = ret + s + "{\n"
	for value in dct[s]:
		ret = ret + "\t" + value + ":" + dct[s][value] + ";\n"
	ret = ret + "}\n"

f = open("compacted.css", "w")
f.write(ret)
f.close()

print(ret)	
