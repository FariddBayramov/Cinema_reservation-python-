#NO: 170421993  Name: FARID Surname: BAYRAMOV

Salon = [["-" for x in range(20)] for y in range(20)]  # salon olusturma

def salonyazdirma():
    for i in range(20):
        for j in range(20):
            if (j != 19):
                print(Salon[i][j], "", end="")
            else:
                print(Salon[i][j], "\n", end="")


def rezarvasyon(kategori,bilet_adedi):


    liste = [4, 3, 2, 1, 0, 15, 16, 17, 18, 19]
    if (kategori == 1):
        listee=[]
        if(Salon[9][14])!="X":
            for i in range(0, 10):
                for j in range(5, 15):
                    if (bilet_adedi > 0 and Salon[i][j] == "-"):
                        Salon[i][j] = "X"
                        bilet_adedi = bilet_adedi - 1
                        listee.append(i+1)
                        listee.append("-")
                        listee.append(j+1)
                        listee.append(",")
            print("Rezerve Edilen Koltuklar (Sira-Koltuk) :")
            print("".join(map(str,listee)))
        else:
            print("\nRezervasyon işleminiz reddedildi! (Girdiginiz kategoride tum yerler dolmustur)")
            return -1

    if (kategori == 2):
        listee = []
        if(Salon[9][19]!="X"):
            for i in range(0, 10):
                for j in liste:
                    if (bilet_adedi > 0 and Salon[i][j] == "-"):
                        Salon[i][j] = "X"
                        bilet_adedi = bilet_adedi - 1
                        listee.append(i + 1)
                        listee.append("-")
                        listee.append(j + 1)
                        listee.append(",")
            print("Rezerve Edilen Koltuklar (Sira-Koltuk) :")
            print("".join(map(str,listee)))
        else:
            print("\nRezervasyon işleminiz reddedildi! (Girdiginiz kategoride tum yerler dolmustur) ")
            return -1

    if (kategori == 3):
        listee = []
        if (Salon[19][14] != "X"):
            for i in range(10, 20):
                for j in range(5, 15):
                    if (bilet_adedi > 0 and Salon[i][j] == "-"):
                        Salon[i][j] = "X"
                        bilet_adedi = bilet_adedi - 1
                        listee.append(i + 1)
                        listee.append("-")
                        listee.append(j + 1)
                        listee.append(",")
            print("Rezerve Edilen Koltuklar (Sira-Koltuk) :")
            print("".join(map(str,listee)))
        else:
            print("\nRezervasyon işleminiz reddedildi! (Girdiginiz kategoride tum yerler dolmustur) ")
            return -1

    if (kategori == 4):
        listee = []
        if (Salon[19][19] != "X"):
            for i in range(10, 20):
                for j in liste:
                    if (bilet_adedi > 0 and Salon[i][j] == "-"):
                        Salon[i][j] = "X"
                        bilet_adedi = bilet_adedi - 1
                        listee.append(i + 1)
                        listee.append("-")
                        listee.append(j + 1)
                        listee.append(",")
            print("Rezerve Edilen Koltuklar (Sira-Koltuk) :", end="")
            print("".join(map(str,listee)))
        else:
            print("\nRezervasyon işleminiz reddedildi! (Girdiginiz kategoride tum yerler dolmustur) ")
            return -1

ciro={1:0,2:0,3:0,4:0}

def fiyathesaplama(bilet, kat):
    global indirim
    global ciro
    liste = []
    file = open("indirim.txt", "r")
    for i in file:
        liste.append(i)
    for i in range(len(liste)):
        liste[i] = liste[i].replace("\n", "")
    myList = []
    for i in liste:
        myList.append(i.split("-"))
    max = int(myList[0][1])
    net=0
    if (bilet < int(myList[5 + 3 * (kat - 1)][1])):
        net = bilet * int(myList[kat][1])
        indirim=0
    elif (bilet >= int(myList[5 + 3 * (kat - 1)][1]) and bilet <= int(myList[5 + 3 * (kat - 1)][2])):
        net = bilet * (100 - int(myList[5 + 3 * (kat - 1)][3])) * int(myList[kat][1]) / 100
        indirim=int(myList[5 + 3 * (kat - 1)][3])
    elif (bilet >= int(myList[6 + 3 * (kat - 1)][1]) and bilet <= int(myList[6 + 3 * (kat - 1)][2])):
        net = bilet * (100 - int(myList[6 + 3 * (kat - 1)][3])) * int(myList[kat][1]) / 100
        indirim=int(myList[6 + 3 * (kat - 1)][3])
    elif (bilet >= int(myList[7 + 3 * (kat - 1)][1]) and bilet <= max):
        net = bilet * (100 - int(myList[7 + 3 * (kat - 1)][3])) * int(myList[kat][1]) / 100
        indirim=int(myList[7 + 3 * (kat - 1)][3])
    toplam = bilet * int(myList[kat][1])

    print("Toplam tutar: ",toplam)
    print("Yapılan indirim: %",indirim)
    print("Net tutar: ",net)

    return  net

