# Program: Remote Air Conditioner Universal
# Spesifikasi: Program ini memungkinkan remote AC melakukan sinkronisasi dengan berbagai tipe atau merk AC lainnya dengan cara mengirimkan
# satu per-satu kode IR dari daftar kode ke AC, lalu melakukan pengecekkan apakah kode IR tersebut sesuai dengan target tipe AC.

import time

# Daftar kode IR bawaan untuk berbagai merek AC (simulasi)
ir_codes = {
    "001": "Tipe A",
    "002": "Tipe B",
    "003": "Tipe C",
    "004": "Tipe D",
    "005": "Tipe E",
    "006": "Tipe F",
    "007": "Tipe G",
    "008": "Tipe H",
    "009": "Tipe I",
    "010": "Tipe J",
}

# Fungsi untuk mensimulasikan pengiriman kode IR
def send_ir_code(code):
    print(f"Mengirim kode IR: {code}")
    return code

# Fungsi untuk mensimulasikan penerimaan dan respons AC
def receive_ir_code(code, target_code):
    if code == target_code:
        print(f"AC merespons: Kode '{code}' cocok! Sinkronisasi berhasil.")
        return True
    else:
        print(f"Kode '{code}' tidak cocok. Mencoba kode berikutnya...")
        return False

# Fungsi untuk sinkronisasi otomatis
def auto_sync(ac_target_code):
    print("Memulai proses sinkronisasi remote AC universal...\n")
    for code in ir_codes:
        # Kirim kode IR
        sent_code = send_ir_code(code)
        # Simulasikan penerimaan dan respons AC
        if receive_ir_code(sent_code, ac_target_code):
            print(f"Remote berhasil disinkronkan dengan {sent_code}.\n")
            return code
        time.sleep(1)  # Tunggu sebelum mencoba kode berikutnya
    
    print("Sinkronisasi gagal. Kode tidak ditemukan.")
    return None

# Main program
# Misalnya, AC memiliki kode "006"
ac_target_code = "006"
synced_code = auto_sync(ac_target_code)

if synced_code:
    print(f"Sinkronisasi selesai. Remote siap digunakan dengan kode: {synced_code}.")


# Program: Remote Air Conditioner GUI
# Spesifikasi: Program ini membuat antarmuka pengguna untuk remote AC dengan berbagai tombol dan layar untuk mengontrol
#              fitur-fitur selayaknya remote AC sungguhan seperti suhu, mode, kecepatan kipas, timer, sleep, dll.

import tkinter as tk
from tkinter import *
from datetime import datetime

# ------------------------------------ KAMUS ------------------------------------
# lebar : int          -- Lebar jendela utama
# tinggi : int         -- Tinggi jendela utama
# lebarlayar : int     -- Lebar layar monitor
# tinggilayar : int    -- Tinggi layar monitor
# x : int              -- Posisi horizontal jendela utama
# y : int              -- Posisi vertikal jendela utama
# formatted_time : str -- Waktu saat ini dalam format yang rapi

# Fungsi untuk menyimpan suhu ke file
def simpan_suhu(suhu):
    with open("suhu_terakhir.txt", "w") as file:
        file.write(str(suhu))

