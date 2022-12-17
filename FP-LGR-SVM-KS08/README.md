# Final Project 2 - Logistic Regression dan SVM


## Kelompok E08, PREFIX IP: 192.196

| **No** | **Nama** | **NRP** |
| - | - | - |
| 1. | Muhammad Ismail | PYTN-KS08-011 |
| 2. | Syahrani Nabila Pardede | PYTN-KS08-013 |
| 3. | Shendy Krisyohanda | PYTN-KS08-021 |


## Latar Belakang  

Dalam proyek ini, kami akan mencoba menjawab pertanyaan apakah besok akan turun hujan di Australia. Kami menerapkan Logistic Regression dan SVM dengan Python dan Scikit-Learn.  

Untuk menjawab pertanyaan tersebut, kami membuat classifier untuk memprediksi apakah besok akan turun hujan di Australia. Kami melatih model klasifikasi biner menggunakan Logistic Regression dan SVM. Kami telah menggunakan dataset <a href="https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package">Rain in Australia</a> untuk proyek ini.  

Jadi, mari kita mulai.  

## Objektif

Final Project 2 ini dibuat guna mengevaluasi konsep Logistic Regression dan SVM
sebagai berikut:
- Mampu memahami konsep Classification dengan Logistic Regression dan SVM
- Mampu mempersiapkan data untuk digunakan dalam model Logistic Regression
dan SVM
- Mampu mengimplementasikan Logistic Regression dan SVM untuk membuat
prediksi

## Ulasan Proyek

Database ini memiliki 23 atribut. Dengan data hujan harian selama 10 tahun di Australia, kolom RainTomorrow adalah target variable yang mau kita prediksi. Jika “Yes” maka besok harinya disana hujan 1mm atau lebih.

## Informasi Atribut

1. `Date` - **tanggal hari itu**
2. `Location` - **lokasi, nama kota di Australia**
3. `MinTemp` - **temperatur terendah hari itu dalam celcius**
4. `MaxTemp` - **temperatur tertinggi hari itu dalam celcius**
5. `Rainfall` - **jumlah curah hujan hari itu dalam mm**
6. `Evaporation` - **jumlah evaporasi dalam mm dari Class A pan selama 24 jam sebelum jam 9 pagi hari itu**
7. `Sunshine` - **jumlah jam hari itu cerah dengan cahaya matahari**
8. `WindGustDir` - **arah kecepatan angin yang paling tinggi selama 24 jam sebelum jam 12 malam hari itu**
9. `WindGustSpeed` - **kecepatan angin yang paling tinggi dalam km/jam selama 24 jam sebelum jam 12 malam hari itu**
10. `WindDir9am` - **arah angin jam 9 pagi**
11. `WindDir3pm` - **arah angin jam 3 sore**
12. `WindSpeed9am` - **kecepatan angin jam 9 pagi dalam km/jam dihitung dari rata-rata kecepatan angin 10 menit sebelum jam 3 sore**
13. `WindSpeed3pm` - **kecepatan angin jam 3 sore dalam km/jam dihitung dari rata-rata kecepatan angin 10 menit sebelum jam 3 sore**
14. `Humidity9am` - **humiditas jam 9 pagi dalam persen**
15. `Humidity3pm` - **humiditas jam 3 sore dalam persen**
16. `Pressure9am` - **tekanan udara jam 9 pagi dalam hpa**
17. `Pressure3pm` - **tekanan udara jam 3 sore dalam hpa**
18. `Cloud9am` - **persentase langit yang tertutup awan jam 9 pagi. dihitung dalam oktas, unit ⅛, menghitung berapa unit ⅛ dari langit yang tertutup awan. Jika 0, langit cerah, jika 8, langit sepenuhnya tertutup awan.**
19. `Cloud3pm` - **persentase langit yang tertutup awan jam 3 sore**
20. `Temp9am` - **temperatur jam 9 pagi dalam celcius**
21. `Temp3pm` - **temperatur jam 3 sore dalam celcius**
22. `RainToday` - **apakah hari ini hujan: jika curah hujan 24 jam sebelum jam 9 pagi melebihi 1mm, maka nilai ini adalah 1, jika tidak nilai nya 0**
23. `RainTomorrow` - **variable yang mau di prediksi**