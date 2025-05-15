class animal():
    def __init__(self,nome,cor):
        self.name=nome
        self.color=cor

    def comer(self,comida="Ração"):
        print(f"{self.name} está comendo {comida}")

    def interagir(self): #abstrato
        self

class cow(animal):
    def __init__(self,nome,cor,leiteira=True):
        super().__init__(nome,cor)
        self.milk=leiteira
        self.milkStatus=""
        if leiteira:
            self.milkStatus="leiteira "
    def interagir(self):
        print(f"A vaca {self.milkStatus}{self.name} disse: MUUUUUUUU")


class dog(animal):
    def __init__(self,nome,cor,raca):
        super().__init__(nome,cor)
        self.race=raca

    def interagir(self):
        print(f"cachorro {self.name} da raça {self.race} fez auauauauuauauauuuuuuuu")

class cat(animal):
    def __init__(self,nome,cor,raca):
        super().__init__(nome,cor)
        self.race=raca
    def interagir(self):
        print(f"Gato {self.name} da raça {self.race} fez miauuuuu")


class Pessoa():
    def __init__(self,name,weight,age):
        self.nome=name
        self.peso=weight
        self.idade=age
        self.statusDormindo=False
        self.statusComendo=False
        self.statusFalando=False
        self.statusApresentando=False
        self.statusAtividade=""

    def apresentar(self):
        if self.statusApresentando==True:
            print(f"{self.nome} já está se apresentando")
        elif self.statusDormindo or self.statusFalando or self.statusComendo:
            print(f"{self.nome} não conseguiu, porque está {self.statusAtividade}")
        else:
            self.statusApresentando=True
            self.statusAtividade= " se apresentando "
            print(f"Olá, meu nome é {self.nome}, "
                  f"tenho {self.idade} anos, e "
                  f"peso {self.peso} kg")

    def comer(self,comida="Feijão"):
        if self.statusComendo==True:
            print(f"{self.nome} já está comendo")
        elif self.statusDormindo or self.statusFalando or self.statusApresentando:
            print(f"{self.nome} não conseguiu, porque está {self.statusAtividade}")
        else:
            self.statusComendo=True
            print(f"{self.nome} está comendo {comida}")
            self.statusAtividade = " comendo "

    def falar(self):
        if self.statusFalando==True:
            print(f"{self.nome} já está falando")
        elif self.statusDormindo or self.statusComendo or self.statusApresentando:
            print(f"{self.nome} não conseguiu, porque está {self.statusAtividade}")
        else:
            self.statusFalando = True
            print(f"{self.nome} está falando sobre sua idade"
                  f" ({self.idade} anos)")
            self.statusAtividade = " falando "
    def dormir(self):
        if self.statusDormindo==True:
            print(f"{self.nome} já está dormindo")
        elif self.statusComendo or self.statusFalando or self.statusApresentando:
            print(f"{self.nome} não conseguiu, porque está {self.statusAtividade}")
        else:
            self.statusDormindo = True
            print(f"{self.nome} foi dormir.")
            self.statusAtividade = " dormindo "


class passagem():
    def __init__(self,preco,quantidade,is_vip=False):
        self.price=preco
        self.quantity=quantidade
        self.vip=is_vip
        self.finalprice = self.price
        self.vipStatus=""
        if self.vip:
            self.vipStatus="Vip "
    def printValue(self):
        if self.vip:
            self.finalprice=self.price*1.5
        self.valor = self.finalprice * self.quantity
        print(f"O valor total dos {self.quantity} ingressos {self.vipStatus}foi R$ {self.valor}")
        
class passagemVip(passagem):
    def __init__(self,preco,quantidade):
        super().__init__(preco,quantidade,is_vip=True)


class forma():
    def __init__(self):
        self.area=0
        self.perimetro=0

    def calculoArea(self):
        pass

    def calculoPerimetro(self):
        pass

class triangulo(forma):
    def __init__(self,base,altura,lado):
        super().__init__()
        self.base=base
        self.altura=altura
        self.lado=lado

    def calculoArea(self):
        self.area= (self.base*self.altura)/2
        print(f"A área do triangulo é: {self.area}")

    def calculoPerimetro(self):
        self.perimetro= 3*self.lado
        print(f"O perimetro do triangulo é: {self.perimetro}")

class retangulo(forma):
    def __init__(self,base,altura):
        super().__init__()
        self.base=base
        self.altura=altura

    def calculoArea(self):
        self.area=self.base*self.altura
        print(f"A área do retangulo é: {self.area}")

    def calculoPerimetro(self):
        self.perimetro= 2 * (self.base + self.perimetro)
        print(f"O perimetro do retangulo é: {self.perimetro}")




