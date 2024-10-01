class Bicicleta: #criação da classe bicicleta
    def __init__(self, cor, modelo, ano, valor): #inicializador, self referencia explicita para o objeto.
        self.cor = cor #receber os atributos
        self.modelo = modelo #receber os atributos
        self.ano = ano #receber os atributos
        self.valor = valor #receber os atributos

    def buzinar(self): #método buzinar
        print("Plim plim...")

    def parar(self): #método parar
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self): #método correr
        print("Vrummmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()
