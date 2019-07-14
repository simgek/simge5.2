class calisan():
    def __init__(self, isim, soyisim,maas,departman, yas = 10):
        print("çalışan sınıfının yapıcı metodu çalıştı")
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.maas = maas
        self.departman = departman


    def __str__(self):
        return "{} {} {}".format(self.isim,self.soyisim,self.yas)

    def bigigoster(self):
        print("çalışan sınıfına ait bilgiler gösterilmektedir")
        print("-"*50)
        print("isim      : {}\nsoyisim   : {}\ndepartman : {}\nmaaş      : {}".format(
            self.isim,self.soyisim,self.departman,self.maas))

    def zamyap(self,zam_orani):
        print("çalışanın maaşına zam yapıldı")
        maas = self.maas
        self.maas += zam_orani
        print("{} {} personelin maaşı : {} tl den {} tl ye yükseldi".format(self.isim,self.soyisim,maas,self.maas))



    def depertmandegistir(self, departman):
        print("çalışanın departmanı değişti")
        departman = self.departman
        self.departman = departman

        print("{} {} personelin departmanı: {} departmanından {} departmanına geçişi sağlandı".format(
            self.isim, self.soyisim,departman,self.departman))


#personelin maaşına zam yapıldığında veya departamnı değiştiğinde kullanıcıya eski değerleri ve yeni değerleri gösterin
#x personelin > departmanından y departmanına geçişi sağlandı
#x personelin maaşı a tl den b tl ye yükseldi










# yas parametresi göndermezsek içeride tnaımlaı sefault değeri geçerli olacaktır

#personel = calisan("simge","karademir")

#personel = calisan("simge ","karademir",9999999,"yazılım",100)
#print(personel)


#personel.zamyap(1000)
#personel.depertmandegistir("ogernci")
#personel.bigigoster()




class yonetici(calisan): # yönetici sınıfına çalışan sınıfını miras veriyoruz
    def __init__(self, isim, soyisim, maas, departman,yas, kisi_sayısı):
        print("yönetici sınıfı yapıcı metodu çalıştı")
        self.isim = isim
        self.soyisim = soyisim
        self.departman = departman
        self.maas = maas
        self.kisi_sayısı = int(kisi_sayısı)
        self.yas = yas

    def print_base(self):
        for base in self.__class__.__bases__:
            print("miras alınan sınıf : ", base.__name__)
    def __str__(self):
        return "{} {} {}".format(self.isim,self.soyisim,self.departman)

Yonetici = yonetici("ahmet","mehmet",9000,"sistem",20,35)
print(Yonetici)
Yonetici.print_base()
Yonetici.bigigoster()
Yonetici.zamyap(10)
Yonetici.depertmandegistir("ogrenci")