import random

def ambil_soal():
    semua_soal = []
    with open('bank_soal.txt', 'r') as data:
        for line in data:
            semua_soal.append(line.strip())
            
    return semua_soal

def buat_soal():
    semua_soal = ambil_soal()
    random.shuffle(semua_soal)
    
    soal_ujian = []
    
    for s in range(10):
        soal = semua_soal[s].split('|')
        pertanyaan = soal[0]
            
        semua_jawaban = soal[1]
        jawaban = semua_jawaban.split(',')
        jawaban_benar = jawaban[0]
        random.shuffle(jawaban)
        
        soal_ujian.append({
            'pertanyaan': pertanyaan,
            'jawaban': jawaban,
            'jawaban_benar': jawaban_benar
        })
            
    return soal_ujian
         
def main():
    soal_ujian = buat_soal()
    soal_benar = 0
    soal_salah = 0
    
    for s in range(len(soal_ujian)):
        soal = soal_ujian[s]
        opsi_jawaban = ['a', 'b', 'c', 'd']
    
        print(f'Pertanyaan {s+1}: {soal['pertanyaan']}')
        
        for j in range(len(soal['jawaban'])):
            print(f'{opsi_jawaban[j]}. {soal['jawaban'][j]}')
            
            
        jawaban_user = input('Masukan Jawaban: (a,b,c,d): ')
        jawaban_user_index = opsi_jawaban.index(jawaban_user)
        jawaban_asli_user = soal['jawaban'][jawaban_user_index]

        if soal['jawaban_benar'] == jawaban_asli_user:
            print('Jawaban anda benar 🌟🌟🌟')
            soal_benar += 1
        else:
            print('Jawaban anda salah 🥲🥲🥲')
            soal_salah += 1
    
    print(f'Ujian anda berakhir skor anda adalah {(len(soal_ujian) - soal_salah) * 10} %')
    
    
print('==== Selamat  Datang ====')
print('=== Di Aplikasi Ujian ===')
print('1. Ujian')
print('2. Keluar')
menu = int(input('Masukan opsi: '))

if menu == 1:
    main()
elif menu == 2:
    exit()
    
print('TerimaKasih')
