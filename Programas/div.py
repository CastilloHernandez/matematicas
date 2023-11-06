import random

calif=0.0
restas=0
correctas=0
op1=0
op2=0
respuesta=' '

while respuesta != 'salir':
	op1=random.randrange(1,13)
	op2=random.randrange(op1,9999)
	print ' ' * len(str(op1).rjust(2)) + ' ' + chr(218) + chr(196) + chr(196) * len(str(op2).rjust(2))
	print str(op1).rjust(2) + ' ' + chr(179) + ' ' + str(op2).rjust(2) 
	
	respuesta = raw_input('Resultado: ')
	resto = raw_input('Resto: ')
	if respuesta == '':
		respuesta = '0'
	if resto=='':
		resto='0'
	if respuesta != 'salir':
		if int(respuesta,10)==int(round(op2/op1)):
			if int(resto)==int(op2 % op1):
				print 30*' ' + 'Correcto!'
				correctas=correctas+1
		else:
			print 20*' ' + 'Incorrecto!'
			print 20*' ' + 'Resultado: ' + str(int(round(op2/op1)))
			print 20*' ' + 'Resto: ' + str(op2 % op1)
		restas=restas+1
	if restas>0:	
		print 30*' ' + 'Calif: ' + str(round((float(correctas)/float(restas))*10,2))
