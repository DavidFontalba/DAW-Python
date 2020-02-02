"""
  * Colección de funciones para manejar fechas en cadenas de caracteres.
  *
  * El formato de la cadena es: AAAAMMDD.
  * Ejemplo: El 15 de diciembre de 2019 sería: "20191215"
  *
  * Colección de funciones:
  *
  * 1. fechaCorrecta: dice si la fecha que se pasa como parámetro es correcta.
  *
  * 2. fechaMas1Dia: suma un día a la fecha que se pasa como parámetro y lo devuelve.
  *
  * 3. fechaMasNDias: suma una serie de días a la fecha que se pasa como parámetro y lo devuelve.
  *
  * 4. fechaMenos1Dia: resta un día a la fecha que se pasa como parámetro y lo devuelve.
  *
  * 5. fechaMenosNDias: resta una serie de días a la fecha que se pasa como parámetro y lo devuelve.
  *
  * 6. esBisiesto: dice si la fecha que se pasa como parámetro es bisiesto.
  *
  * 7. comparaFechas: recibe dos fechas y devuelve un valor negativo si la 1ª es anterior a la
  *    segunda, cero si son iguales, y un valor positivo si la 1ª es posterior a la segunda.
  *
  * 8. fechaFormateada: recibe un fecha y devuelve una cadena con el formato:
  *    DD de {MES} de AAAA     (Ejemplo: "15 de Diciembre de 2019")
  *
  * 9. anyo, mes, dia, nombreMes: recibe un fecha y devuelve esos valores.
  *
  * @author rafa
  *
"""
"""
* Dice si la fecha que se pasa como parámetro es correcta.
*	Separo los meses y los dias
*	Los meses tienen que ser un numero entre 1 y 12
*		Para cada mes, tendrá un máximo
*		Febrero, si es bisiesto, cambiara su máximo de 28 a 29
*
* @param fecha
* @return verdadero o falso.
"""


def fechaCorrecta(fecha):
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
                  't', 'v', 'w', 'x', 'y', 'z']
    abecedarioMayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R',
                       'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    for i in range(len(fecha)):  # for original: int i=0; i<len(fecha); i+=1:
        for j in range(len(abecedario)):
            if fecha[i] == abecedario[j] or fecha[i] == abecedarioMayus[j]:
                return False
    month = mes(fecha)
    day = dia(fecha)

    # Si el mes no esta bien
    if month < 1 or month > 12:
        return False

    # Si el día no esta bien
    if day < 1:
        return False

    # Meses con 31 dias
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day > 31:
            return False

    # Meses con 30 dias
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            return False

    # Febrero
    elif month == 2:
        if esBisiesto(fecha):
            if day > 29:
                return False
        elif day > 28:
            return False

    return True


"""
*
* Suma un día a la fecha que se pasa como parámetro y la devuelve.
*
* @param fecha
* @return nuevo fecha
"""


def fechaMas1Dia(fecha):
    year = anyo(fecha)
    month = mes(fecha)
    day = dia(fecha)
    # Diciembre
    if month == 12:
        if day == 31:
            month = 1
            day = 1
            year += 1
        else:
            day += 1
    # Resto de meses con 31 dias
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
        if day == 31:
            month += 1
            day = 1
        else:
            day += 1
    # Meses con 30 dias
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day == 30:
            month += 1
            day = 1
        else:
            day += 1
    # Febrero
    elif month == 2:
        if esBisiesto(fecha):
            if day == 29:
                month += 1
                day = 1
            else:
                day += 1
        elif day == 28:
            month += 1
            day = 1
        else:
            day += 1

    day = str(day)
    month = str(month)

    # dia
    if len(day) < 2:
        day = "0" + day
    # mes
    if len(month) < 2:
        month = "0" + month

    return str(year) + month + day


"""
* Suma una serie de días a la fecha que se pasa como parámetro y la devuelve
* @param fecha
* @param dias
* @return nueva fecha
"""


def fechaMasNDias(fecha, dias):
    nuevaFecha = fecha
    for i in range(dias):  # for original: int i=0; i<dias; i+=1:
        nuevaFecha = fechaMas1Dia(nuevaFecha)
    return nuevaFecha


"""
* Resta un día a la fecha que se pasa como parámetro y la devuelve.
*
* @param fecha
* @return nuevo fecha
"""


