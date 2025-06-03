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

Membuat folder jaya_institut dan Kloning repositori ke local, buka terminal atau command prompt/powershell lalu jalankan

```
mkdir jaya_institut
cd jaya_institut
git clone https://github.com/Adhiputraa/jaya-jaya-student-performance-analytics
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

Berdasarkan data performa Jaya Jaya Institut yang telah kita analisis. Proses analisis dimulai dari analisis awal di lingkuangan Python/Jupyter Notebook yang untuk membersihkan data, melabeling data, seta memahami pola dasar, yang kemudian kami visualisasikan secara dinamis melalui dashboard Tableau ini bewrdasarkan identifikasi hasil faktor faktor penentu keberhasilan dan dropout mahasiswa Jaya Jaya Institut. Dashboard ini dirancang untuk memberikan gambaran komprehensif dan insight mendalam mengenai perjalanan akademik mahasiswa kita, khususnya terkait dengan isu dropout.

Adapun pada dashboard merangkum jawaban dari permasalahan yang menjadi concern manajemen Jaya Jaya Institut, permasalahan yang dijawab pada dashboard seperti:

- Bagaimana perbedaan proses pembelajaran akademik mahasiswa yang terindikasi/telah di dropout?
- Jurusan apa saja yang paling banyak mahasiswa nya dan juga potensi dropout nya?
- Berapa rata rata umur mahasiswa saat mendaftar pada Jaya Jaya Institut?

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

🔗 Link Prototipe: https://jaya-jaya-student-performance-analytics.streamlit.app/

## Conclusion

Kita lihat bahwa bagiamana kekuatan data dapat meberikan wawasan dan pencerahan kepada kita semua terkhusus manajemen Jaya Jaya Institut. Dari dashboard dan analisis awal yang kita lakukan di file jupyter notebook ini kita dapat menarik beberapa kesimpulan bahwa nilai akademik yang dijalani dan dievaluasi oleh mahasiswa sangat berengaruh terhadap keberhasilan mahasiswa. Keberhasilan yang dimaksud adalah menempuh semua mata pelajaran yang jalani berdasarkan `course` (jurusan). Mahasiswa yang berhasil ini seperti dia mengambil 6 mata pelajaran dan berhasil lulus dalam 6 mata pelajaran tersebut. Sebaliknya mahasiswa yang gagal dalam mata pelajaran yang diambil, dari 6 mata pelajaran hanya 3 yang lulus maka cenderung akan terindikasi dropout. Selain masalah akademik, ada juga permasalahan lain yakni pada Jaya Jaya Institut juga terdapat 3 jurusan favorit yakni Nursing, Management, dan Social Service dimana dari ketiga nya jurusan management yang paling banyak menampilkan dropout nya.

Mahasiwa yang mendaftar menjadi mahasiswa Jaya Jaya Institut rata-rata pada umur dibawah 28 tahun. Terdapat wawasan menarik juga mengenai umur saat pendaftaran yakni semakin tua umur saat pendaftaran semakin tinggi juga potensi mahasiswa tersebut terkena dropout. Adapaun hal lain seperti nilai `Admission Grade` (nilai penerimaan) memiliki korelasi positif dengan `Previous Qualification Grade` (nilai dari pendidikan sebelum masuk ke Jaya Jaya Institut). Selain itu, terlihat bahwa mahasiswa yang berstatus Dropout cenderung memiliki nilai Previous qualification grade dan Admission grade yang lebih rendah dibandingkan dengan mahasiswa yang berstatus Non Dropout. Ini menunjukkan bahwa nilai kualifikasi dan penerimaan awal dapat menjadi indikator awal risiko dropout.

Sedangkan dalam faktor ekonomi dan sosial dari mahasiswa, seperti faktor `GDP`, `Inflation Rate` (tingkat inflasi), dan `Unemployment Rate` (tingkat pengangguran) tidak terlihat pola korelasi yang jelas dan kuat antara fluktuasi GDP, tingkat inflasi, atau tingkat pengangguran dengan status mahasiswa (dropout atau non-dropout). Mahasiswa dari kedua kelompok status (dropout dan non-dropout) tersebar di berbagai rentang indikator ekonomi makro yang ditampilkan.

### Rekomendasi Action Items

Berdasarkan hasil paparan kesimpulan komprehensif diatas, ada beberapa area strategis atau area yang concern yang perlu menjadi perhatian oleh pihak manajemen Jaya Jaya Institut. Berikut adalah rekomndasi tindakan yang bisa diambil/diajukan kepada manajemen Jaya Jaya Institut:

1.  Masalah yang terjadi pada akademik:

    Nilai akademik, terutama keberhasilan dalam menempuh mata kuliah di awal studi, sangat berpengaruh pada keberhasilan mahasiswa dan indikasi dropout. Mahasiswa yang tidak lulus banyak mata kuliah cenderung terindikasi dropout.
    Oleh karena itu kita merekomendasikan beberapa hal yang perlu dilakukan oleh manajemen Jaya Jaya Institut yakni:

    - Implementasikan Sistem Peringatan Dini Akademik, Sistem Otomatisasi ini notifikasi bagi dosen dan penasihat akademik ketika seorang mahasiswa menunjukkan penurunan performa di awal semester atau gagal dalam beberapa mata kuliah kunci.

    - Program Bimbingan Belajar/Remedial Intensif, Sediakan sesi bimbingan belajar atau kursus remedial yang terstruktur untuk mata kuliah yang memiliki tingkat kegagalan tinggi, khususnya bagi mahasiswa yang teridentifikasi berisiko.

    - Perkuat Peran Dosen Pembimbing Akademik, Berikan pelatihan tambahan kepada dosen pembimbing akademik untuk mengidentifikasi tanda-tanda awal kesulitan akademik dan dropout, serta cara memberikan dukungan yang relevan.

2.  Masalah yang terjadi pada program studi:

    Jurusan Management menunjukkan angka dropout tertinggi di antara jurusan favorit (Nursing, Management, Social Service).
    Oleh karena itu kita merekomendasikan beberapa hal yang perlu dilakukan oleh manajemen Jaya Jaya Institut yakni:

    - Melakukan Audit Kurikulum dan Metode Pengajaran, apakah kurikulum tersebut masih relevan dengan kemajuan teknologi saat ini dan juga apakah ada permasalahan oleh dosen penagajar.

    - Membuat Program Mentoring dan Pemngembangan Karir, manajemen bisa membuat program ini yang dilaksanakan ketika awal ajaran baru dan semester menengah menjalang ujian. Dimana yang menjadi mentor adalah siswa yang berprestasi baik secara akademik dan juga non-akademik sebagai mentor yang merangkul mahasiswa agar bisa melihat langsung apakah mahasiswa baru bisa mengikuti kegiatan pelajaran baik atau tidak. Adapaun program pengembangan karir ini berpotensi untuk menyemangati mahasiswa yang sedang kesulitan belajar, karir ini sangat baik untuk membangkitkan moral dan semangat mahasiswa kedepan nya. Bisa juga dilakukan seminar rutin oleh alumni jurusan yang berpotensi memiliki banyak mahasiswa yang akan dropout.

3.  Masalah pada nilai dan kriteria seleksi masuk:

    Mahasiswa dengan `Previous Qualification Grade` dan `Admission Grade` yang lebih rendah cenderung dropout. Kedua nilai ini memiliki korelasi positif. Oleh karena itu kita perlu mengoptimalisasi kriteria penerimaan mahasiswa dan melakukan sistem identifikasi dini berbasis data yang meliputi variabel yang mempengaruhi keberlansungan pembelajaran pada mahasiswa. Adapun cara nya dengan :

    - Melakukan evaluasi ulang apakah nilai Admission Grade dan Previous Qualification Grade saat ini sudah optimal dalam memprediksi keberhasilan. Pertimbangkan untuk memberikan bobot lebih pada komponen nilai tertentu yang terbukti sangat prediktif.

    - Membuat sistem informasi untuk mengidentifikasi dini mahasiswa yang beresiko akan dropout. Apabila tetap menerima mahasiswa yang akan berpotensi dropout maka maanjemen perlu membuat list nama atau menandai mahasiswa yang akan berpotensi dropout tersebut.

4.  Masalah pada profil usia saat pendaftaran:

    Ketika semakin tua amhasiswa yang akan mendaftar maka akan semakin sulit juga mengikuti pembelajaran sehingga berpotensi untuk dropout sangat tinggi, oleh karena itu diperlukan beberapa program yang dapat meringankan mahasiswa yang cenderung tua, yakni:

    - Membuat program khusus mahasiswa yang lebih tua untuk adaptasi mengingat mereka mungkin memiliki beberapa faktor yang membuat mereka tidak fokus. Seperti tanggung jawab keluarga dan pekerjaan berbeda dengan mahasiswa yang lebih muda.

    - Merencanakan fleksibilitas studi, hal ini sangat mungkin bisa menurunkan potensi dropout terhadap mahasiswa yang lebih tua, karena mereka bisa melakukan pembelajaran secara online misalknya dan juga menyesuaikan jadwal mereka.