def yenietkinlik():
    for i in range(20):
        for j in range(20):
            Salon[i][j] = "-"
    print("\n\n* Salon yeni etkinlik için hazır *\n")


def anamenuyazdirma():
    print("\n****************\n"
          "**  ANA MENÜ  **\n"
          "****************\n"
          "1.Rezervasyon\n"
          "2.Salonu Yazdır\n"
          "3.Yeni Etkinlik\n"
          "4.Toplam Ciro\n"
          "0.Çıkış\n")


anamenuyazdirma()
secim = int(input("Seçiminiz  ?\n"))
if (secim < 0 or secim > 4):
    print("Lütfen listedeki sayılar üzerinden seçim yapınız..")
if (secim == 0):
    print("Uygulama kapatıldı...")
if (secim == 1):
    kategori = int(input("Kategori (1-4) ? "))
    if (kategori < 0 or kategori > 4):
        print("Girdiginiz kategori verilen aralıkta değildir...\n")
    if (kategori > 0 and kategori < 5):
        bilet_adedi = int(input("Bilet adedi (1-30) ?"))
        if (bilet_adedi < 0 or bilet_adedi > 30):
            print("Girdiginiz bilet sayısı verilen aralıkta değildir...\n")
        else:
            if(rezarvasyon(kategori,bilet_adedi)!=-1):
                print("\nBilet adedi:",bilet_adedi)
                ciro[kategori] += fiyathesaplama(bilet_adedi, kategori)
    anamenuyazdirma()
if (secim == 2):
    salonyazdirma()
    anamenuyazdirma()
if (secim == 3):
    yenietkinlik()
    ciro[1]=0
    ciro[2]=0
    ciro[3]=0
    ciro[4]=0
    anamenuyazdirma()
if (secim == 4):
    print("1.Kategori Ciro= ", ciro[1])
    print("2.Kategori Ciro= ", ciro[2])
    print("3.Kategori Ciro= ", ciro[3])
    print("4.Kategori Ciro= ", ciro[4])
    print("Toplam ciro= ", sum(ciro.values()))

while (secim != 0):
    secim = int(input("Başka bir seçim için (1-2-3-4) çıkış için 0`a basınız: \n"))
    if (secim < 0 or secim > 4):
        print("Lütfen listedeki sayılar üzerinden seçim yapınız..")
    if (secim == 0):
        print("Uygulama kapatıldı...")
    if (secim == 1):
        kategori = int(input("Kategori (1-4) ? "))
        if (kategori < 0 or kategori > 4):
            print("Girdiginiz kategori verilen aralıkta değildir...\n")
        if (kategori > 0 and kategori < 5):
            bilet_adedi = int(input("Bilet adedi (1-30) ?"))
            if (bilet_adedi < 0 or bilet_adedi > 30):
                print("Girdiginiz bilet sayısı verilen aralıkta değildir...\n")
            else:
                if (rezarvasyon(kategori, bilet_adedi) != -1):
                    print("\nBilet adedi:", bilet_adedi)
                    ciro[kategori] += fiyathesaplama(bilet_adedi, kategori)

        anamenuyazdirma()
    if (secim == 2):
        salonyazdirma()
        anamenuyazdirma()
    if (secim == 3):
        yenietkinlik()
        ciro[1] = 0
        ciro[2] = 0
        ciro[3] = 0
        ciro[4] = 0
        anamenuyazdirma()
    if (secim == 4):
            print("1.Kategori Ciro= ",ciro[1])
            print("2.Kategori Ciro= ", ciro[2])
            print("3.Kategori Ciro= ", ciro[3])
            print("4.Kategori Ciro= ", ciro[4])
            print("Toplam ciro= ",sum(ciro.values()))
