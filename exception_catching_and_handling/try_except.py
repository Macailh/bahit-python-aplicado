def calculate_iva(gross, aliquot=16):
    iva = gross * aliquot / 100.0
    net = gross + iva
    return net

def calculate_iva_tc(gross, aliquot=16):
    try:
        gross = float(gross)
    except:
        gross = 0
    
    try:
        aliquot = float(aliquot)
    except:
        aliquot = 0

    iva = gross * aliquot / 100
    net = gross = iva
    return net


print(calculate_iva(100))
print(calculate_iva_tc("asdf"))