# Fungsi untuk membaca suhu dari file
def baca_suhu():
    try:
        with open("suhu_terakhir.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 24  # Suhu default jika file tidak ditemukan

# Inisialisasi suhu awal dengan membaca dari file
suhu = baca_suhu()

# ---------------------------------- ALGORITMA ----------------------------------
# 1. Inisialisasi jendela utama.
# 2. Tambahkan layar untuk menampilkan informasi suhu, mode, waktu, dan simbol-simbol AC.
# 3. Tambahkan tombol-tombol untuk mengontrol fitur seperti ON/OFF, mode, kecepatan, dan timer.
# 4. Tampilkan jendela utama antarmuka pengguna.

import tkinter as tk  # Mengimpor modul tkinter untuk GUI
from tkinter import Label, Button  # Mengimpor widget Label dan Button dari tkinter
from datetime import datetime  # Mengimpor modul datetime untuk menampilkan waktu saat ini
time = __import__('time')  # Mengimpor modul time untuk simulasi waktu

# Konfigurasi jendela utama
lebar = 300  # Lebar jendela
tinggi = 650  # Tinggi jendela

window = tk.Tk()  # Membuat instance dari jendela tkinter
lebarlayar = window.winfo_screenwidth()  # Mendapatkan lebar layar
tinggilayar = window.winfo_screenheight()  # Mendapatkan tinggi layar

# Menghitung posisi jendela agar berada di tengah layar
x = int((lebarlayar / 2) - (lebar / 2))
y = int((tinggilayar / 2) - (tinggi / 2) - 30)

# Mengatur ukuran dan posisi jendela
window.geometry(f"{lebar}x{tinggi}+{x}+{y}")
window.resizable(0, 0)  # Mencegah pengguna mengubah ukuran jendela
window.title("Remote Air Conditioner")  # Menentukan judul jendela

# ---------- VARIABEL GLOBAL ----------
mode = "Auto"  # Mode default AC
kecepatan = 1  # Kecepatan kipas default
timer = 0  # Timer default
kompressor = 0  # Kecepatan kerja kompresor (skala 1-10)
fanindoor = 0  # Kecepatan kerja fan indoor (skala 1-10)
fanoutdoor = 0  # Kecepatan kerja fan outdoor (skala 1-10)
nyalatimer = True  # Status nyala timer
nyala = True  # Status nyala AC
heat = False  # Status mode pemanasan
cold = False  # Status mode pendinginan
swing = False  # Status ayunan kipas
sleep = False  # Status mode tidur
nyalajam = True  # Status tampilan jam

# ---------- SIMULASI THERMISTOR & SENSOR KELEMBABAN ----------
suhuruang = float(input("Masukkan suhu ruang saat ini:"))  # Input suhu ruangan
humiditas = float(input("Masukkan % kelembaban relatif (Skala: 1-100):"))  # Input kelembapan relatif
selisih = suhuruang - 24  # Selisih suhu ruangan dengan suhu default (24°C)

if suhuruang > 30:  # Jika suhu ruangan lebih dari 30°C
    heat = True  # Mode pemanasan aktif
if humiditas > 60:  # Jika kelembapan lebih dari 60%
    cold = True  # Mode pendinginan aktif

# ---------- LAYAR REMOTE AC ----------
# Membuat layar dengan garis tepi
layar = tk.Frame(window, bg="white", width=260, height=240, highlightbackground="black", highlightthickness=2)
layar.place(x=20, y=10)  # Menempatkan layar di posisi tertentu

# Layer dalam layar
layer1 = tk.Frame(window, bg="white", width=195, height=240, highlightbackground="black", highlightthickness=2)
layer1.place(x=85, y=10)  # Layer bagian dalam pertama

layer2 = tk.Frame(window, bg="white", width=195, height=192, highlightbackground="black", highlightthickness=2)
layer2.place(x=85, y=10)  # Layer bagian dalam kedua

# ---------- LABEL PADA LAYAR ----------
# Label untuk suhu
labelsuhu = Label(layer2, text="24°C", font=("Arial", 40), background="white")  # Menampilkan suhu default
labelsuhu.place(x=47.5-10, y=48, width=115+20, height=96)  # Menempatkan label suhu

# Label untuk mode
labelmode = Label(layer2, text=f"Mode : {mode}", font=("Arial", 22), background="white")  # Menampilkan mode default
labelmode.place(x=0, y=139, width=190, height=48)  # Menempatkan label mode

# Menampilkan waktu real-time
current_time = datetime.now()  # Mendapatkan waktu saat ini
formatted_time = current_time.strftime("%Y-%m-%d | %H:%M:%S")  # Format waktu menjadi string

labeljam = Label(layer1, text=f"{formatted_time}", font=("Arial", 13), background="white")  # Menampilkan waktu
labeljam.place(x=0, y=190, width=190, height=45.5)  # Menempatkan label waktu

# Label untuk timer
labeltimer = Label(layer2, text=f"Timer : {timer}:00", font=("Arial", 15), background="white")  # Menampilkan timer default
labeltimer.place(x=5+2.5, y=0, width=150, height=48)  # Menempatkan label timer

# Simbol tambahan di layar
simbolswing = Label(layar, text="", bg="white", font=("Helvetica", 18))  # Simbol ayunan kipas
simbolswing.place(x=17, y=0, width=60, height=60)  # Menempatkan simbol ayunan kipas

simbolhumidity = Label(layar, text="", bg="white", font=("Helvetica", 18))  # Simbol kelembapan
simbolhumidity.place(x=1.25, y=60, width=60, height=60)  # Menempatkan simbol kelembapan

simbolheat = Label(layar, text="", bg="white", font=("Helvetica", 18))  # Simbol pemanasan
simbolheat.place(x=1.25, y=120, width=60, height=60)  # Menempatkan simbol pemanasan

simbolspeed = Label(layar, text="🌀", bg="white", font=("Helvetica", 11))  # Simbol kecepatan kipas
simbolspeed.place(x=1.25, y=180, width=60, height=55)  # Menempatkan simbol kecepatan kipas

simbolsleep = Label(layer2, text="", bg="white", font=("Helvetica", 18))  # Simbol mode tidur
simbolsleep.place(x=155+2.5, y=0, width=30, height=42)  # Menempatkan simbol mode tidur

# Def on/off
def onoff():
    """
    Fungsi untuk menghidupkan/mematikan layar AC
    """
    global nyala
    nyala = not nyala  # Mengubah status nyala
    if nyala == False:  # Jika AC mati
        # Menyembunyikan semua elemen di layar
        labelsuhu.place_forget()
        labelmode.place_forget()
        labeltimer.place_forget()
        simbolswing.place_forget()
        simbolhumidity.place_forget()
        simbolheat.place_forget()
        simbolspeed.place_forget()
        simbolsleep.place_forget()
        labeljam.place_forget()
    else:  # Jika AC hidup
        # Menampilkan kembali elemen-elemen di layar
        labelsuhu.place(x=47.5-10, y=48, width=115+20, height=96)
        labelmode.place(x=0, y=139, width=190, height=48)
        labeltimer.place(x=5+2.5, y=0, width=150, height=48)
        simbolswing.place(x=17, y=0, width=60, height=60)
        simbolhumidity.place(x=1.25, y=60, width=60, height=60)
        simbolheat.place(x=1.25, y=120, width=60, height=60)
        simbolspeed.place(x=1.25, y=180, width=60, height=55)
        simbolsleep.place(x=155+2.5, y=0, width=30, height=42)
        labeljam.place(x=0, y=190, width=190, height=45.5)

# ---------- UPDATE DISPLAY ----------
# Jika mode "heat" menyala, tampilkan simbol matahari di layar.
if heat == True:
    simbolheat.config(text="☀")

# Jika mode "cold" menyala, tampilkan simbol air di layar.
if cold == True:
    simbolhumidity.config(text="💧")

# Fungsi untuk memperbarui tampilan layar sesuai dengan kondisi terkini.
def updatelayar():
    global mode, suhu, timer, kecepatan
    
    # Memperbarui label mode dengan mode saat ini.
    labelmode.config(text=f"Mode : {mode}")
    
    # Memperbarui label suhu dengan suhu saat ini.
    labelsuhu.config(text=f"{suhu}°C")
    
    # Memperbarui label timer dengan nilai timer saat ini.
    labeltimer.config(text=f"Timer : {timer}:00")
    
    # Menampilkan simbol kecepatan kipas sesuai dengan tingkat kecepatan.
    simbolspeed.config(text="🌀" * kecepatan)
    
    # Menampilkan simbol tidur jika mode sleep menyala.
    if sleep == True:
        simbolsleep.config(text="💤")
    else:
        simbolsleep.config(text="")
    
    # Menampilkan simbol swing jika mode swing menyala.
    if swing == True:
        simbolswing.config(text="💨↕️")
    else:
        simbolswing.config(text="")
    
    # Menyembunyikan label timer jika mode nyala timer mati.
    if nyalatimer == False:
        labeltimer.config(text="")
    
    # Menyembunyikan atau menampilkan label jam sesuai kondisi nyala jam.
    if nyalajam == False:
        labeljam.place_forget()
    else:
        labeljam.place(x=0, y=190, width=190, height=45.5)

# Fungsi untuk mengubah suhu dengan delta tertentu.
def ubahsuhu(delta):
    global suhu
    # Perubahan suhu hanya dilakukan jika perangkat menyala dan suhu dalam rentang 16-30°C.
    if nyala == True and 16 <= suhu + delta <= 30:
        suhu += delta
        simpan_suhu(suhu)  # Menyimpan suhu baru ke file.
        updatelayar()  # Memperbarui tampilan layar.
        selisih = suhuruang - suhu  # Menghitung selisih antara suhu ruang dan suhu yang diinginkan.
        print("Suhu diinginkan saat ini:", suhu)

# Fungsi untuk mengubah mode operasi ke mode berikutnya.
def ubahmode():
    global mode, kecepatan
    modes = ["Auto", "Cool", "Dry", "Fan", "Eco"]  # Daftar mode yang tersedia.
    # Mengubah mode ke mode berikutnya dalam daftar secara sirkular.
    mode = modes[(modes.index(mode) + 1) % len(modes)]
    updatelayar()  # Memperbarui tampilan layar.

    # Menjalankan fungsi terkait sesuai mode yang dipilih.
    if mode == "Auto":
        update_auto_mode(suhuruang, suhu)
    elif mode == "Cool":
        update_cool_mode(suhuruang, suhu)
    elif mode == "Dry":
        update_dry_mode(humiditas)
    elif mode == "Fan":
        update_fan_mode()
    elif mode == "Eco":
        update_eco_mode(suhuruang, suhu)
    else:
        print("Tidak ada perubahan mode.")

# Fungsi untuk mengubah kecepatan kipas.
def ubahkecepatan(kecepatanbaru=None):
    global kecepatan
    # Jika mode Turbo dipilih, setel kecepatan ke maksimum.
    if kecepatanbaru == "Turbo":
        kecepatan = 3
        print("Mode Turbo: Fan Indoor bekerja maksimal (Fan Indoor: 10/10)")
    # Jika mode Quiet dipilih, setel kecepatan ke minimum.
    elif kecepatanbaru == "Quiet":
        kecepatan = 0
        print("Mode Quiet: Fan Indoor bekerja minimal (Fan Indoor: 2/10)")
    # Jika tidak, siklus kecepatan antara 1 hingga 3.
    elif 0 <= kecepatan <= 3:
        if kecepatan == 3:
            kecepatan = 1
        else:
            kecepatan += 1
    updatelayar()

# Fungsi untuk mengaktifkan atau menonaktifkan mode sleep.
def ubahsleep():
    global sleep
    sleep = not sleep  # Toggle status sleep.
    updatelayar()

    # Jika mode sleep aktif, perbarui pengaturan mode sleep.
    if sleep == True:
        update_sleep_mode(suhu)

# Fungsi untuk mengaktifkan atau menonaktifkan mode swing.
def ubahswing():
    global swing
    swing = not swing  # Toggle status swing.
    updatelayar()

    # Menampilkan status swing di konsol.
    if swing == True:
        print('Status Swing: Menyala')
    else:
        print('Status Swing: Mati')

# Fungsi untuk mengatur status nyala timer.
def ubahnyalatimer(nyalagak):
    global nyalatimer
    if nyalagak == "ON":
        nyalatimer = True
    else:
        nyalatimer = False
    updatelayar()

# Fungsi untuk mengubah durasi timer.
def ubahtimer(waktu):
    global timer
    if timer >= 0:
        timer += waktu  # Menambahkan waktu ke timer.
    if timer == -1:
        timer = 0  # Timer tidak boleh negatif.
    updatelayar()

# Fungsi untuk mengaktifkan atau menonaktifkan tampilan jam.
def ubahnyalajam():
    global nyalajam
    nyalajam = not nyalajam  # Toggle status nyala jam.
    updatelayar()

# ---------- SIMULASI PADA KOMPONEN AC ----------
def update_auto_mode(suhuruang, suhu):
    """
    Fungsi untuk mengatur mode Auto pada AC berdasarkan suhu ruang dan suhu target.
    """
    global kompressor, fanindoor, fanoutdoor

    selisih = suhuruang - suhu

    if selisih > 3:
        # Ruangan jauh lebih panas dari suhu target
        kompressor = 10  # Kompressor bekerja maksimal
        fanindoor = 10   # Fan Indoor bekerja maksimal
        fanoutdoor = 10  # Fan Outdoor bekerja maksimal
    elif 1 < selisih <= 3:
        # Ruangan sedikit lebih panas dari suhu target
        kompressor = 7   # Kompressor bekerja menengah
        fanindoor = 7    # Fan Indoor bekerja menengah
        fanoutdoor = 7   # Fan Outdoor bekerja menengah
    elif -1 <= selisih <= 1:
        # Ruangan mendekati suhu target
        kompressor = 4   # Kompressor bekerja rendah
        fanindoor = 4    # Fan Indoor bekerja rendah
        fanoutdoor = 4   # Fan Outdoor bekerja rendah
    elif selisih < -1:
        # Ruangan lebih dingin dari suhu target
        kompressor = 0   # Kompressor mati
        fanindoor = 2    # Fan Indoor bekerja minimal untuk sirkulasi
        fanoutdoor = 0   # Fan Outdoor mati

    print(f"Mode Auto: Suhu ruang = {suhuruang}, Suhu target = {suhu}")
    print(f"Kompressor: {kompressor}/10, Fan Indoor: {fanindoor}/10, Fan Outdoor: {fanoutdoor}/10\n-----------------------")

def update_cool_mode(suhuruang, suhu):
    """
    Fungsi untuk mengatur mode Cool pada AC berdasarkan suhu ruang dan suhu target.
    """
    global kompressor, fanindoor, fanoutdoor

    if suhuruang > suhu:
        kompressor = 8  # Kompressor bekerja maksimal
        fanindoor = 7   # Fan Indoor bekerja maksimal
        fanoutdoor = 7  # Fan Outdoor bekerja maksimal
    else:
        kompressor = 0  # Kompressor mati
        fanindoor = 2   # Fan Indoor bekerja minimal untuk sirkulasi
        fanoutdoor = 0  # Fan Outdoor mati

    print(f"Mode Cool: Suhu ruang = {suhuruang}, Suhu target = {suhu}")
    print(f"Kompressor: {kompressor}/10, Fan Indoor: {fanindoor}/10, Fan Outdoor: {fanoutdoor}/10\n-----------------------")

def update_dry_mode(humiditas):
    """
    Fungsi untuk mengatur mode Dry pada AC berdasarkan tingkat humiditas.
    """
    global kompressor, fanindoor, fanoutdoor

    if humiditas > 70:
        kompressor = 8  # Kompressor bekerja tinggi
        fanindoor = 5   # Fan Indoor bekerja sedang
        fanoutdoor = 7  # Fan Outdoor bekerja tinggi
    elif 50 <= humiditas <= 70:
        kompressor = 6  # Kompressor bekerja sedang
        fanindoor = 4   # Fan Indoor bekerja rendah
        fanoutdoor = 5  # Fan Outdoor bekerja sedang
    else:
        kompressor = 4  # Kompressor bekerja rendah
        fanindoor = 3   # Fan Indoor bekerja rendah
        fanoutdoor = 3  # Fan Outdoor bekerja rendah

    print(f"Mode Dry: Humiditas = {humiditas}%")
    print(f"Kompressor: {kompressor}/10, Fan Indoor: {fanindoor}/10, Fan Outdoor: {fanoutdoor}/10\n-----------------------")

def update_fan_mode():
    """
    Fungsi untuk mengatur mode Fan pada AC.
    """
    global kompressor, fanindoor, fanoutdoor

    kompressor = 0  # Kompressor mati
    fanindoor = 5   # Fan Indoor bekerja sedang
    fanoutdoor = 0  # Fan Outdoor mati

    print("Mode Fan: Hanya kipas yang bekerja")
    print(f"Kompressor: {kompressor}/10, Fan Indoor: {fanindoor}/10, Fan Outdoor: {fanoutdoor}/10\n-----------------------")

def update_eco_mode(suhuruang, suhu):
    """
    Fungsi untuk mengatur mode Eco pada AC berdasarkan suhu ruang dan suhu target.
    """
    global kompressor, fanindoor, fanoutdoor

    selisih = suhuruang - suhu

    if selisih > 2:
        kompressor = 5  # Kompressor bekerja hemat
        fanindoor = 4   # Fan Indoor bekerja rendah
        fanoutdoor = 4  # Fan Outdoor bekerja rendah
    elif selisih <= 2:
        kompressor = 0  # Kompressor mati
        fanindoor = 2   # Fan Indoor bekerja minimal
        fanoutdoor = 0  # Fan Outdoor mati

    print(f"Mode Eco: Suhu ruang = {suhuruang}, Suhu target = {suhu}")
    print(f"Kompressor: {kompressor}/10, Fan Indoor: {fanindoor}/10, Fan Outdoor: {fanoutdoor}/10\n-----------------------")

def update_sleep_mode(suhu_awal):
    """
    Fungsi untuk mengatur mode Sleep pada AC.

    Saat mode Sleep:
    - Suhu target dinaikkan 1 derajat setiap jam hingga maksimal +2 derajat dari suhu awal.
    - Setelah suhu dinaikkan 2 derajat, suhu tetap hingga mode Sleep selesai.
    """
    global suhu

    suhu = suhu_awal
    maksimal_kenaikan = 2  # Maksimal kenaikan suhu (2 derajat)

    for jam in range(1, 8):
        if suhu < suhu_awal + maksimal_kenaikan:
            suhu += 1
            print(f"Jam ke-{jam}: Suhu dinaikkan menjadi {suhu}°C.")
        else:
            print(f"Jam ke-{jam}: Suhu tetap pada {suhu}°C.")
            break
        
        # Simulasi jeda satu jam, dalam simulasi ini 1 jam = 3 detik
        time.sleep(3) 

    print("Mode Sleep selesai. Suhu akhir:", suhu, "\n-----------------------")

    

# ---------- TOMBOL UTAMA BAGIAN TENGAH ----------
# Membuat tombol ON/OFF dengan teks "ON/OFF", warna latar "firebrick2", dan posisi serta ukuran spesifik
Button(text="ON/OFF", command=onoff, background="firebrick2", activebackground="firebrick2").place(x=120, y=270, width=60, height=60)
# Membuat tombol SWING yang menjalankan fungsi ubahswing saat ditekan
Button(text="SWING", command=lambda: ubahswing()).place(x=40, y=275, width=50, height=50)
# Membuat tombol SPEED yang menjalankan fungsi ubahkecepatan saat ditekan
Button(text="SPEED", command=lambda: ubahkecepatan()).place(x=210, y=275, width=50, height=50)
# Membuat tombol MODE yang menjalankan fungsi ubahmode saat ditekan
Button(text="MODE", command=lambda: ubahmode()).place(x=125, y=350, width=50, height=50)
# Membuat tombol TURBO yang mengubah kecepatan ke mode "Turbo" saat ditekan
Button(text="TURBO", command=lambda: ubahkecepatan("Turbo")).place(x=40, y=350, width=50, height=50)
# Membuat tombol QUIET yang mengubah kecepatan ke mode "Quiet" saat ditekan
Button(text="QUIET", command=lambda: ubahkecepatan("Quiet")).place(x=40, y=425, width=50, height=50)
# Membuat tombol SLEEP yang menjalankan fungsi ubahsleep saat ditekan
Button(text="SLEEP", command=lambda: ubahsleep()).place(x=125, y=425, width=50, height=50)
# Membuat tombol "+" untuk meningkatkan suhu, dengan ukuran spesifik
Button(text="+", command=lambda: ubahsuhu(1)).place(x=217.5, y=350, width=35, height=62.5)
# Membuat tombol "-" untuk menurunkan suhu, dengan ukuran spesifik
Button(text="-", command=lambda: ubahsuhu(-1)).place(x=217.5, y=412.5, width=35, height=62.5)

# ---------- TOMBOL TIMER BAGIAN BAWAH ----------
# Membuat frame untuk area tombol timer dengan ukuran spesifik
tk.Frame(window, width=245, height=115, highlightbackground="black", highlightthickness=0.5).place(x=27.5, y=500)

# Membuat label teks "CT ITB" dengan font tebal ukuran 14
Label(text="CT ITB", font=("Helvetica", 14, "bold")).place(x=110, y=615, width=90, height=45)
# Membuat label teks "T I M E R" dengan font ukuran 12
Label(text="T I M E R", font=("Arial", 12)).place(x=117.5, y=515, width=65, height=30)

# Membuat tombol ON untuk menyalakan timer
Button(text="ON", command=lambda: ubahnyalatimer("ON")).place(x=40, y=515, width=50, height=30)
# Membuat tombol "+" untuk meningkatkan durasi timer
Button(text="+", command=lambda: ubahtimer(1)).place(x=40, y=570, width=50, height=30)
# Membuat tombol OFF untuk mematikan timer
Button(text="OFF", command=lambda: ubahnyalatimer("OFF")).place(x=210, y=515, width=50, height=30)
# Membuat tombol "-" untuk mengurangi durasi timer
Button(text="-", command=lambda: ubahtimer(-1)).place(x=210, y=570, width=50, height=30)
# Membuat tombol CLOCK untuk menyalakan/mengatur jam
Button(text="CLOCK", command=lambda: ubahnyalajam()).place(x=125, y=570, width=50, height=30)

# ---------- MENAMPILKAN JENDELA ----------
# Memulai loop utama untuk menampilkan window GUI
window.mainloop()

