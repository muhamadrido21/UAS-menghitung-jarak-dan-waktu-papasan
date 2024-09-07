jarak_Ali = 0
kecepatan_Ali = 2
jarak_Badu = 0
kecepatan_Badu = 3
waktu = 0

while jarak_Ali + jarak_Badu < 1000:
    jarak_Ali += kecepatan_Ali
    kecepatan_Ali += 0.1
    jarak_Ali += kecepatan_Badu
    waktu += 1

    if waktu < 10:
        jarak_Badu = 0
    else:
        jarak_Badu = (waktu - 10) * kecepatan_Badu

print(f"Ali dan Badu berpapasan pada detik ke-{waktu} setelah pukul 8")
print(f"Jarak Badu dengan titik B setelah detik Ali dan Badu berpapasan yaitu {1000 - jarak_Badu} meter")