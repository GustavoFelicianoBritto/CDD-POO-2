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

triangulo1=triangulo(5,5,5)
triangulo1.calculoArea()
triangulo1.calculoPerimetro()

retangulo1=retangulo(23,20)
retangulo1.calculoArea()
retangulo1.calculoPerimetro()

print()

ciclista1=ciclista(False,False)

ciclista1.pedalar()
ciclista1.aquecer()
ciclista1.aquecer()
ciclista1.pedalar()
ciclista1.aposentar()
ciclista1.pedalar()
ciclista1.aposentar()

print()
nadador1=nadador(False,False)

nadador1.nadar()
nadador1.aquecer()
nadador1.aquecer()
nadador1.nadar()
nadador1.aquecer()
nadador1.aposentar()
nadador1.nadar()

print()
corredor1=corredor(False,False)

corredor1.correr()
corredor1.correr()
corredor1.aposentar()
corredor1.aquecer()
corredor1.correr()
print()
triatleta1=triatleta(False,False)

triatleta1.correr()
triatleta1.aquecer()
triatleta1.nadar()
triatleta1.correr()
triatleta1.pedalar()
triatleta1.aposentar()
triatleta1.nadar()