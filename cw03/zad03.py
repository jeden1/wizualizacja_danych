produkty = {
    'ziemniaki': 'kg',
    'chleb': 'szt',
    'lody': 'szt',
    'sok pomarańczowy': 'litr',
}

produkty_sztuki = {
    {produkt: wartosc} for produkt, wartosc in produkty.items() if wartosc == 'sztuki'
}
print(produkty_sztuki)