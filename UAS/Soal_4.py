class Buah:
    def __init__(self):
        self.nama = ""
        self.warna = ""
        self.rasa = ""

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def getNama(self):
        return self.nama

    def getWarna(self):
        return self.warna

    def getRasa(self):
        return self.rasa
    
apel = Buah()

apel.setNama("apel")
apel.setWarna("merah")
apel.setRasa("manis")

print("nama:", apel.getNama())
print("warna:", apel.getWarna())
print("rasa:", apel.getRasa())