print("5 adet sayı giriniz:")
for i in range(5):
    d = input()
    deger = int(d)
    tut = False

    if deger==1:
        print(deger, end=" ")
        print("Asal değil")
        continue;
    else:
        for k in range(2,deger):
            if deger%k==0:
                tut= True
                break;
            else:
                tut=False
    
    if tut==True:
        print(deger, end=" ")
        print("Asal değil")
    else:
        print(deger, end=" ")
        print("Asal")
