class FechaErronea:

    def __init__(self, mensaje):
        self.mensaje = mensaje

class Fecha:
    """
     * Versión 2.0
     * -Añadidos respecto a la 1.0
     *   · Añadido el método __str__
     *
     * Clase para manejar fechas en cadenas de caracteres.
     *
     * El formato de la cadena es: AAAAMMDD.
     * Ejemplo: El 15 de diciembre de 2019 sería: "20191215"
     *
     *
     * @author David Galván Fontalba
     * Basado en la colección de funciones "Fecha.py" del examen del primer trimestre de Programación
     *
    """
    __num_objetos = 0  # Contador de objetos tipo Fecha creado

    def __init__(self, anyo, mes, dia):
        """
        Constructor de la clase
        :param anyo:
        :param mes:
        :param dia:
        """
        Fecha.__num_objetos += 1

        fecha = Fecha.fecha(anyo, mes, dia)
        if not self.fechaCorrecta(fecha): #Compruebo que la fecha es correcta para poder crear el objeto
            raise FechaErronea("Día, mes o año introducidos incorrectamente.")

        self.__anyo = anyo
        self.__mes = mes
        self.__dia = dia

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, value):
        if not self.fechaCorrecta(Fecha.fecha(self.__anyo, self.__mes, self.__dia)):
            raise FechaErronea("Día, mes o año introducidos incorrectamente.")
        self.__dia = value

    @property
    def mes(self):
        return self.__mess

    @dia.setter
    def mes(self, value):
        if not self.fechaCorrecta(Fecha.fecha(self.__anyo, self.__mes, self.__dia)):
            raise FechaErronea("Día, mes o año introducidos incorrectamente.")
        self.__mes = value

    @property
    def anyo(self):
        return self.__anyo

    @dia.setter
    def anyo(self, value):
        if not self.fechaCorrecta(Fecha.fecha(self.__anyo, self.__mes,self.__dia)):
            raise FechaErronea("Día, mes o año introducidos incorrectamente.")
        self.__anyo = value

    #Métodos estáticos
    @staticmethod
    def fechaCorrecta(fecha):
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
        abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
                      't', 'v', 'w', 'x', 'y', 'z']
        abecedarioMayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

        for i in range(len(fecha)):  # for original: int i=0; i<len(fecha); i+=1:
            for j in range(len(abecedario)):
                if fecha[i] == abecedario[j] or fecha[i] == abecedarioMayus[j]:
                    return False
        month = Fecha.mes(fecha)
        day = Fecha.dia(fecha)

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
            if Fecha.esBisiesto(fecha):
                if day > 29:
                    return False
            elif day > 28:
                return False

        return True

    @staticmethod
    def fecha(a, m, d):
        """
         * Devuelve una cadena en formato AAAAMMDD
         * @param d, m, a
         *
         * Test:
         * >>> fecha(6, 1, 2020)
         * '20200106'
        """
        dia_ = str(d).strip()
        mes_ = str(m).strip()
        año_ = str(a).strip()
        # día
        if len(dia_) < 2:
            dia_ = "0" + dia_
        # mes
        if len(mes_) < 2:
            mes_ = "0" + mes_
        # año
        for i in range(len(año_), 4):
            año_ = "0" + año_
        return año_ + mes_ + dia_

    def fecha(self):
        """
         * Devuelve una cadena en formato AAAAMMDD
         * @param self
         *
         * Test:
         * >>> fecha(6, 1, 2020)
         * '20200106'
        """
        dia_ = self.__dia
        mes_ = self.__mes
        año_ = self.__anyo
        # día
        if len(dia_) < 2:
            dia_ = "0" + dia_
        # mes
        if len(mes_) < 2:
            mes_ = "0" + mes_
        # año
        for i in range(len(año_), 4):
            año_ = "0" + año_
        return año_ + mes_ + dia_

    @staticmethod
    def anyo(fecha):
        """
         * Devuelve el año de la fecha.
         *
         * @param fecha
         * @return
        """
        anyo = ""
        for i in range((len(fecha) - 4)):  # for original: int i=0; i<(len(fecha)-4); i+=1:
            anyo += fecha[i] + ""
        year = int(anyo)

        return year

    @staticmethod
    def mes(fecha):
        """
         * Devuelve el mes de la fecha
         *
         * @param fecha
         * @return nombre del mes
        """
        mes = ""
        for i in range((len(fecha) - 4),
                       (len(fecha) - 2)):  # for original: int i=(len(fecha)-4); i<(len(fecha)-2); i+=1:
            mes += fecha[i] + ""

        month = int(mes)

        return month

    @staticmethod
    def dia(fecha):
        """
         * Devuelve el día de la fecha.
         *
         * @param fecha
         * @return
        """
        dia = ""
        for i in range((len(fecha) - 2), len(fecha)):  # for original: int i=(len(fecha)-2); i<len(fecha); i+=1:
            dia += fecha[i]

        day = int(dia)

        return day

    @staticmethod
    def esBisiesto(fecha):
        """
         * Dice si la fecha que se pasa como parámetro es de un año bisiesto.
         *
         * @param fecha
         * @return verdadero o falso
        """
        year = Fecha.anyo(fecha)

        if year / 4 == int(year / 4):
            if year / 100 != int(year / 100) or year / 400 == int(year / 400):
                return True
        return False

    def esBisiesto(self):
        """
         * Dice si la fecha que se pasa como parámetro es de un año bisiesto.
         *
         * @param fecha
         * @return verdadero o falso
        """
        year = self.__anyo

        if year / 4 == int(year / 4):
            if year / 100 != int(year / 100) or year / 400 == int(year / 400):
                return True
        return False

    def __fechaMas1Dia(self):
        """
         *
         * Suma un día a la fecha que se pasa como parámetro y la devuelve.
         *
         * @param fecha
         * @return nuevo fecha
        """
        year = self.__anyo
        month = self.__mes
        day = self.__dia
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
            if Fecha.esBisiesto(self):
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

        return Fecha(year, month, day)

    def __add__(self, dias):
        """
         * Suma una serie de días a la fecha que se pasa como parámetro y la devuelve
         * @param fecha
         * @param dias
         * @return nueva fecha
        """
        nuevaFecha = self

        if dias > 0:
            for i in range(dias):  # for original: int i=0; i<dias; i+=1:
                nuevaFecha = nuevaFecha.__fechaMas1Dia()
        else:
            for i in range(abs(dias)):
                nuevaFecha = nuevaFecha.__fechaMenos1Dia()
        return nuevaFecha

    def __radd__(self, dias):
        return self + dias

    def __fechaMenos1Dia(self):
        """
         * Resta un día a la fecha que se pasa como parámetro y la devuelve.
         *
         * @param fecha
         * @return nuevo fecha
        """
        year = self.__anyo
        month = self.__mes
        day = self.__dia

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
            if Fecha.esBisiesto(self):
                if day == 1:
                    month -= 1
                    day = 29
            elif day == 1:
                month -= 1
                day = 28
            else:
                day -= 1

        return Fecha(year, month, day)

    def __sub__(self, dias):
        """
         * Resta una serie de días a la fecha que se pasa como parámetro y la devuelve.
         *
         * @param fecha
         * @param dias
         * @return objeto con la nueva fecha
        """
        return self + -1*dias

    def comparaFechas(self, otra):
        """
         * Recibe dos fechas y devuelve un valor negativo si la 1º es anterior a la 2º,
         * cero si son iguales, y un valor positivo si la 1º es posterior a la segunda.
         *
         * @param Objeto Fecha
         * @param Otro objeto Fecha
         * @return entero negativo, cero o un entero positivo.
        """
        fecha1Int = int(Fecha.fecha(self))
        fecha2Int = int(Fecha.fecha(otra))

        return fecha1Int - fecha2Int

    def fechaFormateada(self):
        """
         * Recibe un fecha y devuelve una cadena con el formato DD de {MES} de AAAA
         * (Ejemplo: "15 de Diciembre de 2019")
         *
         * @param fecha
         * @return fecha formateada
        """
        day = self.__dia
        month = self.__mes
        year = self.__anyo
        fechaFormat = (str(day) + " de " + str(month) + " de " + str(
            year))  # Original: String fechaFormat = day + " de " + month + " de " + year
        return fechaFormat

    def nombreMes(self):
        """
         * Devuelve el nombre del mes de la fecha.
         *
         * @param fecha
         * @return
        """
        month = self.__mes
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

    def dias_mes_año(self):
        """
         * Esta función se usará para simplificar otras funciones que requieren saber
         * el número de días de cada mes y se complican al tener en cuenta el 29 de febrero
         * de los años bisiestos.
         * @param fecha_
         * @return vector con los días de cada mes para el año de fecha_
         * Test:
         * >>> dias_mes_año("20200106")    # bisiesto
         * [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
         * >>> dias_mes_año("20190102")    # no es bisiesto
         * [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        """
        dias_mes_este_año = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Fecha.esBisiesto(self):
            dias_mes_este_año[1] += 1  # hay 29 días en febrero en este caso
        return dias_mes_este_año

    def __str__(self):
        return Fecha.fechaFormateada(self)