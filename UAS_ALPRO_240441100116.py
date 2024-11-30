#to-do list

tugas = {}
tugas_selesai = ["Belum selesai", "Selesai"]
def tambah_tugas():
    while True:
        print('===============================================')
        mata_kuliah = input('Masukkan mata kuliah: ')
        Jenis_Tugas = input("masukkan jenis tugas: ")
        Tanggal = input("Tanggal (dd/mm/yy): ")
        Deadline = input("Deadline (dd/mm/yy): ")
        waktu1 = input('Waktu akhir deadline: ')
        Tanggal_mengerjakan = input('Masukkan tanggal mengerjakan: ')
        waktu2 = input('Waktu akhir pengerjaan: ')

        for value in tugas.values():
            if value['TglKrj'] == Tanggal_mengerjakan and value['Waktu2'] == waktu2:
                print('Tanggal dan Waktu ini sudah ada, mohon ganti waktu lain ')
                return
            
        id_data = len(tugas) + 1
        tugas[id_data] = {
            'Matkul' : mata_kuliah,
            'Jenis' : Jenis_Tugas,
            'Tanggal' : Tanggal,
            'Deadline' : Deadline,
            'TglKrj': Tanggal_mengerjakan,
            'Waktu1' : waktu1,
            'Waktu2' : waktu2,
            'Status' : tugas_selesai[0]
        }
        print('Data berhasil ditambahkan')
        print()
        ulangi = input('apakah anda masih ingin menambahkan data tugas lagi? (iya/tidak)')
        if ulangi != "iya":
            break

def tampilkan_semua_tugas():
    print('===============================================')
    if len(tugas) <= 0:
        print('Tidak ada tugas.')
    else:
        for ID, value in tugas.items():
            print("*** Daftar Tugas ***")
            print(f"{ID}. Mata Kuliah: {value['Matkul']}")
            print(f"    Jenis Tugas: {value['Jenis']}")
            print(f"    Tanggal: {value['Tanggal']}")
            print(f"    Deadline: {value['Deadline']}")
            print(f"    Waktu Akhir Deadline: {value['Waktu1']}")
            print(f"    Tanggal mengerjakan {value['TglKrj']}")
            print(f"    Waktu Akhir Pengerjaan: {value['Waktu2']}")
            print(f"    Status: {value['Status']}")
            print()
    print('===============================================')

def tampilkan_urutan_deadline():
    print('===============================================')
    if len(tugas) <= 0:
        print('Tidak ada tugas')
    else:
        # Urutkan data berdasarkan deadline
        sorted_data = sorted(tugas.items(), key=lambda item: item[1]['Deadline'] + ' ' + item[1]['Waktu1'])
            
        for idx, (ID, value) in enumerate(sorted_data, 1):
            print(f"{idx}. Mata Kuliah: {value['Matkul']}")
            print(f"    Jenis Tugas: {value['Jenis']}")
            print(f"    Tanggal: {value['Tanggal']}")
            print(f"    Deadline: {value['Deadline']}")
            print(f"    Waktu Akhir Deadline: {value['Waktu1']}")
            print(f"    Waktu Akhir Pengerjaan: {value['Waktu2']}")
            print(f"    Status: {value['Status']}")
            print()
    print('===============================================')
    
def tampilkan_status_tugas(status):
    print('===============================================')
    if len(tugas) <= 0:
        print('Tidak ada tugas')
    else:
        found = False
        for ID, value in tugas.items():
            if value['Status'] == status:
                print(f"*** Tugas dengan status {status} ***")
                print(f"{ID}. Mata Kuliah: {value['Matkul']}")
                print(f"    Jenis Tugas: {value['Jenis']}")
                print(f"    Tanggal: {value['Tanggal']}")
                print(f"    Deadline: {value['Deadline']}")
                print(f"    Waktu Akhir Deadline: {value['Waktu1']}")
                print(f"    Waktu Akhir Pengerjaan: {value['Waktu2']}")
                print(f"    Status: {value['Status']}")
                print()
                found = True
        if not found:
            print(f'Tidak ada tugas yang ditandai {status}')
    print('===============================================')

def tampilkan_tugas():
    print('===============================================')
    while True:
        print('Menu Tampilkan: ')
        print('1. Tampilkan semua tugas')
        print('2. Tampilkan tugas yang belum selesai')
        print('3. Tampilkan tugas yang sudah selesai')
        print('4. Tampilkan tugas sesuai urutan deadline terdekat')
        print('5. Kembali')
        print()
        print('===============================================')

        opsi =int(input('pilih opsi: '))
        if opsi == 1:
            tampilkan_semua_tugas()
        elif opsi == 2:
            tampilkan_status_tugas('Belum selesai')
        elif opsi == 3:
            tampilkan_status_tugas('Selesai')
        elif opsi == 4:
            tampilkan_urutan_deadline()
        elif opsi == 5: 
            break
        else:
            print('Opsi tidak valid')
            
