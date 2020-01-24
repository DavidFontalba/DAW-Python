"""
2. Crea una clase Fraccion (Python) de forma que podamos hacer las siguientes operaciones:

Contruir un objeto Fraccion pasándole el numerador y el denominador.
Obtener la fracción como cadena de caracteres.
Obtener y modificar numerador y denominador. No se puede dividir por cero.
Obtener resultado de la fracción (número real).
Multiplicar la fracción por un número.
Multiplicar, sumar y restar fracciones.
Simplificar la fracción.
"""
class Fraccion:
    """
    Versión 1.0

    Esta clase representa objetos de tipo Fracción
    """
    def __init__(self, numerador, denominador):
        """
        Constructor del objeto
        :param numerador:
        :param denominador:
        """
        self.__numerador = numerador
        self.__denominador = denominador
        self.__aux = 2

    def mostrar(self):
        """
        Muestra una fracción como cadena de texto
        :return: cadena de texto
        """
        cadena = str(self.__numerador)+"/"+str(self.__denominador)
        return cadena

    def valor(self):
        """
        Devuelve el valor de la fracción
        :return:
        """
        return self.__numerador / self.__denominador

    def multiplicar(self, valor):
        """
        Multiplica una fracción por un valor
        :param valor:
        :return:
        """
        self.__numerador *= valor
        self.simplificar()

    def sumar_otro(self, otro):
        """
        Suma una fracción con otra
        :param otro:
        :return: aux, resultado de la suma
        """
        numerResult = self.__numerador * otro.__denominador+self.__denominador*otro.numerador
        denorResult = self.__denominador * otro.__denominador

        aux = Fraccion(numerResult, denorResult)
        aux.simplificar()
        return aux

    def restar_otro(self, otro):
        """
        Resta una fracción con otra
        :param otro:
        :return: aux, resultado de la resta
        """
        numerResult = self.__numerador * otro.__denominador - (self.__denominador * otro.numerador)
        denorResult = self.__denominador * otro.__denominador

        aux = Fraccion(numerResult, denorResult)
        aux.simplificar()
        return aux

    def multiplicar_otro(self, otro):
        """
        Multiplica una fracción con otra
        :param otro:
        :return: aux, resultado de la multiplicacion
        """
        numerResult = self.__numerador * otro.__numerador
        denorResult = self.__denominador * otro.__denominador
        aux = Fraccion(numerResult, denorResult)
        aux.simplificar()
        return aux

    def simplificar(self):
        """
        Simplifica una fracción
        :return:
        """
        # Prueba a dividir numerador y divisor entre aux
        num = float(self.__numerador)/self.__aux
        den = float(self.__denominador)/self.__aux

        # Si son enteros establezco el resultado como los atributos de la fraccion
        # y vuelvo a llamar a la función para que vuelva a dividir
        if type(num) == type(1) and type(den) == type(1):
            self.__numerador = num
            self.__denominador = den
            self.simplificar()
        else:
            # Si alguna de estas condiciones se cumplen, no será posible seguir simplificando
            if self.__aux != self.__numerador or self.__aux != self.__denominador or num <= 1 or den <= 1:
                return self
            else:
                self.__aux += 1
                self.simplificar()

    # Propiedades

    @property
    def ver_numerador(self):
        """
        Devuelve el numerador
        :return:
        """
        return self.__numerador

    @property
    def ver_denominador(self):
        """
        Devuelve el denominador
        :return:
        """
        return self.__denominador

    @property
    def cambiar_numerador(self, numerador):
        """
        Permite cambiar el numerador a una fracción
        :param numerador:
        :return:
        """
        self.__numerador = numerador

    @property
    def cambiar_denominador(self, denominador):
        """
        Permite cambiar el denominador a una fracción, evitando que este tome el valor de 0
        :param denominador:
        :return:
        """
        if denominador != 0:
            self.__denominador = denominador
        else:
            print("ERROR: El denominador no puede ser 0")
