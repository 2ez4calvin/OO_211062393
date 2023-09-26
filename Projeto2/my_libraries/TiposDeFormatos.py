import math


class Ponto():

    def __init__(self,id,x,y):

        self._id = id
        self._x = x
        self._y = y

    def Define(self,x,y):
        self._x = x
        self._y = y
    
    def MostraCoordenada(self):
        print(f'O ponto de numero {self._id} é definido pelas coordenadas X = {self._x} e Y = {self._y}') 

    def ColetaTipo(self):
        print(f'O tipo do objeto {self._id} é de um Ponto.')

    def ColetaID(self):
        print(f'O ID do objeto é : {self._id}')



class Circulo(Ponto):

    def __init__(self, id, x, y, raio):

        super().__init__(id,x,y)
        self.raio= raio

    def Define(self,x,y,raio):
        super().__init__(x,y)
        self.raio= raio

    def ColetaTipo(self):
        print(f'O tipo do objeto {self._id} é de um Circulo.')
    
    def ColetaID(self):
        print(f'O ID do objeto é : {self._id}')

    def Area(self):
        area = 3.14 * (self.raio * self.raio)
        print(f'A Area do circulo {self._id} é de : {area}')
        

class Linha():

    def __init__(self,id,x1,x2,y1,y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._id= id


    def Define(self,x1,y1,x2,y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    def ColetaTipo(self):
        print(f'O tipo do objeto {self._id} é uma linha.')

    def ColetaID(self):
        print(f'O ID do objeto é: {self._id}')

    def CalculaComprimento(self):
        comprimento=(((self._x2-self._x1)*(self._x2-self._x1))+((self._y2-self._y1)*(self._y2-self._y1)))**0.5
        print(f'O Comprimento da linha {self._id} é de {comprimento}')

class QuatroLinhas():
    
    def __init__(self,id,x1,y1,x2,y2,x3,y3,x4,y4):
        self._x1=x1
        self._x2=x2
        self._x3=x3
        self._x4=x4
        self._y1=y1
        self._y2=y2
        self._y3=y3
        self._y4=y4
        self._id=id

    def Define(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self._x1=x1
        self._x2=x2
        self._x3=x3
        self._x4=x4
        self._y1=y1
        self._y2=y2
        self._y3=y3
        self._y4=y4
        
    def ColetaID(self):
        print(f'O ID do objeto é {self._id}')

    def ColetaTipo(self):
        base=(((self._x2-self._x1)*(self._x2-self._x1))+((self._y2-self._y1)*(self._y2-self._y1)))**0.5
        altura=(((self._x3-self._x1)*(self._x3-self._x1))+((self._y3-self._y1)*(self._y3-self._y1)))**0.5
        if(base == altura):
            print(f'O Tipo do objeto {self._id} é um quadrado')
        else:
            print(f'O Tipo do objeto {self._id} é um retangulo')

    def Area(self):
        base=(((self._x2-self._x1)*(self._x2-self._x1))+((self._y2-self._y1)*(self._y2-self._y1)))**0.5
        altura=(((self._x3-self._x1)*(self._x3-self._x1))+((self._y3-self._y1)*(self._y3-self._y1)))**0.5
        area=base*altura
        print(f'A Area do objeto {self._id} é de {area}')