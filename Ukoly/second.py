def cislo_text(x):
    n = int(x)
    jedn = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    d_cisla = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    des = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    #pro 0 a 10 delame "..." dvakrat 
    if n == 100:
        return "sto"
    elif n < 10:
        return jedn[n]
    elif 10 <= n < 20:
        return d_cisla[n-10]
    else: 
        des_cast = n // 10
        jedn_cast = n % 10
        if jedn_cast == 0:
             return des[des_cast]
        else:
            return des[des_cast] + " " + jedn[jedn_cast]
if __name__ == "__main__":
    print(cislo_text("0"))
    print(cislo_text("1"))        
    print(cislo_text("15"))
    print(cislo_text("25"))
    print(cislo_text("100"))