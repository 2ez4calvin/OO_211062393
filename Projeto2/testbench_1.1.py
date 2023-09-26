from TiposDeFormatos import Ponto,Circulo,Linha,QuatroLinhas


#Teste do objeto Ponto

print(f'Teste do objeto ponto\n')

Ponto1= Ponto(1,5,4)
Ponto1.MostraCoordenada()
Ponto1.ColetaTipo()
Ponto1.ColetaID()

#Teste do objeto Circulo

print(f'\nTeste do objeto circulo\n')

Circulo1= Circulo(2,-3,-3,3)
Circulo1.Area()
Circulo1.ColetaTipo()
Circulo1.ColetaID()

#Teste do objeto Linha

print(f'\nTeste do objeto linha\n')

Linha1= Linha(3,2,4,4,4)
Linha1.CalculaComprimento()
Linha1.ColetaID()
Linha1.ColetaTipo()

#Teste do objeto quadrado

print(f'\nTeste do quadrado na classse QuatroLinhas\n')

Quadrado1 = QuatroLinhas(4,10,10,12,10,10,12,12,12)
Quadrado1.Area()
Quadrado1.ColetaID()
Quadrado1.ColetaTipo()

#Teste do objeto Retangulo

print(f'\nTeste do retangulo na classe QuatroLinhas\n')

Retangulo1 = QuatroLinhas(5,-10,-10,-14,-10,-10,-12,-14,-12)
Retangulo1.Area()
Retangulo1.ColetaID()
Retangulo1.ColetaTipo()
