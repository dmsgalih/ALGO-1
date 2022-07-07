import os
import json
from datetime import datetime as dt



def awal():
    os.system('cls')
    print('\n\n\n\n\n\n\n')
    print(' '*28,'##'+' '*7+'##',' '+'##'+' '*9+'##',' '*7+'##'+' '*5+'##',' '+'##'*4,' '+'##'*5,' ##',' '+'#'*8,' '+'#'*8)
    print(' '*28,'## #   # ##',' '+'##'+' '*9+'##',' '*7+'## #'+' '*3+'##',' ##'+' '*4+'##',' '*5+'##',' '*5+'##',' ##',' '*7+'##')
    print(' '*28,'##'+' '*3+'#'+' '*3+'##',' '+'##'+' '*9+'##',' '*7+'##   # ##',' ##'+' '*4+'##',' '*5+'##',' '*5+'##',' ##',' '*7+'#'*8)
    print(' '*28,'##'+' '*7+'##',' '+'#'*13,' '*7+'##     ##',' ##'+' '*4+'##',' '*5+'##',' '*5+'##',' ##',' '*7+'##')
    print(' '*28,'##'+' '*7+'##',' '+' '*11+'##',' '+'####'+' '*2+'##'+' '*5+'##',' '+'##'*4,' '*5+'##',' '*5+'##',' '+'#'*8,' '+'#'*8)
    print(' '*53+'##')
    print(' '*28+'#'*27)
    print('\n\n\n')
    input('{:^150s}'.format('Press Enter\n\n\n\n\n\n\n\n\n'))


def login():
    awal_index = 0
    while awal_index < 3:
        os.system('cls')
        print('{:^135}'.format('##'+' '*6+'#'+'#'*6+'#'+'  '+'#'+'#'*7+'  '+'##'+'  '+'##'+' '*5+' ##'))
        print('{:^135}'.format('##'+' '*6+'##'+' '*4+'##'+'  '+'##'+' '*8+'##'+'  ## #'+' '*3+' ##'))
        print('{:^135}'.format('##'+' '*6+'##'+' '*4+'##'+'  '+'#'*8+'  '+'##'+'  ##   #  ##'))
        print('{:^135}'.format('##'+' '*6+'##'+' '*4+'##'+'  '+'##'+' '*4+'##'+'  ##  ##'+' '*4+' ###'))
        print('{:^135}'.format('#'*6+'  '+'#'*8+'  '+'#'*8+'  '+'##'+'  '+'##'+' '*5+' ##'))
        print('\n\n\n\n\n')
        spasi = ' '
        username = input('{}Username : '.format(spasi*58))
        password = input('{}Password : '.format(spasi*58))
        list_username = ['3513131202005132', '2222222222222222', '3333333333333333', '4444444444444444']
        if username in list_username and len(password)==6:
            break
        awal_index+=1
    else:
        print('\n\n\n\n\n\n{:^133}\n\n\n\n\n\n\n\n\n\n'.format('MAAF, Anda Telah Melakukan Terlalu Banyak Percobaan'))
        exit()

def load(filename):
    try:
        with open(filename, 'r') as file:
            isi = json.load(file)
        return isi
    except :
        try:
            with open(filename, 'w') as file:
                json.dump([], file, indent=4)
        except IOError as e:
            print(e)


def write(data, filename):
    try:
        isi = load(filename)
        isi.append(data[0])
        with open(filename, 'w') as file:
            json.dump(isi, file, indent=4)

    except IOError as e:
        print(e)


def show(filename):
    print('-'*142)
    print('| {:^4s} |   {:^7s}    |  {:^18s}     | {:^20s} |   {:^17}   |  {:^17}  |   {:^17}   |'.format('No', 'Tanggal', 'Keterangan', 'Jumlah Transaksi', 'Keluar', 'Masuk', 'Saldo'))
    print('-'*7+'+'+'-'*14+'+'+'-'*25+'+'+'-'*22+'+'+'-'*23+'+'+'-'*21+'+'+'-'*24)
    isi = load(filename)
    kredit_list = []
    debet_list = []
    i = 0
    saldo = 0
    while i < len(isi):
        if isi[i]['Debet']=='-':
            saldo += isi[i]['Kredit']
            kredit_list.append(isi[i]['Kredit'])
            print('| {:<4} |  {:^7s}  | {:<20s}    | {:<20s} | {:^21} | {:^19} | {:<21} |'.format(i+1, isi[i]['Tanggal'], isi[i]['Keterangan'], isi[i]['Jumlah'], isi[i]['Debet'], 'Rp {:,}'.format(isi[i]['Kredit']), 'Rp {:,}'.format(saldo)))
        elif isi[i]['Kredit']=='-':
            saldo -= isi[i]['Debet']
            debet_list.append(isi[i]['Debet'])
            print('| {:<4} |  {:^7s}  | {:<20s}    | {:<20s} | {:<21} | {:^19} | {:<21} |'.format(i+1, isi[i]['Tanggal'], isi[i]['Keterangan'], isi[i]['Jumlah'], 'Rp {:,}'.format(isi[i]['Debet']), isi[i]['Kredit'], 'Rp {:,}'.format(saldo)))
        i+=1
    print('-'*71+'+'+'-'*23+'+'+'-'*21+'+'+'-'*24)
    print('|{:^70}| {:<21} | {:<19} | {:^21} |'.format('Jumlah', 'Rp {:,}'.format(sum(debet_list)), 'Rp {:,}'.format(sum(kredit_list)), ' '))
    print('-'*142)


