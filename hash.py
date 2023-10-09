import hashlib
import itertools
import sys

#This part manage the number of arguments
if len(sys.argv) < 2 or len(sys.argv) > 4:
	print("av[1] = encrypt/decrypt | av[2] = password/key | av[3] = dictionnary file")
	exit()

if len(sys.argv) > 2:
	key = sys.argv[2]

char = "abcdefghijklmnopqrstuvwxyz" #You can add some char if you want a better range
verif = False

def	sha_convert(hash_string):
	sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
	return sha_signature

def	gen_comb(char, lenght):
	for comb in itertools.product(char, repeat=lenght):
		yield ''.join(comb)

#This part gonna test all letters combination possibilities in a range of 5
def	brute_force(char):
	for lenght in range(1, 6): #You can change the range if you want
		for comb in gen_comb(char, lenght):
			if sha_convert(comb) == key:
				return comb
			#else:
			#	print(comb + " ---> " + sha_convert(comb))

#This part gonna test between 1M password to find which key is equal
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
			#	print(line.strip('\n') + " ---> " + sha_convert(line))
	return line

#This part is to encrypt or decrypt a password
if sys.argv[1] == "encrypt" and len(sys.argv) == 3:
	print("Your encrypted password is : " + sha_convert(key))
	exit()

elif sys.argv[1] == "decrypt" and len(sys.argv) == 4:
	comb = brute_force_dict(sys.argv[3])
	if sha_convert(comb) == key:
		print("key : " + key)
		print("decrypted key = " + comb + " ---> " + sha_convert(comb))
		verif = True

elif sys.argv[1] == "decrypt" and len(sys.argv) == 3:
	comb = brute_force(char)
	if sha_convert(comb) == key:
		print("key : " + key)
		print("decrypted key = " + comb + " ---> " + sha_convert(comb))
		verif = True

else:
	print("av[1] = encrypt/decrypt | av[2] = password/key | av[3] = dictionnary file")
	exit()

if verif == False:
	print("Bad value: no arguments match the key")