def fechaMenos1Dia(fecha):
    year = anyo(fecha)
    month = mes(fecha)
    day = dia(fecha)

    # Enero
    if month == 1:
        if day == 1:
            month = 12
            day = 31
            year -= 1
        else:
            day -= 1

    # Meses cuyo mes anterior tiene 30 dias
    elif month == 12 or month == 5 or month == 7 or month == 10:
        if day == 1:
            month -= 1
            day = 30
        else:
            day -= 1

    # Meses cuyo mes anterior tiene 31 dias
    elif month == 4 or month == 6 or month == 9 or month == 11 or month == 8 or month == 2:
        if day == 1:
            month -= 1
            day = 31
        else:
            day -= 1

    # Marzo
    elif month == 3:
        if esBisiesto(fecha):
            if day == 1:
                month -= 1
                day = 29
        elif day == 1:
            month -= 1
            day = 28
        else:
            day -= 1

    day = str(day)
    month = str(month)

    # dia
    if len(day) < 2:
        day = "0" + day
    # mes
    if len(month) < 2:
        month = "0" + month

    return str(year) + month + day


"""
* Resta una serie de días a la fecha que se pasa como parámetro y la devuelve.
*
* @param fecha
* @param dias
* @return nueva fecha
"""


def fechaMenosNDias(fecha, dias):
    nuevaFecha = fecha

    for i in range(dias):  # for original: int i=0; i<dias; i+=1:
        nuevaFecha = fechaMenos1Dia(nuevaFecha)

    return nuevaFecha


"""
* Dice si la fecha que se pasa como parámetro es de un año bisiesto.
*
* @param fecha
* @return verdadero o falso
"""


def esBisiesto(fecha):
    year = anyo(fecha)

    if year / 4 == (int)(year / 4):
        if year / 100 != (int)(year / 100) or year / 400 == (int)(year / 400):
            return True
    return False


"""
* Recibe dos fechas y devuelve un valor negativo si la 1º es anterior a la 2º,
* cero si son iguales, y un valor positivo si la 1º es posterior a la segunda.
*
* @param fecha1
* @param fecha2
* @return entero negativo, cero o un entero positivo.
"""


def comparaFechas(fecha1, fecha2):
    fecha1Int = int(fecha1)
    fecha2Int = int(fecha2)

    return fecha1Int - fecha2Int


"""
* Recibe un fecha y devuelve una cadena con el formato DD de {MES} de AAAA
* (Ejemplo: "15 de Diciembre de 2019")
*
* @param fecha
* @return fecha formateada
"""


def fechaFormateada(fecha):
    day = dia(fecha)
    month = nombreMes(fecha)
    year = anyo(fecha)
    fechaFormat = (str(day) + " de " + str(month) + " de " + str(
        year))  # Original: String fechaFormat = day + " de " + month + " de " + year
    return fechaFormat


"""
* Devuelve el año de la fecha.
*
* @param fecha
* @return
"""


def anyo(fecha):
    anyo = ""
    for i in range((len(fecha) - 4)):  # for original: int i=0; i<(len(fecha)-4); i+=1:
        anyo += fecha[i] + ""
    year = int(anyo)

    return year


"""
* Devuelve el nombre del mes de la fecha.
*
* @param fecha
* @return
"""


def nombreMes(fecha):
    month = mes(fecha)
    if month == 1:
        return "enero"
    elif month == 2:
        return "febrero"
    elif month == 3:
        return "marzo"
    elif month == 4:
        return "abril"
    elif month == 5:
        return "mayo"
    elif month == 6:
        return "junio"
    elif month == 7:
        return "julio"
    elif month == 8:
        return "agosto"
    elif month == 9:
        return "septiembre"
    elif month == 10:
        return "octubre"
    elif month == 11:
        return "noviembre"
    elif month == 12:
        return "diciembre"
    else:
        return "ERROR: INVALID MONTH"


"""
* Devuelve el mes de la fecha
*
* @param fecha
* @return nombre del mes
"""


def mes(fecha):
    mes = ""
    for i in range((len(fecha) - 4), (len(fecha) - 2)):  # for original: int i=(len(fecha)-4); i<(len(fecha)-2); i+=1:
        mes += fecha[i] + ""

    month = int(mes)

    return month


"""
* Devuelve el día de la fecha.
*
* @param fecha
* @return
"""


def dia(fecha):
    dia = ""
    for i in range((len(fecha) - 2), len(fecha)):  # for original: int i=(len(fecha)-2); i<len(fecha); i+=1:
        dia += fecha[i]

    day = int(dia)

    return day