def tandai_tugas_selesai():
    print('===============================================')
    if len(tugas) <= 0:
        print("Tidak ada tugas")
    else:
        tampilkan_semua_tugas()
        ID = int(input('Tugas ke berapa yang akan kamu tandai sebagai selesai? '))
        if ID in tugas:
            if tugas[ID]['Status'] == tugas_selesai[1]:
                print('Tugas ini sudah ditandai')
            else:    
                tugas[ID]['Status'] = tugas_selesai[1]
                print('Tugas berhasil ditandai')
                print()
        else:
            print('Tugas tidak ditemukan')
            print()
    
def ubah_tugas():
    print('===============================================')
    while True:
        if len(tugas) <= 0:
            print('Tidak ada tugas')
        else:
            tampilkan_semua_tugas()
            ID = int(input('tugas ke berapa yang mau diupdate: '))
            if ID in tugas:
                print('Data tugas yang akan di update')
                print(f"{ID}. Mata Kuliah: {tugas[ID]['Matkul']}")
                print(f"   Jenis Tugas: {tugas[ID]['Jenis']}")
                print(f"   Tanggal: {tugas[ID]['Tanggal']}")
                print(f"   Deadline: {tugas[ID]['Deadline']}")
                print(f"   Waktu Akhir deadline: {tugas[ID]['Waktu1']}")
                print(f"   Tanggal Mengerjakan: {tugas[ID]['TglKrj']}")
                print(f"   Waktu Akhir Pengerjaan: {tugas[ID]['Waktu2']}")
                print(f"   Status: {tugas[ID]['Status']}")
                print('===============================================')
                print()
                
                print('===============================================')
                print('1. Jenis Tugas')
                print('2. tanggal Tugas')
                print('3. deadline Tugas')
                print('4. Waktu mengerjakan Tugas')
                print('5. Keluar')
                opsi = int(input('Pilih data tugas yang ingin di update: '))
                print('Masukkan data tugas baru')
                if opsi == 1:
                    Jenis_baru = input('Masukkan jenis tugas baru : ')
                    tugas[ID]['Jenis'] = Jenis_baru
                elif opsi == 2:
                    Tanggal_baru = input('Masukkan tanggal baru : ')
                    tugas[ID]['Tanggal'] = Tanggal_baru
                elif opsi == 3:
                    deadline_baru= input('Masukkan deadline baru : ')
                    waktu1_baru = input('Masukkan waktu akhir deadline: ')
                    tugas[ID]['Deadline'] = deadline_baru
                    tugas[ID]['Waktu1'] = waktu1_baru
                elif opsi == 4:
                    waktu2_baru = input('Masukkan waktu akhir pengerjaan: ')
                    Tanggal_mengerjakan_baru = input('masukkan tanggal mengerjakan baru: ')
                    for value in tugas.values():
                        if value['TglKrj'] == Tanggal_mengerjakan_baru and value['Waktu2'] == waktu2_baru:
                            print('Tanggal dan Waktu ini sudah ada, mohon ganti waktu lain ')
                            return
                    
                    tugas[ID]['Waktu2'] = waktu2_baru
                    print('Data berhasil diperbarui ')
                elif opsi ==  5:
                    break        
                else:
                    print('Opsi tidak valid')
            else:
                print('Tugas tidak ditemukan')
                print()

            ulangi = input('Apakah anda masih ingin mengubah data tugas lagi? (iya/tidak)')
            if ulangi != "iya":
                break
    print('===============================================')
        

    
def hapus_tugas():
    print('===============================================')
    if len(tugas) <= 0:
        print("Tidak ada tugas")
    else:
        while True:
            tampilkan_semua_tugas()
            ID = int(input('Data tugas ke berapa yang ingin dihapus: '))
            if ID in tugas:
                print('Data Tugas yang akan dihapus')
                print(f"{ID}. Mata Kuliah: {tugas[ID]['Matkul']}")
                print(f"    Jenis Tugas: {tugas[ID]['Jenis']}")
                print(f"    Tanggal: {tugas[ID]['Tanggal']}")
                print(f"    Deadline: {tugas[ID]['Deadline']}")
                print(f"    Waktu Akhir deadline: {tugas[ID]['Waktu1']}")
                print(f"    Waktu Akhir Pengerjaan: {tugas[ID]['Waktu2']}")
                print(f"    Status: {tugas[ID]['Status']}")

                del tugas[ID]
                print(f'Data Tugas berhasil dihapus')
            else:
                print('Tugas tidak ditemukan')
            ulangi = input('Apakah anda masih ingin menghapus data tugas lagi? (iya/tidak)')
            if ulangi != "iya":
                break

def menu():  
    while True:
        print('===============================================')
        print('1. Tambah Tugas')
        print('2. Tampilkan Tugas')
        print('3. Ubah Tugas')
        print('4. Hapus Tugas')
        print('5. Tandai Tugas Selesai')
        print('6. Keluar')
        print('===============================================')
        menu = int(input('pilih opsi: '))
        
        if menu == 1:
            tambah_tugas()
        elif menu == 2:
            tampilkan_tugas()
        elif menu == 3:
            ubah_tugas()
        elif menu == 4:
            hapus_tugas()
        elif menu == 5:
            tandai_tugas_selesai()
        elif menu == 6:
            print('kembali ke menu')
            break
        else:
            print('Opsi tidak valid')
menu()