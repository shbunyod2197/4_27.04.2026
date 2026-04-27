# # 1-masala
class Inson:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def malumot(self):
        print(self.ism)
        print(self.yosh)


class Talaba(Inson):
    def __init__(self, ism, yosh, universitet):
        super().__init__(ism, yosh)
        self.universitet = universitet

    def malumot(self):
        super().malumot()
        print(self.universitet)


t = Talaba("Ali", 20, "TATU")
t.malumot()


## 2-masala
class Hayvon:
    def __init__(self, nomi):
        self.nomi = nomi

    def ovoz(self):
        print("Noma'lum ovoz")

class It(Hayvon):
    def __init__(self, nomi, zoti):
        super().__init__(nomi)
        self.zoti = zoti

    def ovoz(self):
        print(f"Nomi: {self.nomi}")
        print(f"Zoti: {self.zoti}")
        print("Vov-vov")

i = It("Rex", "Ovchi")
i.ovoz()

## 3-masala
class Transport:
    def __init__(self, nomi, tezlik):
        self.nomi = nomi
        self.tezlik = tezlik

    def info(self):
        print(self.nomi, self.tezlik)

class Mashina(Transport):
    def __init__(self, nomi, tezlik, yoqilgi):
        super().__init__(nomi, tezlik)
        self.yoqilgi = yoqilgi


    def info(self):
        super().info()
        print(self.yoqilgi)


m = Mashina("Cobalt", 180, "benzin")
m.info()

## 4-masala
class Xodim:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

    def info(self):
        print(self.ism, self.maosh)

class Dasturchi(Xodim):
    def __init__(self, ism, maosh, til):
        super().__init__(ism, maosh)
        self.til = til

    def info(self):
        super().info()
        print(self.til)


d = Dasturchi("Aziz", 500, "Python")
d.info()

## 5-masala
class Telefon:
    def __init__(self, model):
        self.model = model

    def info(self):
        print(self.model)

class Smartfon(Telefon):
    def __init__(self, model, xotira):
        super().__init__(model)
        self.xotira = xotira

    def info(self):
        super().info()
        print(self.xotira)

s = Smartfon("iPhone", "256GB")
s.info()

