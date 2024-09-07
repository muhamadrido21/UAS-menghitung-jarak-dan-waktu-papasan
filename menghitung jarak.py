jarak_Ali = 0
kecepatan_Ali = 2
waktu = 0

while jarak_Ali < 1000:
    jarak_Ali += kecepatan_Ali * 10
    kecepatan_Ali += 0.1
    waktu += 10

keberangkatan_Badu = 60
jarak_Badu = 0
kecepatan_Badu = 3

while jarak_Badu < jarak_Ali:
    jarak_Badu += kecepatan_Badu * 10
    waktu += 10

print(f"Badu menyusul Ali {keberangkatan_Badu + waktu // 3600}:{(keberangkatan_Badu + waktu // 60) % 60}:{keberangkatan_Badu + waktu % 60}")