"""
* Devuelve una cadena en formato AAAAMMDD
* @param d día del mes
* @param m día del año
* @param a año
* @return
""""""
  * Colección de funciones para manejar fechas en cadenas de caracteres.
  *
  * El formato de la cadena es: AAAAMMDD.
  * Ejemplo: El 15 de diciembre de 2019 sería: "20191215"
  *
  * Colección de funciones:
  *
  * 1. fechaCorrecta: dice si la fecha que se pasa como parámetro es correcta.
  *
  * 2. fechaMas1Dia: suma un día a la fecha que se pasa como parámetro y lo devuelve.
  *
  * 3. fechaMasNDias: suma una serie de días a la fecha que se pasa como parámetro y lo devuelve.
  *
  * 4. fechaMenos1Dia: resta un día a la fecha que se pasa como parámetro y lo devuelve.
  *
  * 5. fechaMenosNDias: resta una serie de días a la fecha que se pasa como parámetro y lo devuelve.
  *
  * 6. esBisiesto: dice si la fecha que se pasa como parámetro es bisiesto.
  *
  * 7. comparaFechas: recibe dos fechas y devuelve un valor negativo si la 1ª es anterior a la
  *    segunda, cero si son iguales, y un valor positivo si la 1ª es posterior a la segunda.
  *
  * 8. fechaFormateada: recibe un fecha y devuelve una cadena con el formato:
  *    DD de {MES} de AAAA     (Ejemplo: "15 de Diciembre de 2019")
  *
  * 9. anyo, mes, dia, nombreMes: recibe un fecha y devuelve esos valores.
  *
  * @author rafa
  *
"""
"""
* Dice si la fecha que se pasa como parámetro es correcta.
*	Separo los meses y los dias
*	Los meses tienen que ser un numero entre 1 y 12
*		Para cada mes, tendrá un máximo
*		Febrero, si es bisiesto, cambiara su máximo de 28 a 29
*
* @param fecha
* @return verdadero o falso.
"""


def fechaCorrecta(fecha):
	abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','v','w','x','y','z']
	abecedarioMayus = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','V','W','X','Y','Z']

	for i in range(len(fecha)): # for original: int i=0; i<len(fecha); i+=1:
		for j in range(len(abecedario)):
			if fecha[i] == abecedario[j] or fecha[i] == abecedarioMayus[j]:
				return False
	month = mes(fecha)
	day = dia(fecha)

	#Si el mes no esta bien
	if month < 1 or month > 12:
		return False

	#Si el día no esta bien
	if day < 1:
		return False

	#Meses con 31 dias
	if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
		if day > 31:
			return False

	#Meses con 30 dias
	elif month == 4 or month == 6 or month == 9 or  month == 11:
		if day > 30:
			return False

	#Febrero
	elif month == 2:
		if esBisiesto(fecha):
			if day > 29:
				return False
		elif day > 28:
			return False

	return True


"""
*
* Suma un día a la fecha que se pasa como parámetro y la devuelve.
*
* @param fecha
* @return nuevo fecha
"""


def fechaMas1Dia(fecha):
	year = anyo(fecha)
	month = mes(fecha)
	day = dia(fecha)
	# Diciembre
	if month == 12:
		if day == 31:
			month = 1
			day = 1
			year += 1
		else:
			day += 1
	# Resto de meses con 31 dias
	elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
		if day == 31:
			month += 1
			day = 1
		else:
			day += 1
	# Meses con 30 dias
	elif month == 4 or month == 6 or month == 9 or month == 11:
		if day == 30:
			month += 1
			day = 1
		else:
			day += 1
	# Febrero
	elif month == 2:
		if esBisiesto(fecha):
			if day == 29:
				month += 1
				day = 1
			else:
				day += 1
		elif day == 28:
			month += 1
			day = 1
		else:
			day += 1

	day = str(day)
	month = str(month)

	# dia
	if len(day) < 2:
		day = "0"+day
	# mes
	if len(month) < 2:
		month = "0"+month

	return str(year) + month + day


"""
* Suma una serie de días a la fecha que se pasa como parámetro y la devuelve
* @param fecha
* @param dias
* @return nueva fecha
"""


def fechaMasNDias(fecha, dias):
	nuevaFecha = fecha
	for i in range(dias): # for original: int i=0; i<dias; i+=1:
		nuevaFecha = fechaMas1Dia(nuevaFecha)
	return nuevaFecha


"""
* Resta un día a la fecha que se pasa como parámetro y la devuelve.
*
* @param fecha
* @return nuevo fecha
"""

