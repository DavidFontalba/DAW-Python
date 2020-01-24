"""
* Ejercicios 1-14
*
*	Crea una biblioteca de funciones matemáticas que contenga las siguientes
*	funciones. Recuerda que puedes usar unas dentro de otras si es necesario.
*	Observa bien lo que hace cada función ya que, si las implementas en el orden
*	adecuado, te puedes ahorrar mucho trabajo. Por ejemplo, la función esCapicua
*	resulta trivial teniendo voltea y la función siguientePrimo también es muy fácil de
*	implementar teniendo esPrimo .
*
*	1. esCapicua: Devuelve verdadero si el número que se pasa como paráme-
*	tro es capicúa y falso en caso contrario.
*	2. esPrimo: Devuelve verdadero si el número que se pasa como parámetro
*	es primo y falso en caso contrario.
*	3. siguientePrimo: Devuelve el menor primo que es mayor al número que
*	se pasa como parámetro.
*	4. potencia: Dada una base y un exponente devuelve la potencia.
*	5. digitos: Cuenta el número de dígitos de un número entero.
*	6. voltea: Le da la vuelta a un número.
*	7. digitoN: Devuelve el dígito que está en la posición n de un número entero.
*	Se empieza contando por el 0 y de izquierda a derecha.
*	8. posicionDeDigito: Da la posición de la primera ocurrencia de un dígito
*	dentro de un número entero. Si no se encuentra, devuelve -1.
*	9. quitaPorDetras: Le quita a un número n dígitos por detrás (por la
*	derecha).
*	10. quitaPorDelante: Le quita a un número n dígitos por delante (por la
*	izquierda).
*	11. pegaPorDetras: Añade un dígito a un número por detrás.
*	12. pegaPorDelante: Añade un dígito a un número por delante.
*	13. trozoDeNumero: Toma como parámetros las posiciones inicial y final
*	dentro de un número y devuelve el trozo correspondiente.
*	14. juntaNumeros: Pega dos números para formar uno.
*
*	@author David Galván Fontalba
*	Fecha: 4/12/2019
*
*	Orden que voy a implementar:
*	1. potencia			2. voltea			3. esPrimo			4. digitos
*	5. esCapicua		6. siguientePrimo	7. digitoN			8. posicionDeDigito
*	9. trozoDeNumero	10. juntaNumeros	11. pegaPorDetras	12. pegaPorDelante
*	13. quitaPorDetras	14. quitaPorDelante
"""

"""
 * 1 Función que hace una potencia dadas la base y el exponente
 * @param base
 * @param exp
 * @return potencia
"""


def potencia (base, exp):
	potenciaNum = base
	for i in range(1, exp): # for original: int i=1 i<exp i+=1:
		potenciaNum = potenciaNum * base
	return potenciaNum


"""
* 2 Función que invierte los dígitos de un entero
* @param num
* @return inverse
"""


def voltea (num):
	aux = num
	inverse = 0
	while aux > 0:
		resto = aux % 10
		inverse = inverse * 10 + resto
		aux = aux//10
	return inverse


"""
* 3 Función para decirte si un número es primo (true) o no (false)
* @param num
* @return true o false
"""


def esPrimo (num):
	divider = 2
	itsPrime = True
	while (divider <= num//2) and itsPrime:
		if num % divider == 0:
			itsPrime = False
		divider += 1
	return itsPrime


"""
*
* 4 Función que cuenta el número de dígitos de un número entero
* @param num
* @return digits
"""


def digitos (num):
	digits = 0
	while num != 0:
		num = num//10
		digits += 1
	return digits


"""
*
* 5 Función que comprueba si un número es capicua
* @param num
* @return true o false
"""


def esCapicua (num):
	if num == voltea(num):
		return True
	else:
		return False


"""
*
* 6 Función que te dice el siguiente número primo tras el número que has introducido
* @param num
* @return candidate
"""


def siguientePrimo (num):
	candidate = num+1
	while not esPrimo(candidate):
		candidate += 1
	return candidate


"""
*
* 7 Funcion que devuelve el dígito que está en la posición n de un número entero.
* Se empieza contando por el 0 y de izquierda a derecha.
* @param num
* @param n
* @return 
"""


def digitoN (num, n):
	ourNum = voltea(num)
	for i in range(n): # for original: int i=0 i < n i+=1:
		ourNum = ourNum // 10
	return ourNum % 10


"""
* 8 Da la posición de la primera ocurrencia de un dígito
*	dentro de un número entero. Si no se encuentra, devuelve -1.
* @param num
* @param digit
* @return
"""


def posicionDeDigito (num, digit):
	ourNum = voltea(num)
	for i in range(digitos(num)): # for original: int i=0 i < digitos(num) i+=1:
		if ourNum % 10 == digit:
			return i
		ourNum = ourNum // 10
	return -1


"""
* 9. trozoDeNumero: Toma como parámetros las posiciones inicial y final
*	dentro de un número y devuelve el trozo correspondiente.
*
* @param num
* @param init
* @param end
* @return
"""


def trozoDeNumero (num, init, end):
	aux = ""
	for i in range(init, end+1): # for original: int i=init i <= end i+=1:
		digito = digitoN(num, i)
		aux += str(digito)
	return int(aux)


"""
*
* 10. juntaNumeros: Pega dos números para formar uno.
* @param num1
* @param num2
* @return solution
"""

def juntaNumeros (num1, num2):
	num1Str = str(num1)
	num2Str = str(num2)
	solution = num1Str + num2Str
	return int(solution)

"""
*
* 11. pegaPorDetras: Añade un dígito a un número por detrás.
* @param num
* @param digit
* @return solution
"""

def pegaPorDetras (num, digit):
	solution = juntaNumeros(num, digit)
	return solution

"""
*
* 12. pegaPorDelante: Añade un dígito a un número por delante.
* @param num
* @param digit
* @return solution
"""

def pegaPorDelante (num, digit):
	solution = juntaNumeros(digit, num)
	return solution

"""
*
* 13. quitaPorDetras: Le quita a un número n dígitos por detrás (por la derecha).
* @param num
* @param numOfDigits
* @return ourNum
"""

def quitaPorDetras (num, numOfDigits):
	ourNum = num
	for i in range(numOfDigits): # for original: int i=0 i<numOfDigits i+=1:
		ourNum = ourNum//10
	return ourNum

"""
* 14. quitaPorDelante: Le quita a un número n dígitos por delante (por la izquierda).
* @param num
* @param numOfDigits
* @return ourNum
"""

def quitaPorDelante (num, numOfDigits):
	ourNum = voltea(num)
	for i in range(numOfDigits): # for original: int i=0 i<numOfDigits i+=1:
		ourNum = ourNum//10
	return voltea(ourNum)
