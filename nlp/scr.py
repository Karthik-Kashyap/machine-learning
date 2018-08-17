kannada = open("kannadascript","r").read().split()

target=open("finalscript","w")
consonants = {"0xc82":"M","0xc83":"ha","0xc85":"a","0xc86":"aa","0xc87":"i","0xc88":"ii","0xc89":"u","0xc8a":"uu","0xc8b":"R","0xc8c":"L","0xc8e":"e","0xc8f":"ee",
"0xc90":"ai","0xc92":"o","0xc93":"oo","0xc94":"au",
"0xc95":"ka","0xc96":"kha","0xc97":"ga","0xc98":"gha","0xc99":"nga","0xc9a":"ca",
"0xc9b":"cha","0xc9c":"ja","0xc9d":"jha","0xc9e":"nya","0xc9f":"Ta","0xca0":"ttha","0xca1":"Da","0xca2":"ddha",
"0xca3":"Na","0xca4":"ta","0xca5":"tha","0xca6":"da","0xca7":"dha","0xca8":"na","0xcaa":"pa","0xcab":"fha","0xcac":"ba","0xcad":"bha",
"0xcae":"ma","0xcaf":"ya","0xcb0":"ra","0xcb1":"rra","0xcb2":"la","0xcb3":"La","0xcb5":"va","0xcb6":"sha","0xcb7":"Sha",
"0xcb8":"sa","0xcb9":"ha","0xcde":"llla","0xce0":"rr","0xce1":"ll","0xc82":"M",
"0xce6":"0","0xce7":"1","0xce8":"2","0xce9":"3","0xcea":"4","0xceb":"5","0xcec":"6","0xced":"7","0xcee":"8","0xcef":"9",
"0x200d":"","0x2e":".","0x30":"0","0x31":"1","0x32":"2","0x33":"3","0x34":"4","0x35":"5","0x36":"6","0x37":"7","0x38":"8","0x39":"9",}
vowels = {
"0xcbe":"aa","0xcbf":"i","0xcc0":"ii","0xcc1":"u","0xcc2":"uu","0xcc3":"R","0xcc4":"Rr","0xcc6":"e","0xcc7":"ee",
"0xcc8":"ai","0xcca":"o","0xccb":"oc","0xccc":"au","0xccd":""}

for x in range(0,len(kannada)):
	for y in range(0,len(kannada[x])):
		if hex(ord(kannada[x][y])) not in consonants and hex(ord(kannada[x][y])) not in vowels:
			target.write(kannada[x][y])
			continue;
		if hex(ord(kannada[x][y]))=="0xccd":
			continue;
		if hex(ord(kannada[x][y]))=="0x2e":
			target.write(".\n")
			continue
		if y != len(kannada[x])-1:
			if hex(ord(kannada[x][y])) in consonants and hex(ord(kannada[x][y+1])) not in vowels:
				target.write(consonants[hex(ord(kannada[x][y]))])
			elif hex(ord(kannada[x][y])) in consonants and hex(ord(kannada[x][y+1])) in vowels:
					lt=consonants[hex(ord(kannada[x][y]))]
					lt=lt[:-1]
					target.write(lt)
			else:
				target.write(vowels[hex(ord(kannada[x][y]))])
		elif hex(ord(kannada[x][y])) in vowels:
			target.write(vowels[hex(ord(kannada[x][y]))])
		else:
			target.write(consonants[hex(ord(kannada[x][y]))])

	target.write(" ")















