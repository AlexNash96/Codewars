def nb_year(p0, percent, aug, p):
    years = 0
    percent = percent/100
    while p0 < p:
        p0 = p0 * (1+percent) + aug
        p0 = int(p0)
        years = years+1
    return years

def test_answer():
    assert nb_year(1500, 5, 100, 5000) == 15
    assert type(nb_year(1500, 5, 100, 5000)) is int
    assert nb_year(1500000, 2.5, 10000, 2000000) == 10
    assert type(nb_year(1500000, 2.5, 10000, 2000000)) is int