def tambah():
    os.system('cls')
    print(' '*45,'##',' ##'+' '*6+'##',' '+'##'*3,' '+'##'*3,' '+'##'*3,' '+'##'*5)
    print(' '*45,'##',' ## #'+' '*4+'##',' ##',' '*5+'##',' '*5+'##'+' '*3+'##',' '+' '*3+'##')
    print(' '*45,'##',' ##'+' '*3+'#  ##',' '+'##'*3,' '+'##'*3,' '+'##'*3,' '+'  '*2+'##')
    print(' '*45,'##',' ##'+' '*5+'###',' '*5+'##',' ##',' '*5+'## #',' '+'  '*3+'##')
    print(' '*45,'##',' ##'+' '*6+'##',' '+'##'*3,' '+'##'*3,' '+'##   #',' '+'  '*2+'##\n')
    

def insert(filename):
    i = 0
    tambah()
    show(filename)
    print('\nData Tambahan \n')
    tanggal = dt.now().strftime('%Y-%m-%d')
    keterangan = input('Keterangan       : ')
    jumlah = input('Jumlah Transaksi : ')
    total = int(input('Jumlah Uang      : Rp '))
    while True:
        tambah()
        show(filename)
        print('\nData Tambahan \n')
        print(f'Keterangan       : {keterangan}')
        print(f'Jumlah Transaksi : {jumlah}')
        print(f'Jumlah Uang      : Rp {total}')
        print('''Jenis Transaksi :
        1. Pengeluaran 
        2. Penerimaan \n\n ''')
        if i>=1:
            print('Maaf, masukkan anda tidak valid\n')
        pilihan_transaksi = input('Pilih Transaksi : ')
        if pilihan_transaksi=='1':
            debet = total
            kredit = '-'
            break
        elif pilihan_transaksi=='2':
            debet = '-'
            kredit = total
            break
        i += 1

    kosong_dict = {'Tanggal':tanggal, 'Keterangan':keterangan, 'Jumlah':jumlah, 'Debet':debet, 'Kredit':kredit,}
    kosong_list = [kosong_dict]
    write(kosong_list, filename)


def preview(index, filename):
    isi = load(filename)
    print('-'*118)
    print('| {:^4s} |   {:^7s}    |  {:^18s}     | {:^20s} |   {:^17}   |  {:^17}  |'.format('No', 'Tanggal', 'Keterangan', 'Jumlah Transaksi', 'Keluar', 'Masuk'))
    print('-'*7+'+'+'-'*14+'+'+'-'*25+'+'+'-'*22+'+'+'-'*23+'+'+'-'*22)
    if isi[index]['Debet']=='-':
        print('| {:<4} |  {:^7s}  | {:<20s}    | {:<20s} | {:<21} | {:^19} |'.format(index+1, isi[index]['Tanggal'], isi[index]['Keterangan'], isi[index]['Jumlah'], isi[index]['Debet'], 'Rp {:,}'.format(isi[index]['Kredit'])))
    elif isi[index]['Kredit']=='-':
        print('| {:<4} |  {:^7s}  | {:<20s}    | {:<20s} | {:<21} | {:<19} |'.format(index+1, isi[index]['Tanggal'], isi[index]['Keterangan'], isi[index]['Jumlah'], 'Rp {:,}'.format(isi[index]['Debet']), isi[index]['Kredit']))
    print('-'*118)


def ganti():
    os.system('cls')
    print(' '*41,'##'+' '*4+'##', '  '+'#'*6, '  '+'#'*4, ' '*4+'    #    ', ' '+'#'*10, ' '+'#'*6)
    print(' '*41,'##'+' '*4+'##', '  '+'##   ##', ' ##  ##', '  '+' ##   ## ', ' '+' '*4+'##'+' '*4, ' '+'##')
    print(' '*41,'##'+' '*4+'##', '  '+'#'*6, '  ##    #', ' ##     ##', ' '+' '*4+'##'+' '*4, ' '+'#'*6)
    print(' '*41,'##'+' '*4+'##', '  ##', ' '*6+'##  ##', '  '+'## ### ##', ' '+' '*4+'##'+' '*4, ' '+'##')
    print(' '*41,'#'*8, '  ##', ' '*6+'#'*4, ' '*4+'##     ##', ' '+' '*4+'##'+' '*4, ' '+'#'*6)
    print('\n')
    

