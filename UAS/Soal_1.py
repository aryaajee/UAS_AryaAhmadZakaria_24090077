data_mahasiswa = []

while True:
    print('Menu:')
    print('1. Masukkan Data Mahasiswa')
    print('2. Tampilkan Data Mahasiswa')
    print('3. Keluar')
    
    pilihan=input('Pilih menu (1/2/3):')
    if pilihan == '1a':
        while True:
            nim = input('Masukkan NIM: ')
            nama = input('Masukkan Nama:')
            data_mahasiswa.append({'nim': nim, 'nama': nama})
            
            tambah_lagi = input('Ingin tambah lagi? (y/t):').lower()
            if tambah_lagi != 'y':
                break
    elif pilihan == '2':
        if len(data_mahasiswa) == 0:
            print('Tidak ada data mahasiswa')
        else:
            print('Data Mahasiswa:')
            for idx, mahasiswa in enumerate(data_mahasiswa,start=1):
                print(f'{idx}. NIM: {mahasiswa['nim']}, Nama:{mahasiswa['nama']}')
    elif pilihan == '3':
        print('Terima kasih, program selesai')
        break
    else:
        print('Pilihan tidak valid. Silakan pilih lagi')