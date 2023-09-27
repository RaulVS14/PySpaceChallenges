def vokaalid(uuritav):
    tähed = "AEIOUÕÄÖÜ"
    return "".join(filter(lambda x: x.upper() in tähed, list(uuritav)))
    

if __name__ == "__main__":
    print(vokaalid("Tere"))
    print(vokaalid("OtotOtot"))
    print(vokaalid("Brrr"))
