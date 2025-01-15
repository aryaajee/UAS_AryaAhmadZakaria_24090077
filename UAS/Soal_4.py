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
    
mangga = Buah()

mangga.setNama("mangga")
mangga.setWarna("orange")
mangga.setRasa("manis")

print("nama:", mangga.getNama())
print("warna:", mangga.getWarna())
print("rasa:", mangga.getRasa())
