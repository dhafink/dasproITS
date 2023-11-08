# Membaca input tanggal, bulan, dan tahun
tanggal, bulan, tahun = map(int, input().split())

# Daftar nama bulan
nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

# Daftar nama hari
nama_hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]

# Mencetak tanggal dalam format yang diinginkan
print(f"Tanggal : {tanggal} {nama_bulan[bulan - 1]} {tahun}")

# Menghitung hari dengan bantuan library datetime
from datetime import datetime
tanggal_input = datetime.strptime(f"{tahun}-{bulan:02d}-{tanggal:02d}", "%Y-%m-%d")
hari = tanggal_input.weekday()

# Mencetak hari
print(f"Hari : {nama_hari[hari + 1]}")