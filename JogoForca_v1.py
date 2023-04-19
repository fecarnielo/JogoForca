# Desenvolvimento Jogo da Forca Versão 1

# Importar pacote random
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpar_tela():
  
  #windows
  if name == 'nt':
    _ = system('cls')
    
  # Mac ou Linux
  else:
    _ = system('clear')

# Função Game
def game():
  
  limpar_tela()
  print('\nBem-vindo(a) ao jogo da forca!')
  print('Adivinhe a palavra abaixo:\n')
  
  # Lista de palavras para o jogo
  palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
  
  # Escolher a palavra de forma aleatória
  palavra = random.choice(palavras)
  
  # Calcular o número de traços para cada letra da palavra - List Comprehension
  letras_descobertas = ['_' for letra in palavra]
  
  # Número de chances - depende do tamanho das palavras
  chances = 6
  
  # Lista vazia para receber as letras erradas
  letras_erradas = []
  
  # Loop enquanto o número de chances for maior do que zero
  while chances > 0:
    
    #Print
    print(' '.join(letras_descobertas))
    print('\nChances restantes:', chances)
    print('Letras erradas:', ' '.join(letras_erradas))
    
    #Tentativa
    tentativa = input('\nDigite uma letra: ').lower()
    
    # Condicional 1
    if tentativa in palavra:
      index = 0
      
      for letra in palavra:
        if tentativa == letra:
          letras_descobertas[index] = letra
        index += 1
    else:
      chances -= 1
      letras_erradas.append(tentativa)
    
    # Condicional 2 se a palavra já está completa
    if '_' not in letras_descobertas:
      print('\nVocê venceu, a palavra é:', palavra)
      break
    
  # Condicional 3
  if '_' in letras_descobertas:
        print('\nVocê perdeu, a palavra era:', palavra)

# Bloco main
if __name__ == '__main__':
  game()
  print('Parabéns! Você está aprendendo programação em Python com a DSA. :\n')
        

    
        
    
    
      
  
