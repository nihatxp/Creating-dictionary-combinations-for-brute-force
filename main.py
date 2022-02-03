import itertools
import keyboard
#harfler = 'AaBbCcÇçDdEeFfGgĞğHhİiIıJjKkLIMmNnOoÖöPpRrSsŞşTtUuÜüVvYyZz'
sayi=int(input("kac ozellik eklemek istiyorsunuz"))
minHarfSayi=int(input("en az kac harfli olsun?"))
maxHarfSayi=int(input("en cok kac harfli olsun?"))
ozellikler=[]
if keyboard.is_pressed('q'):
    print('Kaydedildi!')
for i in range(sayi):
    a=input("ozellik:")
    ozellikler.append(a)
    print(ozellikler)
            
    
dosya=open("index.txt","w")
for i in itertools.product(ozellikler, repeat=2):
    sefer="".join(i)
    if len(sefer)>maxHarfSayi:
        continue
    if len(sefer)<minHarfSayi:
        continue
    dosya.write(sefer)
    dosya.write("\n")
    print(sefer)


for i in itertools.product(ozellikler, repeat=3):
    sefer="".join(i)
    if len(sefer)>maxHarfSayi:
        continue
    if len(sefer)<minHarfSayi:
        continue
    dosya.write(sefer)
    dosya.write("\n")
    print(sefer)
    if keyboard.is_pressed('q'):
        print('Kaydedildi!')
        dosya.close()
        break
    
for t in ozellikler:  #ozelliklerin icindeki kelimeleri son olarak ekliyorum
    if len(t)>maxHarfSayi:
        continue
    if len(t)<minHarfSayi:
        continue
    else:
        print(t)
        dosya.write(t)
        dosya.write("\n")
dosya.close()


