# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

Oleh karena itu dibuatlah sebuah Sistem Prediksi Monitoring Performa Mahasiswa Jaya Jaya Institut yang dibuat untuk mengestimasi performa mahasiwa jaya jaya institutnstitut jaya jaya dan memonitoring potensi dropout pada mahasiswa jaya jaya institut.

### Permasalahan Bisnis

Tingginya angka dropout mahasiswa di Jaya Jaya Institut menjadi ancaman serius terhadap reputasi institusi dan efisiensi operasional. Institusi perlu sistem yang proaktif untuk mengidentifikasi mahasiswa berisiko dropout sejak dini, agar intervensi dan bimbingan khusus dapat diberikan untuk meningkatkan tingkat kelulusan dan menjaga kualitas lulusan.

### Cakupan Proyek

- Membersihkan dataset yang digunakan untuk di analisa.
- Mengidentifikasi feature yang memiliki pengaruh besar terhadap potensi dropout pada mahasiswa.
- Membangun model prediksi untuk Sistem Prediksi Monitoring Performa Mahasiswa Jaya Jaya Institut.
- Membuat dashboard visualisasi untuk memonitor potensi dropout maupun menjabarkan latarbelakang penyebab dropout.
- Memberikan sebuah pandangan berupa rekomendasi yang baik dilakukan oleh manajemen Jaya jaya Institut.

### Persiapan

Sumber data: Dataset yang digunakan dalam proyek kali ini adalah bersumber dari sebuah platform.

UC Irvine Machine Learning Repository: https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success

Dicoding Dataset: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

Setup environment:

Proyek ini menggunakan Pipenv untuk mengelola lingkungan virtual dan dependensi proyek secara terisolasi.
Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah berikut untuk menyiapkan virtual environment nya:

1. Clone Repository

Kloning repositori ke local, buka terminal atau command prompt/powershell lalu jalankan

```
git clone
cd
```

2. Instal Pipenv

Jika anda belum memiliki Pipenv yang terinstal dalam sebuah sistem, aka instal dulu dengan cara

```
pip install pipenv
```

3. Pipenv Environment Initialization and Dependencies Installation:

dari dalam direktori proyek ini, kita dapat menginisialisasi lingkungan Pipenv dan secara bersamaan menginstall depedensi kebutuhan proyek ini dari file requirement.txt

```
pipenv install -r requirements.txt
```

3. Activate/Enable Virtual Environment

Setelah semua dependensi terinstal, aktifkan lingkungan virtual yang dibuat oleh Pipenv

```
pipenv shell
```

4. Run the App

Jika ingin menjalankan sebuah sistem prediksi berbasis website maka anda dapat menjalankan command berikut:

```
streamlit run app.py
```

## Business Dashboard

Business Dashboard
n

🔗 Link Dashboard:

## Menjalankan Sistem Machine Learning

Sistem Prediksi Monitoring Performa Mahasiswa dibuat sebagai solusi langsung untuk masalah ini, dengan tujuan utama mendukung pengambilan keputusan dalam memberikan bimbingan dan intervensi yang tepat waktu.

Model yang digunakan adalah XGBoost Classifier, dipilih karena performa akurasi yang tinggi setelah dibandingkan dengan model lain seperti Logistic Regression dan Support Vector Machine Classifier. Model ini sudah disimpan dalam format .joblib agar dapat di-load kembali saat digunakan di aplikasi. Selain model prediktif yang disimpan, ada juga menyimpan model dalam bentuk dictionary yang digunakan untuk preprocessing data yang akan di input oleh user.

Untuk menjalankan prototipe sistem:

1. Buka halaman Prediksi Streamlit.
2. Terdapat sebuah informasi feature/variabel data mahasiswa yang akan digunakan untuk prediksi. Untuk melakukan prediksi ada pada sidebar halaman streamlit.
3. Masukkan data mahasiswa yang digunakan berdasarkan data mahasiswa.
4. Klik prediksi untuk melihat hasilnya:
5. Apakah mahasiswa berpotensi Dropout atau non-Dropout
6. Probabilitasnya dalam bentuk persentase

🔗 Link Prototipe:

## Conclusion

Proporsi mahasiswa yakni 80 % merupakan berstatus single dan sebagian besar berjenis kelamin perempuan.

75% mahasiswa merupakan kuliah dengan biaya sendiri atau dengan kata lain tidak menyandang beasiswa karena tidak menerima scholarship_holder.

Orang tua mahasiswa baik ibu maupun bapak paling banyak bekerja sebagai Profesional/Manajerial dan Unskilled Labour akan tetapi berbanding terbalik dengan tingkat pendidikan orang tua. Sebagian besar orang tua merupakan `Low Educated` dan `Medium Educated`.

Kebayakan mahasiswa yang mengalami/mengindikasikan akan di dropout berstatus single sebanyak 1184 dari 4424 mahasiswa maju jaya institut.

Ada beberapa jurusan yang terindikasi dengan jumlah dropout terbesar yakni jurusan Management ada sekiar >250 mahasiwa management yang berpotensi/terancam dropout baik Jurusan Manajemen di kelas siang maupun sore hari. Adapun yang kedua merupakan jurusan Social Services

Sebagian besar mahasiswa berasal dari highschool level.
Jurusan yang terbanyak diminati yakni Nursing Management dan sosial service

### Rekomendasi Action Items
