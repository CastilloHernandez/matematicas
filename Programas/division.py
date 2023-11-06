class Numero:
	def __init__(self, valor):
		self.valor = valor
	def primerosdigitos(self, longitud):
		temp = str(self.valor)[:longitud]
		return int(temp)
	def digito(self, ubicacion):
		temp = str(self.valor)[ubicacion:ubicacion + 1]
		return int(temp)

class Resta:
    def __init__(self, minuendo, sustraendo, indent):
        self.minuendo = minuendo
        self.sustraendo = sustraendo
        self.indent = indent

    def alinear_numeros(self):
        # Encuentra la longitud máxima entre minuendo y sustraendo
        max_length = max(len(str(self.minuendo)), len(str(self.sustraendo)))
        # Convierte los números a cadenas y alinea a la derecha con espacios
        minuendo_str = str(self.minuendo).rjust(max_length)
        sustraendo_str = str(self.sustraendo).rjust(max_length)
        return minuendo_str, sustraendo_str

    def mostrar(self):
        minuendo_str, sustraendo_str = self.alinear_numeros()
        resultado = self.minuendo - self.sustraendo
        resultado_str = str(resultado).rjust(len(minuendo_str))
        max_length = max(len(minuendo_str), len(sustraendo_str))
        print((self.indent - max_length - 1) * ' ' + '~' * (len(minuendo_str) + 1))
        print((self.indent - len(minuendo_str)) *' ' + minuendo_str)
        print((self.indent - len(sustraendo_str) - 1) *' ' +'-' + sustraendo_str)
        print((self.indent - max_length - 1) * ' ' + '-' * (len(minuendo_str) + 1))
        print((self.indent - max_length) * ' ' + resultado_str)
        
    def resultado(self):
    	return int(self.minuendo - self.sustraendo)
	
def division_con_procedimiento(dividendo, divisor):
	#salir = False
	restas = []
	digitoacarreo = len(str(divisor.valor)) - 1
	indent_cociente = digitoacarreo 
	falsodividendo = dividendo.primerosdigitos(len(str(divisor.valor)))
	str_cociente = ' '
	indent = len(str(divisor.valor)) + len(str(falsodividendo)) + 2
	#iteracion = 20

		
	#print (falsodividendo)
	while digitoacarreo < len(str(dividendo.valor)):
		cocienteactual = falsodividendo // divisor.valor
		
		#print ('Falso dividendo ' + str(falsodividendo))
		str_cociente = str_cociente + str(cocienteactual)
		#print (cocienteparcial)
		restas.append(Resta(falsodividendo, (divisor.valor * cocienteactual), indent))


		print (20 * '#')
		print (' ' * (len(str(divisor.valor)) + 1) + ' ' * indent_cociente + str_cociente)
		print (' ' * (len(str(divisor.valor)) + 1) + '+' + '-' * len(str(dividendo.valor)))
		print (' ' + str(divisor.valor) + '|' + str(dividendo.valor))
		for resta in restas:
			resta.mostrar()
		#iteracion = iteracion + 1
		digitoacarreo = digitoacarreo + 1

		indent = indent + 1
		if digitoacarreo < len(str(dividendo.valor)):
			falsodividendo = int(resta.resultado() * 10 + int(dividendo.digito(digitoacarreo)))

dividendo = Numero(2696)
divisor = Numero(15)

division_con_procedimiento(dividendo, divisor)


