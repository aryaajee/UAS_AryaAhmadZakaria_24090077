class AntrianPesanan:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        'menambahkan pesanan ke dalam antrian.'
        self.antrian.append(pesanan)
        print(f'pesanan '{pesanan}' telah ditambahkan ke antrian.')

    def dequeue(self):
        'menghapus pesanan dari depan antrian.'
        if self.is_empty():
            print('antrian kosong, tidak ada pesanan yang bisa dihapus.')
        else:
            pesanan = self.antrian.pop(0)
            print(f'pesanan '{pesanan}' telah dihapus dari antrian.')

    def is_empty(self):
        'mengecek apakah antrian kosong'
        return len(self.antrian) == 0

    def tampilkan_antrian(self):
        'menampilkan semua pesanan dalam antrian'
        if self.is_empty():
            print('Antrian kosong')
        else:
            print('Antrian pesanan saat ini:')
            for i, pesanan in enumerate(self.antrian, start=1):
                print(f'{i}. {pesanan}')


antrian = AntrianPesanan()

antrian.enqueue('Pesanan 1')
antrian.enqueue('Pesanan 2')
antrian.enqueue('Pesanan 3')

antrian.tampilkan_antrian()

antrian.dequeue()
antrian.tampilkan_antrian()

antrian.dequeue()
antrian.dequeue()
antrian.tampilkan_antrian()