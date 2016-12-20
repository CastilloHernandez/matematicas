import random

calif=0.0
restas=0
correctas=0
op1=0
op2=0
r=0
respuesta=' '

while respuesta != 'salir':
	op2=random.randrange(0,1000)
	op1=random.randrange(op2,1000)
	print ' ' + str(op1).rjust(3)
	print '-' + str(op2).rjust(3)
	print '________'
	respuesta = raw_input('Resultado: ')
	if respuesta != 'salir':
		try: 
			r=int(respuesta,10)
			if r==op1-op2:
				print 30*' ' + 'Correcto!'
				correctas=correctas+1
			else:
				print 20*' ' + 'Incorrecto!'
				print 20*' ' + 'Resultado: ' + str(op1-op2)
			restas=restas+1
		except:
			print 'Respuesta invalida'
	if restas>0:	
		print 30*' ' + 'Calif: ' + str(round((float(correctas)/float(restas))*10,2))
