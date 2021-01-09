#Mooc.fi - Python-kurssin tehtävä kaupunkipyöristä: lasketaan annettujen asemien välinen suurin etäisyys

import math

def hae_asematiedot(tiedosto:str):
    asemat={}
    with open(tiedosto) as tiedostona:
        for rivi in tiedostona:
            
            osat=rivi.split(";")
            if osat[0]=="Longitude":
                continue
            asemat[osat[3]]=(float(osat[0]),float(osat[1]))
    return(asemat)
        
def etaisyys(asemat: dict, asema1:str, asema2:str):
    longitude1=asemat[asema1][0]
    
    latitude1 = asemat[asema1][1]
    longitude2=asemat[asema2][0]
    latitude2=asemat[asema2][1]
    
    x_kilometreina=(longitude1 - longitude2)*55.26
    y_kilometreina = (latitude1-latitude2)*111.2
    etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)
    return etaisyys
def suurin_etaisyys(asemat:dict):
    #lasketaan kaikkien asemien etäisyys toisiinsa
    
    #palauttaa tuplen(asema1, asema2, etaisyys)
    suurin=0
    mista=""
    mihin=""
    for asema1 in asemat:
        for asema2 in asemat:
            ero=etaisyys(asemat, asema1, asema2)
            if ero > suurin:
                suurin=ero
                mista=asema1
                mihin=asema2
    return mista, mihin, suurin
            


if __name__ == "__main__":
    asemat=hae_asematiedot("stations1.csv")
    asema1, asema2,suurin=suurin_etaisyys(asemat)

    #e=etaisyys(asemat, "Designmuseo", "Hietalahdentori")
    print(asema1, asema2, (round(suurin,2)))