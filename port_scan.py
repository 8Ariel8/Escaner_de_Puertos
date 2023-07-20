#!/usr/bin/python3

import nmap
escaneo = nmap.PortScanner()
#Aca estoy creando una instancia de PortScanner.

print("""
+-------------------------------+
|                               |
|                               |
| Bienvenidos a mi primer       |
| escaner de puertos.           |
|                               |
|                               |
| *-*-*-*-*-*-*-*-*-*-*-*-*-*-  |
|                               |
|       Micoli Ariel R.         |
| Entrega Evaluacion Continua.  |
|                               |
|     Version Alfa.             |
+-------------------------------+
"""
)

menu = True
while menu==True:
	print("""Que desea realizar: 
	[1]- INICIAR
	[2]- SALIR SISTEMA
	 """)      
	respuesta = input()
	if respuesta == "2":
		menu = False

	elif respuesta == "1":

		masEscaneos = True
		while masEscaneos == True:
			eleccionTipo = input("""
	Que tipo de escaneo  desea llevar adelante:
	[1]-Escaneo simple.
	[2]-Escaneo sistema operativo.
	

""")
			if eleccionTipo == "1":
				masEscaneos = False
				direccionEscaneo = input("Usted ha elegido Escaneo Simple. Por favor, ahora ingrese el numero de ip que desea escanear ")
				print("Usted ha elegido la direccion ", direccionEscaneo)
				type(direccionEscaneo)
				escaneo.scan(direccionEscaneo, "1-1024", "-v")
				print(escaneo.scaninfo())
				try:
					print("Puertos abiertos: ", escaneo[direccionEscaneo]["tcp"].keys())
				except:
					print("No se encontraron puertos abiertos en el Protocolo TCP")
# Utilice sentencias try/except debido a que cuando no tenia puertos abiertos en protocolo 
# TCP se generaba un error y el programa se bloqueaba.
				print("GRACIAS POR HABER USADO NUESTRO SERVICIO")

			elif eleccionTipo == "2":
				masEscaneos = False
				direccionEscaneo = input("Usted ha elegido Escaneo Sistema Operativo.\n  Por favor, ahora ingrese el numero de ip que desea escanear ")
				print("Usted ha elegido la direccion ", direccionEscaneo)
				escaneo.scan(direccionEscaneo, arguments="-A")
				print(escaneo.scaninfo())

				resultadoOSMATCH = escaneo[direccionEscaneo].get("osmatch", [])
				if resultadoOSMATCH:
					print("Información del sistema operativo:")
					for osmatch in resultadoOSMATCH:
						print("Nombre: ", osmatch["name"])
						print("Familia: ", osmatch["osclass"]["osfamily"])
						print("Tipo: ", osmatch["osclass"]["type"])
						print("---------------")
						print("Sistema Operativo: ", resultadoOSMATCH[0]["name"] )
				else:
					print("No se encontró información del sistema operativo.")

			else:
				print("Error de tipeo. \n Debe ingresar solo alguna de las opciones proporcionadas")	
	else:
		print("Error al tipear. Debe elegir numericamente las opciones proporcionadas")

			









