def duplikat(wejscie):
    wyjscie=[]
    for slowo in wejscie: 
        if slowo not in wyjscie:
            wyjscie.append(slowo)
    return wyjscie
slowa=['kot', 'pies', 'mysz', 'kot', 'kot', 'mlot', 'pies']
tablica=duplikat(slowa)
print tablica
