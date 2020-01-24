import tiempo.Fecha
"""
  * Prueba funciones de Fecha.java.
  *
  * @author rafa
  *
"""


# Testeamos funciones fecha correcta
fechas = [  "20191215", # correcto
            "20181111", # correcto
            "dfdfdw",   # incorrecto
            "AAAAMMDD", # incorrecto
            "20181242", # incorrecto (diciembre no tiene 42 días)
            "20010229", # incorrecto (no es bisiesto)
            "20000229"  # correcto (fue bisiesto)
]
for f in fechas:
    print(f"La fecha {f} tiene un formato ", end="") #Original: print("La fecha " + f + " tiene un formato ",end="")
    if tiempo.Fecha.fechaCorrecta(f):
        print("CORRECTO")
    else:
        print("INCORRECTO")

print()

# Testeamos suma y resta de días
fecha1 = "20160228"
fecha2 = "20160301"
fecha3 = "20170228"
fecha4 = "20170301"
print("Si sumamos un día a '" + tiempo.Fecha.fechaFormateada(fecha1) + "' obtenemos: " + tiempo.Fecha.fechaMas1Dia(fecha1))
print("Si restamos un día a '" + tiempo.Fecha.fechaFormateada(fecha2) + "' obtenemos: " + tiempo.Fecha.fechaMenos1Dia(fecha2))
print("Si sumamos un día a '" + tiempo.Fecha.fechaFormateada(fecha3) + "' obtenemos: " + tiempo.Fecha.fechaMas1Dia(fecha3))
print("Si restamos un día a '" + tiempo.Fecha.fechaFormateada(fecha4) + "' obtenemos: " + tiempo.Fecha.fechaMenos1Dia(fecha4))
print()

suma = int(input("¿Cuantos días quieres sumar a " + tiempo.Fecha.fechaFormateada(fecha1) + "? "))
print("La fecha resultante es " + tiempo.Fecha.fechaMasNDias(fecha1, suma))
print()

resta = int(input("¿Cuantos días quieres restar a " + tiempo.Fecha.fechaFormateada(fecha1) + "? "))
print("La fecha resultante es " + tiempo.Fecha.fechaMenosNDias(fecha1, resta))
print()

# Testeamos comparaciones de fechas
fecha2 = "20160120"
fecha3 = "20190101"
print("El resultado de comparar '" + str(tiempo.Fecha.fechaFormateada(fecha1)) + "' con '" + str(tiempo.Fecha.fechaFormateada(fecha2)) + "' es " + str(tiempo.Fecha.comparaFechas(fecha1, fecha2)))
print("El resultado de comparar '" + str(tiempo.Fecha.fechaFormateada(fecha1)) + "' con '" + str(tiempo.Fecha.fechaFormateada(fecha3)) + "' es " + str(tiempo.Fecha.comparaFechas(fecha1, fecha3)))
print("El resultado de comparar '" + str(tiempo.Fecha.fechaFormateada(fecha3)) + "' con '" + str(tiempo.Fecha.fechaFormateada(fecha2)) + "' es " + str(tiempo.Fecha.comparaFechas(fecha3, fecha2)))
print("El resultado de comparar '" + str(tiempo.Fecha.fechaFormateada(fecha3)) + "' con '" + str(tiempo.Fecha.fechaFormateada(fecha3)) + "' es " + str(tiempo.Fecha.comparaFechas(fecha3, fecha3)))
