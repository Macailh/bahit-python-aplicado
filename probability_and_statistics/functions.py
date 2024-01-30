# Probability of simple mutually exclusive events
pssme = lambda e: 1.0 / len(e)

# Probability of mutually exclusive compound events
def pscme(e, sc):
    n = len(e)

    return len(sc) / float(n)

# Conditional probability: dependent events
def pscd(e, a, b):
    i = list(set(a).intersection(b))
    pi = pscme(e, i)
    pa = pscme(e, a)
    
    return pi / pa

# Conditional probability: independent events
def psci(e, a, b):
    pa = pscme(e, a)
    pb = pscme(e, b)

    return pa * pb