exceptions = [
    ("ImportError", "Lanzado cuando se intenta importar un elemento que por diversos motivos no puede ser importado."),
    ("NameError", "Lanzado cuando se quiere acceder a un elemento no definido."),
    ("SyntaxError", "Lanzado cuando se encuentra un error sintáctico en el código fuente."),
    ("IndentationError", "Lanzado cuando existen errores en la tabulación."),
    ("TypeError", "Lanzado cuando se intenta tratar un tipo de dato como un tipo diferente."),
    ("KeyboardInterrupt", "Lanzado cuando se interrumpe la ejecución de un script mediante Ctrl+C."),
    ("OSError", "Lanzado cuando una función obtiene un error, generalmente de E/S, desde el sistema operativo."),
    ("RuntimeError", "Lanzado cuando se produce un error en tiempo de ejecución, no capturado por otra excepción."),
    ("IndexError", "Lanzado cuando se intenta acceder al elemento de una colección, que se encuentra fuera de rango."),
    ("KeyError", "Lanzado cuando se quiere acceder a un elemento de un diccionario, cuya clave no existe.")
]

def print_exceptions_table(exceptions):
    print("{:<20} | {}".format("Exception Type", "Description"))
    print("-" * 80)

    for exception_type, description in exceptions:
        print("{:<20} | {}".format(exception_type, description))

print_exceptions_table(exceptions)
