from tabulate import tabulate

table_one = [
    ["Caracteres de posición", "Cuantificadores"],
    ["^ Inicio de cadena", "? Cero o uno"],
    ["$ Final de cadena", "* Cero o más"],
    ["", "+ Uno o más"],
    ["", "{n} n veces"],
    ["", "{n,} n o más veces"],
    ["", "{,m} Entre 0 y n veces"],
    ["", "{n,m} Entre n y m veces"],
]

print(tabulate(table_one, headers="firstrow", tablefmt="fancy_grid"))

table_two = [
    ["Agrupamiento", "(...) Grupo exacto"],
    ["", "[...] Caracteres opcionales y rangos"],
    ["", "| Operador lógico «or» (A|B)"],
    ["", "- Usado para expresar un rango [a-z]"],
    [
        "Caracteres de formato",
        "\\ Caracter de escape para expresar literales: \\. (literal del carácter punto)",
    ],
    ["", "\\d Dígito NOTA"],
    ["Caracteres de posición", ". Cualquier carácter excepto el salto de línea"],
    ["", "\\n Salto de línea"],
    ["", "\\s Espacio en blanco NOTA"],
    ["", "\\w Palabra NOTA"],
    [
        "NOTA: En mayúsculas significa lo contrario.",
        "Por ejemplo, \\S simboliza cualquier carácter que no sea un espacio en blanco",
    ],
]

print(
    tabulate(
        table_two, headers=["Expresión Regular", "Descripción"], tablefmt="fancy_grid"
    )
)
