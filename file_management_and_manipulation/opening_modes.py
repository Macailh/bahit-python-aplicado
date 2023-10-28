# Data for the table
data = [
    ("Indicador", "Modo de apertura", "Ubicación del puntero"),
    ("r", "Solo lectura", "Al inicio del archivo"),
    ("rb", "Solo lectura en modo binario", "Al inicio del archivo"),
    ("r+", "Lectura y escritura", "Al inicio del archivo"),
    ("rb+", "Lectura y escritura en modo binario", "Al inicio del archivo"),
    (
        "w",
        "Solo escritura",
        "Sobrescribe el archivo si existe. Crea el archivo si no existe. Al inicio del archivo",
    ),
    (
        "wb",
        "Solo escritura en modo binario",
        "Sobrescribe el archivo si existe. Crea el archivo si no existe. Al inicio del archivo",
    ),
    (
        "w+",
        "Escritura y lectura",
        "Sobrescribe el archivo si existe. Crea el archivo si no existe. Al inicio del archivo",
    ),
    (
        "wb+",
        "Escritura y lectura en modo binario",
        "Sobrescribe el archivo si existe. Crea el archivo si no existe. Al inicio del archivo",
    ),
    (
        "a",
        "Añadido (agregar contenido)",
        "Crea el archivo si éste no existe. Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.",
    ),
    (
        "ab",
        "Añadido en modo binario (agregar contenido)",
        "Crea el archivo si éste no existe. Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.",
    ),
    (
        "a+",
        "Añadido (agregar contenido) y lectura",
        "Crea el archivo si éste no existe. Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.",
    ),
    (
        "w+",
        "Escritura y lectura",
        "Sobrescribe el archivo si existe. Crea el archivo si no existe. Al inicio del archivo",
    ),
    (
        "ab+",
        "Añadido (agregar contenido) y lectura en modo binario",
        "Crea el archivo si éste no existe. Si el archivo existe, al final de éste.",
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
