"""
1. Crea la clase Tiempo. Los objetos de la clase Tiempo son intervalos de tiempo y se crean de la forma:
t = Tiempo(1, 20, 30)
donde los parámetros que se le pasan al constructor son las horas, los minutos y los segundos respectivamente.
Crea métodos para:
Sumar y restar otro objeto de la clase Tiempo.
Sumar y restar segundos, minutos y/o horas.
Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.
Realiza un programa de prueba para comprobar que la clase funciona bien.
"""


class Tiempo:
    """
    Versión 1.0
    Esta clase representa objetos de tipo tiempo
    """
    __num_objetos = 0 # Contador de objetos tipo Tiempo creados

    def __init__(self, hours, minutes, seconds):
        """
        Constructor de la clase
        :param hours:
        :param minutes:
        :param seconds:
        """
        Tiempo.__num_objetos += 1

        assert hours >= 0 and 60 >= minutes >= 0 and 60 >= seconds >= 0
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def sumarle(self, hours=0, minutes=0, seconds=0):
        """
        Sumar segundos, minutos y/o horas.
        :param hours: Horas a sumar
        :param minutes: Minutos a sumar
        :param seconds: Segundos a sumar
        :return:
        """
        assert self.__hours + hours < 0 and self.__minutes + minutes < 0 and self.__seconds + seconds < 0
        segundos = self.__seconds
        minutos = self.__minutes
        horas = self.__hours

        segundos += seconds
        while segundos >= 60:
            segundos -= 60
            minutos += 1

        minutos += minutes
        while minutos >= 60:
            minutos -= 60
            horas += 1

        horas += hours

        return Tiempo(horas, minutos, segundos)

    def restarle(self, hours=0, minutes=0, seconds=0):
        """
        Restar segundos, minutos y/o horas.
        :param hours: Horas a restar
        :param minutes: Minutos a restar
        :param seconds: Segundos a restar
        :return:
        """
        totalSegundos = (3600 * hours) + (60 * minutes) + seconds
        totalTiempoSegundos = (3600 * self.__hours) + (60 * self.__minutes) + self.__seconds

        totalTiempoSegundos -= totalSegundos

        segundos = totalTiempoSegundos

        horas = segundos // 3600
        segundos = segundos % 3600
        minutos = segundos // 60
        segundos = segundos % 60

        return Tiempo(horas, minutos, segundos)

    def sumarOtro(self, otro):
        """
        Sumar otro objeto de la clase Tiempo.
        :param otro: Objeto de la misma clase
        :return:
        """
        return self.sumarle(otro.__hours, otro.__minutes, otro.__seconds)

    def restarOtro(self, otro):
        """
        Restar otro objeto de la clase Tiempo.
        :param otro: Objeto de la misma clase
        :return:
        """
        return self.restarle(otro.__hours, otro.__minutes, otro.__seconds)

    def escribe(self):
        """
        Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.
        :return:
        """

        return str(self.__hours) + "h " + str(self.__minutes) + "m " + str(self.__seconds) + "s"

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    @staticmethod
    def num_objetos():
        return Tiempo.__num_objetos

if __name__ == "__main__":
    t1 = Tiempo(1, 15, 40)
    t2 = Tiempo(30, 29, 55)
    print("Probamos clase Tiempo con t1 y t2: ")
    # mostramos
    print(t1.escribe())
    print(t2.escribe())
    print()
    # suma y resta horas
    aux = t1.restarle(0,20,50)
    print("Resultado de restarle a t1 20 m 50s: ", aux.escribe())
    aux = t1.sumarle(1,50,50)
    print("Resultado de sumarle a t1 1 h 50 m 50 s: ", aux.escribe())
    print()
    # suma y resta otros
    aux = t2.restarOtro(t1)
    print("Restarle t1 a t2: ", aux.escribe())
    aux = t2.sumarOtro(t1)
    print("Sumarle t1 a t2: " , aux.escribe())
    print()
    print("Objetos creados: ", Tiempo.num_objetos())