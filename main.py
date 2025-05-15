from Library import *


cachorro1=dog("krypto","Branco","Pastor suiço")
gato1=cat("Neguto","Amarelo","vira-lata")
vaca1=cow("Rosinha", "branca")
vaca2=cow("Alice", "malhada", False)

cachorro1.comer()
cachorro1.interagir()
gato1.interagir()
vaca1.interagir()
vaca2.interagir()

print()

pessoa1=Pessoa("Gustavo",80,26)
pessoa1.comer("Pizza")
pessoa1.dormir()
pessoa1.apresentar()

print()

ticket1=passagem(50.0,2)
ticket2=passagemVip(50.0,2)

ticket1.printValue()
ticket2.printValue()


print()


