#mymodule.py
def keygen(k): 
	# retornar um tuplo (p,s,m,n) em que:
	# p é uma lista de inteiros contendo k inteiros (a chave públicad do algoritmo de knapsacks)
	# s é a lista contendo a chave privada (o knapsack super crescente)
	# m e n são os inteiros referidos no algoritmo
	
	s,m= genSuperSack(k)
	listOfCP=[]

	i=1
	while(i<m):
		x=euclid(m,i)
		if(x==1):
			listOfCP.append(i)
		i+=1
	n= calculateCP(listOfCP,s,m)
	print( s, m, n)
	#return (p,s,m,n)




#def cipher(msg, p): 
	# que retorna uma lista de inteiros que corresponde ao processo de cifra com a 
	# chave pública p de uma mensagem msg que consiste numa lista de 0s e 1s.
	# Podes supor que o tamanho da lista msg é um multiplo do tamanho dos knapsacks que 
	# constituem as chaves públicas e privadas.
	


	#return cmsg




#def decipher(msg, s, m, n):
	# que decifra a mensagem msg (supondo que esta é uma lista de inteiros, 
	# como o output do método cipher)
	# s é a chave privada
	# m e n são os inteiros "ingredientes" do algoritmo
	# O método deve retornar uma lista de 0s e 1s, exactamente como o input de cipher.



	#return dmsg


def genSuperSack(k):
	sackList =[1]
	iteration = k
	i=5
	while(iteration>0):
	#for i in range(k,1,summ+k**2):
		summ =listSum(sackList)+5
		i= int(summ+(summ**(1/2)//1))
		sackList.append(i)
		iteration-=1
		#print(sackList , "    with i= ",i,"    and summ= ",summ,"    and summ**(1//2)= ",summ**(1//2))
	summ =listSum(sackList)+5
	return sackList , int(summ+(summ**(1/2)//1))

def listSum(l):
	returnable=0
	for i in range(len(l)):
		returnable += l[i]
	#print (returnable)
	return returnable

def euclid(a, b):
    if a % b == 0:
        return b
    else:
        return euclid(b, a % b)        

def calculateCP(l, sack, m):

	lengthSack=len(sack)//2
	lengthL = len(l)//2 
	while True:
		counter=0
		for element in sack:
			if (l[lengthL]*element > m):
				counter+=1

		if (counter==lengthSack):
			return l[lengthL]
		if (counter>lengthSack):
			lengthL=lengthL-lengthL//2 
		if(counter<lengthSack):
			lengthL=lengthL+(lengthSack-lengthL)//2















def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


if __name__ == '__main__':
	numanuma=15
	wrapped=(keygen,numanuma)







