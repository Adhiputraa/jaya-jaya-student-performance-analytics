import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Memuat model, scaler, dan label encoder yang telah disimpan
try:
    scaler = joblib.load('model/scaler_v2.joblib')
    model = joblib.load('model/model_prediction.joblib')
    labels_encoded = joblib.load('model/label_encoder_v2.joblib')
except FileNotFoundError as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

st.set_page_config(
    page_title="Forecasting Student Dropout",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🎓 Sistem Prediksi Monitoring Performa Mahasiswa Jaya Jaya Institut")
st.markdown("""
            Aplikasi ini membantu memprediksi potensi mahasiswa untuk putus Kuliah (drop out).
            Sistem digunakan untuk mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.
            Sistem prediksi ini dibuat berdasarkan berbagai faktor demografi, akademik, dan ekonomi.
            Silakan masukkan data mahasiswa di **Sidebar** untuk mendapatkan hasil prediksi.
""")

# --- Halaman Utama untuk Informasi Variabel ---
st.header("📚 Informasi Variabel")
st.markdown("""
    Berikut adalah penjelasan singkat mengenai setiap variabel yang digunakan dalam model prediksi.
    Memahami variabel ini dapat membantu Anda memberikan input yang lebih akurat.
""")
st.markdown("---")
#############################################################################
st.subheader("Data Umum & Demografi")
st.markdown("""
    Variabel ini mengidentifikasi program studi atau jurusan yang diambil oleh mahasiswa.
    Setiap jurusan memiliki karakteristik dan tantangan yang berbeda.
    """)
with st.expander("**Jurusan (Course)**"):
    st.markdown("Berikut adalah daftar jurusan dan penjelasan singkatnya:")
    st.markdown("""
    - **Nursing (Keperawatan):** Program studi yang berfokus pada ilmu dan praktik keperawatan.
        - **Fokus Studi:** Anatomi, fisiologi, farmakologi, etika keperawatan.
        - **Prospek Karir:** Perawat di rumah sakit, klinik, atau layanan kesehatan masyarakat.
        - **Tantangan:** Beban akademik tinggi, jam praktik panjang.
    - **Management (Manajemen):** Program studi yang mempelajari pengelolaan organisasi dan bisnis.
        - **Fokus Studi:** Keuangan, pemasaran, sumber daya manusia, strategi bisnis.
        - **Prospek Karir:** Manajer, analis bisnis, konsultan.
    - **Social Service (Pelayanan Sosial):** Program studi yang bertujuan mempersiapkan profesional di bidang pekerjaan sosial.
        - **Fokus Studi:** Psikologi sosial, kebijakan sosial, intervensi komunitas.
        - **Prospek Karir:** Pekerja sosial, konselor.
    - **Informatics Engineering (Teknik Informatika):** Program studi yang berpusat pada pengembangan perangkat lunak dan sistem informasi.
        - **Fokus Studi:** Pemrograman, algoritma, basis data, jaringan komputer.
        - **Prospek Karir:** Pengembang perangkat lunak, data scientist, ahli jaringan.
    - **Agronomy (Agronomi):** Program studi ilmu pertanian dan pengelolaan tanaman.
        - **Fokus Studi:** Ilmu tanah, budidaya tanaman, hama dan penyakit tanaman.
        - **Prospek Karir:** Peneliti pertanian, konsultan pertanian.
    - **Tourism (Pariwisata):** Program studi yang fokus pada industri perjalanan dan keramah-tamahan.
        - **Fokus Studi:** Manajemen hotel, pemasaran destinasi, event management.
        - **Prospek Karir:** Manajer hotel, pemandu wisata, perencana acara.
    - **Basic Education (Pendidikan Dasar):** Program studi untuk menjadi guru di tingkat dasar.
        - **Fokus Studi:** Pedagogi, psikologi anak, kurikulum pendidikan dasar.
        - **Prospek Karir:** Guru SD.
    - **Veterinary Nursing (Asisten Dokter Hewan):** Studi tentang perawatan dan penanganan hewan di bawah supervisi dokter hewan.
    - **Journalism and Communication (Jurnalistik dan Komunikasi):** Studi tentang pengumpulan, penulisan, dan penyebaran berita dan informasi.
    - **Advertising and Marketing Management (Manajemen Periklanan dan Pemasaran):** Studi tentang strategi periklanan dan pemasaran produk atau jasa.
    - **Communication Design (Desain Komunikasi):** Desain visual untuk menyampaikan pesan secara efektif.
    - **Animation and Multimedia Design (Desain Animasi dan Multimedia):** Kreasi animasi dan konten multimedia.
    - **Equinculture (Ilmu Kuda):** Studi tentang pemeliharaan dan budaya terkait kuda.
    - **Oral Hygiene (Kebersihan Gigi):** Profesi yang fokus pada pencegahan penyakit mulut.
    - **Biofuel Production Technologies (Teknologi Produksi Biofuel):** Studi tentang produksi bahan bakar dari biomassa.
    """)

with st.expander("**Usia Saat Pendaftaran (Age_at_enrollment):**"):
    st.markdown("""
    Usia mahasiswa saat pertama kali mendaftar di universitas.
    """)

with st.expander("**Jenis Kelamin (Gender):**"):
    st.markdown("""
    Jenis kelamin mahasiswa: laki-laki / perempuan (male/female).
    """)

# Anda bisa menerapkan pola ini untuk variabel lain juga
with st.expander("**Pekerjaan Ayah (Fathers_occupation)**"):
    st.markdown("""
    Kategori pekerjaan ayah mahasiswa dapat memberikan indikasi latar belakang ekonomi dan sosial.
    """)
    st.markdown("""
    - **Professional/Managerial:** Pekerjaan yang membutuhkan pendidikan tinggi dan tanggung jawab besar. Berikut merupakan beberapa contoh pekerjaan profesional/ manajerial:
        - **Perwakilan Legislatif dan Eksekutif, Direktur, serta Manajer Eksekutif (DPR, CEO, Direktur Utama, General Manager)**
        - **Spesialis dalam Aktivitas Intelektual dan Ilmiah (ilmuwan)**
        - **Teknisi dan Profesional Tingkat Menengah (asisten profesional)**
        - **Staf Administrasi (resepsionis/Staff umum)**
        - **Direktur Layanan Administrasi dan Komersial**
        - **Direktur Hotel, Katering, Perdagangan, dan Layanan Lainnya**
        - **Pekerja Kantor, Sekretaris Umum, dan Operator Pemrosesan Data**
        - **Operator Data, Akuntansi, Statistik, Layanan Keuangan, dan Pendaftaran**
        - **Staf Pendukung Administrasi Lainnya**
        - **Spesialis Ilmu Fisika, Matematika, Teknik, dan Teknik Terkait**
        - **Profesional Kesehatan**
        - **Guru/Pengajar**
        - **Spesialis Keuangan, Akuntansi, Organisasi Administrasi, Hubungan Masyarakat dan Komersial**
        - **Spesialis Teknologi Informasi dan Komunikasi (TIK)**
        - **Teknisi dan Profesional Sains dan Teknik Tingkat Menengah**
        - **Teknisi dan Profesional Kesehatan Tingkat Menengah**
        - **Teknisi Tingkat Menengah dari Layanan Hukum, Sosial, Olahraga, Budaya, dan Sejenisnya**
        - **Teknisi Teknologi Informasi dan Komunikasi**
    - **Pekerja Kasar (Unskilled Labor):** Pekerjaan yang tidak memerlukan keahlian khusus atau pelatihan formal. Berikut merupakan beberapa contoh pekerjaan kasar:
        - **Pekerja Kasar Umum**
        - **Petugas Kebersihan**
        - **Pekerja Kasar di Pertambangan, Konstruksi, Manufaktur, dan Transportasi**
        - **Asisten Penyiap Makanan**
    - **Machine/Vehicle Operators:** Pengemudi atau operator mesin berat. Berikut merupakan beberapa contoh pekerjaan operator mesin/ kendaraan:
        - **Operator Mesin, Tukang Pasang, dan Perakit**
        - **Tukang listrik, tukang kayu, teknisi**
        - **Operator Mesin Tetap (Pabrik)**
        - **Pekerja Perakit**
        - **Sopir Kendaraan dan Operator Alat Berat**
    - **Service/Sales:** Pekerja di sektor jasa atau penjualan. Berikut merupakan beberapa contoh pekerjaan di bidang jasa/penjualan:
        - **Pekerja Jasa Pribadi, Keamanan, dan Penjual**
        - **Pekerja Jasa Pribadi (Tukang Pijat)**
        - **Penjual (SPG/SPB)**
        - **Pekerja Perawatan Pribadi dan Sejenisnya (Pengasuh Anak)**
        - **Petugas Keamanan dan Penjaga (Security)**
        - **Pedagang Kaki Lima (Bukan Makanan) dan Penyedia Jasa Jalanan**
    - **Military:** Merupakan bagian dari angkatan bersenjata. Berikut merupakan beberapa contoh pekerjaan di bidang militer:
        - **Profesi Angkatan Bersenjata**
        - **Perwira Angkatan Bersenjata**
        - **Sersan Angkatan Bersenjata**
        - **Personel Angkatan Bersenjata Lainnya**
    - **Agriculture:** Pekerja di bidang pertanian. Berikut merupakan beberapa contoh pekerjaan di bidang pertanian:
        - **Petani, Nelayan, dan Pekerja Hutan yang Ahli**
        - **Petani & Peternak Ahli (Fokus Jual Hasil)**
        - **Petani, Peternak, Nelayan, Pemburu, dan Pengumpul (Kebutuhan Sendiri)**
        - **Pekerja Kasar di Pertanian, Peternakan, Perikanan, dan Kehutanan (buruh tani musiman)**
    - **Student:** Masih berstatus pelajar/mahasiswa.
    - **Others:** Kategori pekerjaan lain yang tidak termasuk di atas.
    - **Skilled Labor:** Pekerjaan yang membutuhkan keahlian atau pelatihan khusus. Berikur merupakan beberapa contoh pekerjaan terampil:
        - **Pekerja Konstruksi Terampil (kecuali Ahli Listrik)**
        - **Pekerja Terampil di Metalurgi, Pengerjaan Logam, dan Sejenisnya**
        - **Pekerja Terampil Percetakan, Pembuat Instrumen Presisi, Perhiasan, Pengrajin, dan Sejenisnya**
        - **Pekerja Terampil di Bidang Listrik dan Elektronik**
        - **Pekerja di Industri Pengolahan Makanan, Kayu, Pakaian, dan Industri/Kerajinan Lainnya**
    """)

with st.expander("**Mahasiswa Domisili Luar Daerah (Displaced):**"):
    st.markdown("""
    Apakah mahasiswa tinggal jauh dari rumah asalnya untuk kuliah : Ya / Tidak (yes/no).
    """)
st.markdown("---")
#############################################################################
st.subheader("Data Keadaan Ekonomi Mahasiswa")
with st.expander("**Penerima Beasiwa (Scholarship_holder)**"):
    st.markdown("""
    Apakah mahasiswa menerima beasiswa: Ya / Tidak (yes/no).
    Beasiswa dapat membantu mahasiswa dalam biaya pendidikan dan mengurangi risiko drop out.
    """)

with st.expander("**Apakah biaya Kuliah siswa sudah sesuai dengan yang berlaku? (Tuition_fees_up_to_date)**"):
    st.markdown("""
    Apakah biaya kuliah mahasiswa sudah sesuai dengan yang berlaku: Ya / Tidak (yes/no).
    Biaya kuliah yang tidak sesuai dapat menjadi faktor stress finansial bagi mahasiswa.
    """)

with st.expander("**Tingkat Inflasi (Inflation_rate)**"):
    st.markdown("""
    Tingkat inflasi di negara/wilayah mahasiswa.
    Kondisi ekonomi makro dapat memengaruhi stabilitas finansial mahasiswa.
    """)

with st.expander("**Tingkat Pengangguran (Unemployment_rate)**"):
    st.markdown("""
    Tingkat pengangguran di negara/wilayah mahasiswa.
    Tingkat pengangguran yang tinggi dapat mempengaruhi peluang kerja mahasiswa setelah lulus.
    """)

with st.expander("**Keadaan Gross Domestick Product (GDP)**"):
    st.markdown("""
    Keadaan GDP (Gross Domestic Product) di negara/wilayah mahasiswa.
    GDP mencerminkan kesehatan ekonomi dan dapat mempengaruhi peluang kerja mahasiswa.
    """)

st.markdown("---")
#############################################################################

st.subheader("Data Akademik Mahasiswa")
with st.expander("**Nilai Kualifikasi Terakhir (Previous_qualification_grade)**"):
    st.markdown("""
    Nilai yang diperoleh mahasiswa pada kualifikasi terakhir sebelum masuk universitas (skala 80-200).
    Ini mencerminkan kemampuan akademik awal mahasiswa.
    """)

with st.expander("**Nilai Masuk (Admission_grade)**"):
    st.markdown("""
    Nilai yang diperoleh mahasiswa saat masuk universitas (skala 0-200).
    Ini mencerminkan kemampuan akademik awal mahasiswa.
    """)

with st.expander("**Mata Kuliah Diikuti Semester 1 (Curricular_units_1st_sem_enrolled)**"):
    st.markdown("""
    Jumlah mata kuliah yang diikuti mahasiswa pada semester pertama.
    Ini mencerminkan beban akademik yang dihadapi mahasiswa.
    """)

with st.expander("**Total Evaluasi Mata Kuliah Semester 1 (Curricular_units_1st_sem_evaluations)**"):
    st.markdown("""
    Jumlah evaluasi (ujian, tugas, dll.) yang dihadapi mahasiswa pada semester pertama.
    Ini mencerminkan tingkat keterlibatan akademik mahasiswa.
    """)

with st.expander("**Mata Kuliah Lulus Semester 1 (Curricular_units_1st_sem_approved)**"):
    st.markdown("""
    Jumlah mata kuliah yang berhasil diselesaikan mahasiswa pada semester pertama.
    Ini mencerminkan kemampuan mahasiswa dalam menyelesaikan beban akademik.
    """)

with st.expander("**Nilai Indeks Semester 1 (Curricular_units_1st_sem_grade)**"):
    st.markdown("""
    Nilai indeks yang diperoleh mahasiswa pada semester pertama.
    Ini mencerminkan performa akademik mahasiswa pada semester tersebut.
    """)

with st.expander("**Mata Kuliah Diikuti Semester 2 (Curricular_units_2nd_sem_enrolled)**"):
    st.markdown("""
    Jumlah mata kuliah yang diikuti mahasiswa pada semester kedua.
    Ini mencerminkan beban akademik yang dihadapi mahasiswa.
    """)

with st.expander("**Total Evaluasi Mata Kuliah Semester 2 (Curricular_units_2nd_sem_evaluations)**"):
    st.markdown("""
    Jumlah evaluasi (ujian, tugas, dll.) yang dihadapi mahasiswa pada semester pertama.
    Ini mencerminkan tingkat keterlibatan akademik mahasiswa.
    """)

with st.expander("**Mata Kuliah Lulus Semester 2 (Curricular_units_2nd_sem_approved)**"):
    st.markdown("""
    Jumlah mata kuliah yang berhasil diselesaikan mahasiswa pada semester kedua.
    Ini mencerminkan kemampuan mahasiswa dalam menyelesaikan beban akademik.
    """)

with st.expander("**Nilai Indeks Semester 2 (Curricular_units_2nd_sem_grade)**"):
    st.markdown("""
    Nilai indeks yang diperoleh mahasiswa pada semester kedua.
    Ini mencerminkan performa akademik mahasiswa pada semester tersebut.
    """)


st.markdown("---")
st.caption("Aplikasi ini dibuat untuk tujuan demonstrasi dan pendidikan. Hasil prediksi adalah estimasi dan tidak menggantikan penilaian profesional.")
st.caption(" © 2023 Jaya Jaya Institut. All rights reserved.")
st.caption("full code available at [GitHub](https://github.com/Adhiputraa/jaya-jaya-student-performance-analytics)")


def user_input_features():
    st.sidebar.header("Sistem Prediksi Monitoring Performa Mahasiswa Jaya Jaya Institut")
    st.sidebar.markdown("Masukkan data mahasiswa untuk memprediksi kemungkinan mereka drop out.")
##################################################################################
    st.sidebar.subheader("Data Umum & Demografi Mahasiswa")
    Course = st.sidebar.selectbox('Jurusan', ['Nursing','Management','Social Service',
                                    'Veterinary Nursing','Journalism and Communication',
                                    'Advertising and Marketing Management','Tourism','Communication Design',
                                    'Animation and Multimedia Design','Agronomy',
                                    'Basic Education','Informatics Engineering',
                                    'Equinculture','Oral Hygiene','Biofuel Production Technologies'])
    Age_at_enrollment = st.sidebar.number_input('Usia saat pendaftaran',
                                        min_value=0, max_value=70, value=18, step=1,
                                        help="Age at enrollment in years")
    Gender = st.sidebar.selectbox('Jenis Kelamin',['male', 'female'])
    Fathers_occupation = st.sidebar.selectbox('Pekerjaan Ayah', ['Professional/Managerial','Unskilled Labor',
                                                            'Machine/Vehicle Operators',
                                                            'Service/Sales','Military','Agriculture','Student','Others',
                                                            'Skilled Labor'])
    Displaced = st.sidebar.selectbox('Mahasiswa Domisili Luar Daerah', ['yes', 'no'])
########################################################################################
    st.sidebar.subheader("Data Keadaan Ekonomi Mahasiswa")
    Scholarship_holder = st.sidebar.selectbox('Apakah mahasiswa menerima beasiswa', ['yes', 'no'])
    Tuition_fees_up_to_date = st.sidebar.selectbox('Apakah biaya Kuliah siswa sudah sesuai dengan yang berlaku', ['yes', 'no'])
    Inflation_rate = st.sidebar.slider('Tingkat inflasi %', min_value=-5.0, max_value=5.0, value=0.0,
                                    help="Inflation rate in percentage")
    Unemployment_rate = st.sidebar.slider('Tingkat pengangguran %',
                                        min_value=0.0, max_value=100.0, value=10.0,
                                        step=0.1, help="Unemployment rate in percentage")
    GDP = st.sidebar.slider('Keadaan GDP (Gross Domestic Product)', min_value=-5.0, max_value=10.0,
                        value=1.0, step=0.01, help="GDP in percentage")
#########################################################################################
    st.sidebar.subheader("Data Akademik Mahasiswa")
    Previous_qualification_grade = st.sidebar.number_input('Nilai Kualifikasi Terakhir', min_value=80,
                                                max_value=200, value=130, step=13,)
    Admission_grade = st.sidebar.number_input('Nilai Ujian Masuk', min_value=80,
                                    max_value=200, value=120, step=1)
    Curricular_units_1st_sem_enrolled = st.sidebar.number_input('Mata Kuliah Diikuti Semester 1',
                                                        min_value=0,
                                                        max_value=32, value=6,
                                                        help="Number of curricular units enrolled in the first Semester")
    Curricular_units_1st_sem_evaluations = st.sidebar.number_input('Total Evaluasi Mata Kuliah Semester 1', min_value=0,
                                                            max_value=50,
                                                            value=8,
                                                            help="Number of evaluations in the first Semester")
    Curricular_units_1st_sem_approved = st.sidebar.number_input('Mata Kuliah Lulus Semester 1', min_value=0,
                                                        max_value=40, value=10,
                                                        help="Number of curricular units approved in the first Semester")
    Curricular_units_1st_sem_grade = st.sidebar.number_input('Nilai Indeks Semester 1',
                                                    min_value=0,
                                                    max_value=24,
                                                    value=10,help="Curricular units 1st sem grade")
    Curricular_units_2nd_sem_enrolled = st.sidebar.number_input('Mata Kuliah Diikuti Semester 2', min_value=0,
                                                        max_value=32, value=6,
                                                        help="Number of curricular units enrolled in the second Semester")
    Curricular_units_2nd_sem_evaluations = st.sidebar.number_input('Total Evaluasi Mata Kuliah Semester 2',  min_value=0,
                                                            max_value=50,
                                                            value=8,
                                                            help="Number of evaluations in the second Semester")
    Curricular_units_2nd_sem_approved = st.sidebar.number_input('Mata Kuliah Lulus Semester 2',
                                                        min_value=0,
                                                        max_value=30, value=4,
                                                        help="Number of curricular units approved in the second Semester")
    Curricular_units_2nd_sem_grade = st.sidebar.number_input('Nilai Indeks Semester 2', min_value=0,
                                                    max_value=24,
                                                    value=10,
                                                    help="Curricular units 2nd sem grade")
    # Validasi input dari user
    # Validasi Course
    if Inflation_rate < -5 or Inflation_rate > 10:
        st.sidebar.error("Inflation_rate must be between 0.0 and 20.0")
        return None
    # Validasi umur pada saat pendaftaran
    if Age_at_enrollment < 0 or Age_at_enrollment > 70:
        st.sidebar.error("Age at enrollment must be between 0 and 70")
        return None
    # Validasi tingkat pengangguran
    if Unemployment_rate < 0 or Unemployment_rate > 100:
        st.sidebar.error("Unemployment_rate must be between 0 and 70")
        return None
    # Validasi Admission_grade
    if Admission_grade < 80 or Admission_grade > 200:
        st.sidebar.error("Admission grade must be between 0.0 and 20.0")
        return None
    # Validasi GDP
    if GDP < -5 or GDP > 10:
        st.sidebar.error("GDP must be between -5 and 10")
        return None
    # Validasi Previous_qualification_grade
    if Previous_qualification_grade < 80 or Previous_qualification_grade > 200:
        st.sidebar.error("Previous qualification grade must be between 80 and 200")
        return None
    # Validasi Curricular_units_1st_sem_approved
    if Curricular_units_1st_sem_approved < 0 or Curricular_units_1st_sem_approved > 30:
        st.sidebar.error("Curricular units 1st sem approved must be between 0 and 20")
        return None
    # Validasi Curricular_units_1st_sem_enrolled
    if Curricular_units_1st_sem_enrolled < 0 or Curricular_units_1st_sem_enrolled > 32:
        st.sidebar.error("Curricular units 1st sem enrolled must be between 0 and 40")
        return None
    # Validasi Curricular_units_1st_sem_evaluations
    if Curricular_units_1st_sem_evaluations < 0 or Curricular_units_1st_sem_evaluations > 50:
        st.sidebar.error("Curricular units 1st sem evaluations must be between 0 and 50")
        return None
    # Validasi Curricular_units_1st_sem_grade
    if Curricular_units_1st_sem_grade < 0 or Curricular_units_1st_sem_grade > 24:
        st.sidebar.error("Curricular units 1st sem grade must be between 0.0 and 24.0")
        return None
    # Validasi Curricular_units_2nd_sem_approved
    if Curricular_units_2nd_sem_approved < 0 or Curricular_units_2nd_sem_approved > 30:
        st.sidebar.error("Curricular units 2nd sem approved must be between 0 and 30")
        return None
    # Validasi Curricular_units_2nd_sem_enrolled
    if Curricular_units_2nd_sem_enrolled < 0 or Curricular_units_2nd_sem_enrolled > 32:
        st.sidebar.error("Curricular units 2nd sem enrolled must be between 0 and 32")
        return None
    # Validasi Curricular_units_2nd_sem_evaluations
    if Curricular_units_2nd_sem_evaluations < 0 or Curricular_units_2nd_sem_evaluations > 50:
        st.sidebar.error("Curricular units 2nd sem evaluations must be between 0 and 50")
        return None
    # Validasi Curricular_units_2nd_sem_grade
    if Curricular_units_2nd_sem_grade < 0 or Curricular_units_2nd_sem_grade > 24:
        st.sidebar.error("Curricular units 2nd sem grade must be between 0.0 and 24.0")
        return None
        # Membuat dictionary untuk menyimpan input dari user
    data = {
        'Course': Course,
        'Fathers_occupation': Fathers_occupation,
        'Gender': Gender,
        'Scholarship_holder': Scholarship_holder,
        'Tuition_fees_up_to_date': Tuition_fees_up_to_date,
        'Displaced': Displaced,
        'Inflation_rate': Inflation_rate,
        'Age_at_enrollment': Age_at_enrollment,
        'Unemployment_rate': Unemployment_rate,
        'Admission_grade': Admission_grade,
        'GDP': GDP,
        'Previous_qualification_grade': Previous_qualification_grade,
        'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
        'Curricular_units_1st_sem_evaluations': Curricular_units_1st_sem_evaluations,
        'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
        'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
        'Curricular_units_2nd_sem_evaluations': Curricular_units_2nd_sem_evaluations,
        'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade
    }
    features = pd.DataFrame(data, index=[0])
    return features

    # Function melakukan preprocessing menggunakan model yang telah dibuat sebelumnya
def preprocess_input(input_df):
    expected_model_features = [
    'Tuition_fees_up_to_date', 'Course', 'Displaced', 'Gender', 'Scholarship_holder',
    'Fathers_occupation', 'Curricular_units_2nd_sem_approved', 'Age_at_enrollment',
    'Curricular_units_1st_sem_approved', 'Curricular_units_2nd_sem_grade', 'Admission_grade',
    'Curricular_units_2nd_sem_evaluations', 'Unemployment_rate', 'Previous_qualification_grade',
    'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_grade',
    'Curricular_units_2nd_sem_enrolled', 'GDP', 'Curricular_units_1st_sem_evaluations',
    'Inflation_rate']

    # Reorder dataframe
    input_df = input_df[expected_model_features]
    input_num = input_df.select_dtypes(include=['int64', 'float64'])
    input_cat = input_df.select_dtypes(include=['object'])

    input_num_scaled = pd.DataFrame(scaler.transform(input_num), columns=input_num.columns)

    input_cat_encoded = input_cat.copy()
    for col in input_cat.columns:
        le = labels_encoded[col]
        try:
            input_cat_encoded[col] = le.transform(input_cat[col])
        except:
            st.error(f"Value di kolom {col} tidak dikenal: {input_cat[col].values}")
            return None

    preprocessed = pd.concat([input_num_scaled, input_cat_encoded], axis=1)

    return preprocessed[expected_model_features]

# memuat data yang di input oleh user dan menjadkan sebuah dataframe
with st.sidebar:
    input_df = user_input_features()
    if st.button("Predict"):
        preprocessed = preprocess_input(input_df)
        if preprocessed is not None:
            pred_proba = model.predict_proba(preprocessed)[0][1]
            pred_class = model.predict(preprocessed)[0]

            st.markdown("---")
            st.success(f"**Probabilitas Dropout:** {pred_proba * 100:.2f}%")

            if pred_class == 1:
                st.warning("🔴 **Mahasiswa ini berpotensi untuk DROP OUT**")
            else:
                st.info("🟢 **Mahasiswa ini diprediksi TIDAK akan Drop Out**")
        else:
            st.error("Input tidak valid, silakan periksa data Anda.")