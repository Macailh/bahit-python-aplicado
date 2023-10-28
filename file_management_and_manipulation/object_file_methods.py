# Data for the table
data = [
    ("Método", "Descripción"),
    (
        "read([bytes])",
        "Lee todo el contenido de un archivo. Si se le pasa la longitud de bytes, leerá solo el contenido hasta la longitud especificada.",
    ),
    ("readlines()", "Lee todas las líneas de un archivo."),
    ("write(cadena)", "Escribe la cadena en el archivo."),
    (
        "writelines(secuencia)",
        "La secuencia debe ser cualquier iterable cuyos elementos se escribirán uno por línea.",
    ),
]

# Calculate column widths
column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

# Print column headers
for i, header in enumerate(data[0]):
    print(f"{header:{column_widths[i]}}", end=" | ")
print()  # Newline

# Print separator
for width in column_widths:
    print("-" * width, end=" | ")
print()  # Newline

# Print data rows
for row in data[1:]:
    for i, value in enumerate(row):
        print(f"{value:{column_widths[i]}}", end=" | ")
    print()  # Newline
