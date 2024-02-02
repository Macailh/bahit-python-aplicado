# Bayes theorem
def bayes(e, b):
    n = float(sum(e))
    pa = [h / n for h in e]
    pi = [k / n for k in b]
    pba = [pi[i] / pa[i] for i in range(len(pi))]
    prods = [pa[i] * pba[i] for i in range(len(pa))]
    ptb = sum(prods)
    pab = [p / ptb for p in prods]

    return pab