from csv import reader, DictReader, writer, DictWriter


print("===================================================")
print("Print entire file with read()")
with open("file_management_and_manipulation/met.csv", "r") as f:
    data = f.read()
    print(data)


print("===================================================")
print("Print file with reader()")
with open("file_management_and_manipulation/met.csv", "r") as f:
    document = reader(f, delimiter=";", quotechar='"')
    for row in document:
        print(" ".join(row))
        print()


print("===================================================")
print("Print file without headers with reader()")
with open("file_management_and_manipulation/met.csv", "r") as f:
    document = reader(f, delimiter=";", quotechar='"')
    headers = next(document)
    for row in document:
        print(" ".join(row))


print("===================================================")
print("Print file without headers with DictReader()")
with open("file_management_and_manipulation/met.csv", "r") as f:
    document = DictReader(f, delimiter=";", quotechar='"')
    for row in document:
        print(row["DATA"])


print("===================================================")
print("Write in file without headers with write()")
matriz1 = [
    ["Juan", 373, 1970],
    ["Ana", 124, 1983],
    ["Pedro", 901, 1650],
    ["Rosa", 300, 2000],
    ["Juana", 75, 1975],
]
with open("file_management_and_manipulation/data1.csv", "w") as f:
    doc = writer(f, delimiter=";", quotechar='"')
    doc.writerows(matriz1)


print("===================================================")
print("Write in file without headers with DictWriter()")
headers = ["player", "points", "anio"]
matriz2 = [
    dict(player="Juan", points=373, anio=1970),
    dict(player="Ana", points=124, anio=1983),
    dict(player="Pedro", points=901, anio=1650),
    dict(player="Rosa", points=300, anio=2000),
    dict(player="Juana", points=75, anio=1975),
]

with open("file_management_and_manipulation/data2.csv", "w") as f:
    doc = DictWriter(f, delimiter=";", quotechar='"', fieldnames=headers)
    doc.writeheader()
    doc.writerows(matriz2)
