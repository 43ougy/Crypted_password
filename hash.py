import hashlib
import itertools
import sys

def	sha_convert(hash_string):
	sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
	return sha_signature

key = sys.argv[2]
char = "abcdefghijklmnopqrstuvwxyz"
lenght = 5
verif = False

def	gen_comb(char, lenght):
	for comb in itertools.product(char, repeat=lenght):
		yield ''.join(comb)

def	brute_force(char, lenght):
	for comb in gen_comb(char, lenght):
		if sha_convert(comb) == key:
			break
		#else:
		#	print comb + " ---> " + sha_convert(comb)
	return comb

def	brute_force_dict(dictio):
	with open(dictio) as f:
		while True:
			line = f.readline()
			line = line.strip('\n')
			if not line:
				break
			elif sha_convert(line) == key:
				break
			#else:
			#	print line.strip('\n') + " ---> " + sha_convert(line)
	return line

if sys.argv[1] == "encrypt" and len(sys.argv) == 3:
	print "Your encrypted password is : " + sha_convert(key)

elif sys.argv[1] == "decrypt" and len(sys.argv) == 4:
	comb = brute_force_dict(sys.argv[3])
	if sha_convert(comb) == key:
		print "key : " + key
		print "decrypted key = " + comb + " ---> " + sha_convert(comb)
		verif = True
	if verif == False:
		comb = brute_force(char, lenght)
		if sha_convert(comb) == key:
			print "key : " + key
			print "decrypted key = " + comb + " ---> " + sha_convert(comb)
			verif = True
	if verif == False:
		print "Bad value: no arguments match the key"

else:
	print "av[1] = encrypt/decrypt | av[2] = password/key | av[3] = dictionnary file"