def fechaMenos1Dia(fecha):
	year = anyo(fecha)
	month = mes(fecha)
	day = dia(fecha)

	#Enero
	if month == 1:
		if day == 1:
			month = 12
			day = 31
			year -= 1
		else:
			day -= 1

	#Meses cuyo mes anterior tiene 30 dias
	elif month == 12 or month == 5 or month == 7 or month == 10:
		if day == 1:
			month -= 1
			day = 30
		else:
			day -= 1

	#Meses cuyo mes anterior tiene 31 dias
	elif month == 4 or month == 6 or month == 9 or  month == 11 or month == 8 or month == 2:
		if day == 1:
			month -= 1
			day = 31
		else:
			day -= 1

	#Marzo
	elif month == 3:
		if esBisiesto(fecha):
			if day == 1:
				month -= 1
				day = 29
		elif day == 1:
			month -= 1
			day = 28
		else:
			day -= 1

	day = str(day)
	month = str(month)

	# dia
	if len(day) < 2:
		day = "0"+day
	# mes
	if len(month) < 2:
		month = "0"+month

	return str(year) + month + day


"""
* Resta una serie de días a la fecha que se pasa como parámetro y la devuelve.
*
* @param fecha
* @param dias
* @return nueva fecha
"""


def fechaMenosNDias(fecha,dias):
	nuevaFecha = fecha

	for i in range(dias): # for original: int i=0; i<dias; i+=1:
		nuevaFecha = fechaMenos1Dia(nuevaFecha)

	return nuevaFecha


"""
* Dice si la fecha que se pasa como parámetro es de un año bisiesto.
*
* @param fecha
* @return verdadero o falso
"""

def esBisiesto(fecha):
	year = anyo(fecha)

	if  year/4 == (int)(year/4) :
		if year/100 != (int)(year/100) or year/400 == (int)(year/400):
			return True
	return False


"""
* Recibe dos fechas y devuelve un valor negativo si la 1º es anterior a la 2º,
* cero si son iguales, y un valor positivo si la 1º es posterior a la segunda.
*
* @param fecha1
* @param fecha2
* @return entero negativo, cero o un entero positivo.
"""


def comparaFechas(fecha1, fecha2):
	fecha1Int = int(fecha1)
	fecha2Int = int(fecha2)

	return fecha1Int - fecha2Int


"""
* Recibe un fecha y devuelve una cadena con el formato DD de {MES} de AAAA
* (Ejemplo: "15 de Diciembre de 2019")
*
* @param fecha
* @return fecha formateada
"""


def fechaFormateada(fecha):
	day = dia(fecha)
	month = nombreMes(fecha)
	year = anyo(fecha)
	fechaFormat = (str(day) + " de " + str(month) + " de " + str(year)) #Original: String fechaFormat = day + " de " + month + " de " + year
	return fechaFormat


"""
* Devuelve el año de la fecha.
*
* @param fecha
* @return
"""


def anyo(fecha):
	anyo = ""
	for i in range((len(fecha)-4)): # for original: int i=0; i<(len(fecha)-4); i+=1:
		anyo += fecha[i] + ""
	year = int(anyo)

	return year

"""
* Devuelve el nombre del mes de la fecha.
*
* @param fecha
* @return
"""


def nombreMes(fecha):
	month = mes(fecha)
	if month == 1:
		return "enero"
	elif month == 2:
		return "febrero"
	elif month == 3:
		return "marzo"
	elif month == 4:
		return "abril"
	elif month == 5:
		return "mayo"
	elif month == 6:
		return "junio"
	elif month == 7:
		return "julio"
	elif month == 8:
		return "agosto"
	elif month == 9:
		return "septiembre"
	elif month == 10:
		return "octubre"
	elif month == 11:
		return "noviembre"
	elif month == 12:
		return "diciembre"
	else:
		return "ERROR: INVALID MONTH"


"""
* Devuelve el mes de la fecha
*
* @param fecha
* @return nombre del mes
"""


def mes(fecha):
	mes = ""
	for i in range((len(fecha)-4),(len(fecha)-2)): # for original: int i=(len(fecha)-4); i<(len(fecha)-2); i+=1:
		mes += fecha[i] + ""

	month = int(mes)

	return month


"""
* Devuelve el día de la fecha.
*
* @param fecha
* @return
"""


def dia(fecha):
	dia = ""
	for i in range((len(fecha)-2),len(fecha)): # for original: int i=(len(fecha)-2); i<len(fecha); i+=1:
		dia += fecha[i]

	day = int(dia)

	return day


"""
* Devuelve una cadena en formato AAAAMMDD
* @param d día del mes
* @param m día del año
* @param a año
* @return
"""