def update(filename):
    ganti()
    show(filename)
    index = int(input('\nPilih nomor yang akan diubah : '))
    index-=1
    ganti()
    preview(index, filename)
    isi = load(filename)
    print('\n\nUbah Data \n')
    keterangan = input('Keterangan       : ')
    jumlah = input('Jumlah Transaksi : ')
    total = int(input('Jumlah Uang      : Rp '))
    i=0
    while True:
        ganti()
        preview(index, filename)
        print('\n\nUbah Data \n')
        print(f'Keterangan       : {keterangan}')
        print(f'Jumlah Transaksi : {jumlah}')
        print(f'Jumlah Uang      : Rp {total}')
        print('''Jenis Transaksi  :
        1. Debet ( Pengeluaran )
        2. Kredit ( Penerimaan )\n\n ''')
        if i>=1:
            print('Maaf, masukkan anda tidak valid\n')
        pilihan_transaksi = input('Pilih Transaksi : ')
        if pilihan_transaksi=='1':
            isi[index]['Keterangan'] = keterangan
            isi[index]['Jumlah'] = jumlah
            isi[index]['Debet'] = total
            isi[index]['Kredit'] = '-'
            break
        elif pilihan_transaksi=='2':
            isi[index]['Keterangan'] = keterangan
            isi[index]['Jumlah'] = jumlah
            isi[index]['Debet'] = '-'
            isi[index]['Kredit'] = total
            break
        i += 1
        print(isi)
    try :
        with open(filename, 'w') as file:
            json.dump(isi, file, indent=4)
    except IOError as e:
        print(e)


def hapus():
    os.system('cls')
    print(' '*44,'##'*2,' '*5+'##'*3,' '+'##',' '*5+'##'*3,' '+'##'*5, ' '+'##'*3)
    print(' '*44,'##   #',' '*3+'##',' '*5+'##',' '*5+'##',' '*9+'##', ' '*5+'##')
    print(' '*44,'##     #',' '+'##'*3,' '+'##',' '*5+'##'*3,' '*5+'##',' '*5+'##'*3)
    print(' '*44,'##   #',' '*3+'##',' '*5+'##',' '*5+'##',' '*9+'##', ' '*5+'##')
    print(' '*44,'##'*2,' '*5+'##'*3,' '+'##'*3,' '+'##'*3,' '*5+'##',' '*5+'##'*3)
    print('\n')

def delet(filename):
    hapus()
    show(filename)
    isi = load(filename)
    index = int(input('\nPilih nomor yang akan di hapus : '))
    index-=1
    hapus()
    preview(index, filename)
    verifikasi = input('\napakah anda yakin menghapus data tersebut ? [y]/[n] ')
    if verifikasi=='y':
        isi.pop(index)
    try:
        with open(filename, 'w') as file:
            json.dump(isi, file, indent=4)

    except IOError as e:
        print(e)


def akhir():
    os.system('cls')
    print('\n\n\n\n\n\n\n\n\n\n\n\n')
    print(' '*35,'##'*5,' ##'+'  '*3+'##',' '+' '*4+'#'+' '*4,' '+'##'+' '*5+'##',' '+'##    #',' '+'##'*4)
    print(' '*35,' '*4+'##'+' '*5,'##'+'  '*3+'##',' '+' ##   ## ',' '+'## #   ##',' '+'##  #',' '*3+'##')
    print(' '*35,' '*4+'##'+' '*5,'##'*5,' '+'##'+' '*5+'##',' '+'##   # ##',' '+'###',' '*5+'##'*4)
    print(' '*35,' '*4+'##'+' '*5,'##'+'  '*3+'##',' '+'## ### ##',' '+'##'+' '*5+'##',' '+'##  #',' '*3+'  '*3+'##')
    print(' '*35,' '*4+'##'+' '*5,'##'+'  '*3+'##',' '+'##'+' '*5+'##',' '+'##'+' '*5+'##',' '+'##    #',' '+'##'*4)
    print('\n\n\n\n\n\n\n\n\n\n\n')    

filename = 'saldo.json'
menu = '''

Menu Transaksi : 

1. Tambah Data
2. Ganti Data
3. Hapus Data
4. Log Out
'''

load(filename)
#awal()
#login()
while True:
    os.system('cls')
    print(' '*53,'##',' '*6+'##','  '+'##'*3,' '+'##'*5)
    print(' '*53,'##',' '*6+'##','  '+'##',' '*9+'##')
    print(' '*53,'##',' '*6+'##','  '+'##'*3,' '*5+'##')
    print(' '*53,'##',' '*6+'##',' '*6+'##',' '*5+'##')
    print(' '*53,'##'*3,'  ##','  '+'##'*3,' '*5+'##\n')
    show(filename)
    print(menu)
    komen = input('\n\n\nPilih Menu : ')
    if komen=='1':
        insert(filename)
    elif komen=='2':
        update(filename)
    elif komen=='3':
        delet(filename)
    elif komen=='4':
        akhir()
        break