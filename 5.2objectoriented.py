#__init__ constructor yapıcı metot


class Personel:
    isim    = ""
    soyisim = ""
    yas     = 0

    def __str__(self):
        return "{} {}".format(self.isim,self.soyisim)

    def __init__(self, firstname, lastname, age):
        self.isim = firstname
        self.soyisim = lastname
        self.yas = age

# __init__ metodu çalıştığından

#personel = Personel()
#personel.isim = "simge"
#personel.soyisim = "karademir"
#personel.yas = 100

#print(personel)

employee = Personel("simge","karademir",100)
print(employee)
emp = employee