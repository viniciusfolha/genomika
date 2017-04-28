import random
def lcs_t(s1,s2):
	longest_string = ''
	max_overlap = 0
	maiorS = max(len(s1),len(s2))
	menorS = min(len(s1),len(s2))
	for x in range(menorS,menorS/2,-1):
		if(s1[(len(s1)-x):] == s2[:x]):
			if(x > max_overlap):
				max_overlap = x
				longest_string = s1 + s2[x:]
				break

	for x in range(menorS,menorS/2,-1):
		if(s1[:x] == s2[ (len(s2) - x):]):
			if(max_overlap < x):
				max_overlap = x 
				longest_string = s2 + s1[x:]
				break
	return longest_string




def long_common_sub(s1,s2):
	max_occ = 0
	longest_string = ''
	maiorS = max(len(s1),len(s2))
	menorS = min(len(s1),len(s2))


	for x in range(len(s1)):
		i = 0
		t = x

		while(i < len(s2) and t < len(s1) and s1[t] == s2[i]):
			i+= 1
			t+= 1
			
		if(i > menorS/2 and t == len(s1)):
			max_occ = i;
			longest_string = s1[0:x] + s2
			break;

	for x in range(len(s2)):
		i = 0
		t = x

		while( i < len(s1) and t < len(s2) and s2[t] == s1[i]):
			i+= 1
			t+= 1
		
		if(i > menorS/2 and t == len(s2) and i > max_occ):
			max_occ = i;
			longest_string = s2[0:x] + s1
			break;
	return longest_string

conj = []	
with open("input.txt") as file:
	for line in file:
		conj.append(line.rstrip()) 


aux = ''
count_err = 0
while(len(conj)!= 1 and count_err < 10):
	random_index = random.sample(xrange(0,len(conj)), 2)
	'''s1 = conj[random_index]'''
	s1 = conj[random_index[0]]
	s2 = conj[random_index[1]]
	aux = lcs_t(s1, s2)
	
	if(aux != '' and len(aux) <= (len(s1) + len(s2))):
		del conj[random_index[0]]
		if(random_index[0] > random_index[1]):
			del conj[random_index[1]]
		else:
			del conj[random_index[1] - 1]
		conj.append(aux)
		count_err = 0
	else:
		count_err=+1


file = open("output.txt", "w")



if(len(conj) == 1):
	file.write(conj[0])
else:
	file.write('Nao encontrou uma menor superstring com todos os reads')
file.close()


