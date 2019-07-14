class Cup1:
    def __init__(self):
        self.color = None     # public variable
        self.content = None   #public variable

    def fill(self,beverage):
        self.content = beverage
    def empty(self):
        self.content = None
    def __str__(self):
        return self.color + " " + self.content

cup1 = Cup1()
cup1.color = "red"
cup1.content = "tea"

print(cup1)
cup1.empty()
cup1.content = "coffee"
print(cup1)


class Cup2:
    def __init__(self):
        self.color = None # public variable
        self._content = None # protected variable

# korumalı üye C# gibi dillerde miras alınan sınıflarda görünsede python dilinde
# tel bir _ ç,zgisi varsa bana dokunma anlamına gelir


    def fill(self,bevarage):
        self._content = bevarage
    def empty(self):
        self._content = None
    def __str__(self):
        return self.color + " " + self._content

cup2 = Cup2()
cup2.color = "blue"
cup2._content = "tea"

print(cup2)







class Cup3:
    def __init__(self,color):
        self._color = color # protected variable
        self.__content = None # private  variable



    def fill(self,bevarage):
        self.__content = bevarage;
    def empty(self):
        self.__content = None
    def __str__(self):
        return self._color + " " + self.__content

cup3 = Cup3("blue")
#cup3._Cup3__content = "tea"
cup3._Cup3__content = "çay"

print(cup3)