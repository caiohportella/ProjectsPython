import time

# Bem vindo
nome = input(r"Qual seu nome? ")

print ("Olá, "+ nome +"! Vamos jogar forca!")

print ()

# Espera um segundo
time.sleep(1)

print ("Vamos comecar a adivinhar...")
time.sleep(0.5)

#here we set the secret
palavra = "secret"

# Variável que estoca chutes
chute = ''

# Número de tentativas
tentativas = 10

while tentativas > 0:         

    falhou = 0             

    # Para cada caracter em 'palavra'   
    for carac in palavra:      

    # Verifica se carac está em chute
        if carac in chute:    
            print (carac)    
		else:
    		# Se não achou, imprime _
            print ("_")     
            falhou += 1    

    if falhou == 0:        
        print ("Voce ganhou!")  
        break              

    print()

    # Pede para adivinhar caracter
    chute2 = input(r"Adivinhe uma letra: ") 

    # Define o chute2 para chute
    chute += chute2                   

    # Se chute2 != palavra
    if chute2 not in palavra:  
 	# Contador de tentativas diminui 1 (9)
        tentativas -= 1        
 	 # print wrong
        print ("Errou!") 
 
    # Tentativas restantes
        print ("Voce tem", + tentativas, "tentativas restantes.") 
 
        if tentativas == 0:           
            print ("Voce perdeu!")