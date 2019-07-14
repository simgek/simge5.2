a = 40  # değeri kırk olan sayısal bir <class 'int'> tipinde bir değişken

b = a   # b değişkeni tanımlayıp referansını a değişkeninden aldık
c = [b] # c değişkenini tanımlayıp <class 'list> b değerini referans olarak verdik

print(type(a))
print(a)

del a        # a değişkeninin referansını sildik
b = 100       # b değerine 100 değerini vererküzerinde yer alan 40 değerini değiştirdik
print(type(c))
c[0] = -1    # c listesinin 0. elemanın değerini -1 olarak değiştirerek 40 değerini sildik
# ve a değişkeine ait hiç bir referans kalmamıştır
print(c[0])


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "heap üzerinden silindi")

pt1 = Point()
pt2 = pt1
pt3 = pt1

print(id(pt1), id(pt2), id(pt3)) # nesnenin ram adresi değerinin ekrana yazdırılması


del pt1
print( id(pt2), id(pt3))

# id() nesnenin kimliğini döndürür nesne yaşam ömrü boyunca benzersiz ve sabit olacağı garantilenen (uniq) bir tam sayıdır
# biribirinden benzersiz iki nesne aynı değere sahip olabilirler


