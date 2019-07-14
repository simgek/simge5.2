class parentclass():
    def send_message(self):
        print("bu alan içerisnde mesaj verilecektir")




class basedclass(parentclass):
    def send_message(self):
        print("base class üzerinden glen mesaj")

parent = parentclass()
parent.send_message()


base = basedclass()
base.send_message()

