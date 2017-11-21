import random
def keygen(k): 
	# retornar um tuplo (p,s,m,n) em que:
	# p é uma lista de inteiros contendo k inteiros (a chave públicad do algoritmo de knapsacks)
	# s é a lista contendo a chave privada (o knapsack super crescente)
	# m e n são os inteiros referidos no algoritmo
	s,m= genSuperSack(k)
	listOfCP=[]

	i=1
	
	n = random.randint(2, m-1)
	while (not euclid(m,n)==1 and checkN(s,m,n)):
		n = random.randint(2, m-1)
	
	p=genPubKey(s, n, m)

	return (p,s,m,n)




def cipher(msg, p): 
	# que retorna uma lista de inteiros que corresponde ao processo de cifra com a 
	# chave pública p de uma mensagem msg que consiste numa lista de 0s e 1s.
	# Podes supor que o tamanho da lista msg é um multiplo do tamanho dos knapsacks que 
	# constituem as chaves públicas e privadas.
	lenp=len(p)
	cmsg=[]
	ciphered=[]
	for k in range(0,len(msg)//lenp):
		cmsg.append(0)

	for j in range(0,len(cmsg)):
		min_bound=j*lenp
		max_bound=((j+1)*lenp)

		for i in range(min_bound,max_bound):
			#rint(min_bound,max_bound)
			cmsg[j]= cmsg[j]+(msg[i]*p[i%lenp])

	return cmsg




def decipher(msg, s, m, n):
	# que decifra a mensagem msg (supondo que esta é uma lista de inteiros, 
	# como o output do método cipher)
	# s é a chave privada
	# m e n são os inteiros "ingredientes" do algoritmo
	# O método deve retornar uma lista de 0s e 1s, exactamente como o input de cipher.
	dmsg=[]
	inverse=extended_gcd(n,m)%m
	for k in range(0,len(msg)):
		dmsg.append([])
	for i in range(0,len(msg)):
		men=(msg[i]*inverse)%m
		for j in reversed(s):
			toAdd=0
			if(men>=j):
				men-=j
				toAdd=1
			dmsg[i].insert(0,toAdd)



	return dmsg


def checkN(s,m,n):
	lenS=len(s)
	min_bound= lenS-(lenS//2)
	max_bound= lenS+(lenS//2)
	counter=0
	for element in s:
		if(n*element>m):
			counter+=1
	if(counter>min_bound and counter<max_bound):
		return True
	return False


def genSuperSack(k):
	sackList =[random.randint(3,7)]
	iteration = k
	i=5
	summ= sackList[0]
	while(iteration>1):
		summ += random.randint(1,50)
		i= int(summ+(summ//random.randint(2,4)))
		summ+= i
		sackList.append(i)
		iteration-=1
	return sackList , random.randint(summ,(summ+summ//2))



#def listSum(l):
#	returnable=0
#	for i in range(len(l)):
#		returnable += l[i]
#	return returnable



def euclid(a, b):
	while(not (a % b == 0)):
	        a,b=b, (a % b)   
	return b



def xEuclid(d,f):
	x1,x2,x3=1,0,f
	y1,y2,y3=0,1,d
	while True:
		if y3 == 0: return (x3,0)
		if y3 == 1: return (y3,y2)
		q=x3/y3
		x1,x2,x3,y1,y2,y3 = y1,y2,y3,x1-q*y1,x2-q*y2,x3-q*y3



def genPubKey(s, n, m):
	pub =[]
	for element in s:
		pub.append((element*n)%m)
	return pub



def extended_gcd(aa, bb):
    lastremainder, remainder = aa, bb
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastx * (-1 if aa < 0 else 1)




def main():
	for exp in range(5,16):
		k= 2**exp
		print(k)
		p,s,m,n=keygen(k)
		msg=[]
		for i in range(0,random.randint(10,50)*k):
			msg.append(random.randint(0,1))
		msgString = ''.join(str(e) for e in msg)
		cmsg = cipher(msg, p)		
		dmsg=decipher(cmsg,s,m,n)
		flatDmsg=[]
		for sub in dmsg:
			for element in sub:
				flatDmsg.append(element)
		if(msg==flatDmsg):
			print("success")
