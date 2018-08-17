letter_dict={"a":"b","b":"c","c":"d","d":"e","e":"f","f":"g","g":"h","h":"i","i":"j","j":"k","k":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"w","w":"x","x":"y","y":"z","z":"a"}
original_file=open("original",'r').read().split("\n\n")
#print(original_file)
cipher_file=open("cipher","w")
for x in original_file:
	print(x)
	x=x.split()
	for y in x:
		print(y)
		for z in y:
			#print(z)
			z=z.lower()
			#if z in letter_dict:
			print(letter_dict[z])
			cipher_file.write(letter_dict[z])
		cipher_file.write(' ')
	cipher_file.write("\n")

