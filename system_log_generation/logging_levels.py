logging_levels = [
    ("DEBUG", 10, "Utilizado generalmente para monitorizar el funcionamiento de un programa, permitiendo "
                   "depurar un programa durante su ejecución normal, a fin de obtener la información deseada para "
                   "efectuar un diagnóstico determinado."),
    ("INFO", 20, "Utilizado para registrar eventos afirmativos, es decir, mantener un registro detallado, de ciertas "
                 "acciones ejecutadas en la aplicación, de forma satisfactoria."),
    ("WARNING", 30, "Utilizado para emitir una alerta sobre un evento determinado, permitiendo grabar en el archivo "
                    "de registros, información que, sin representar un error o momento crítico de fallo, podría ser "
                    "indicativa de un posible fallo, error, o acción no deseada. Generalmente útil en advertencias de "
                    "seguridad."),
    ("ERROR", 40, "Utilizado para registrar un error cuando el programa no logra llevar a cabo una acción esperada."),
    ("CRITICAL", 50, "Utilizado para registrar un error que frene la ejecución normal del programa. Suele emplearse "
                      "cuando errores fatales son capturados, y la ejecución normal del programa se ve impedida.")
]

def print_logging_levels_table(logging_levels):
    print("{:<8} | {:<5} | {}".format("LEVEL", "Value", "Description"))
    print("-" * 90)

    for level, value, description in logging_levels:
        wrapped_description = "\n          |       | ".join(description[i:i+65] for i in range(0, len(description), 65))
        print("{:<8} | {:<5} | {}".format(level, value, wrapped_description))

print_logging_levels_table(logging_levels)
