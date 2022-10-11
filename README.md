[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8172496&assignment_repo_type=AssignmentRepo)
# Milestones 1

_Milestones ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada Phase 0._

---

# Assignment Problems

Kamu adalah seorang Data Analyst yang akan mengerjakan projek besar untuk menyelesaikan suatu permasalahan client dan client kamu butuh sekali hasil analisa datamu menggunakan statistik dan dashboard visualisasi data untuk membantu mereka menyelesaikan masalah. **Pilihlah satu** dari empat masalah berikut yang dapat kamu bantu selesaikan:

1. Tim sukses seorang politisi di California ingin mengadakan kampanye menggunakan Google Ads. Namun, mereka tidak tahu apakah kampanye ini akan berhasil atau tidak dan butuh budget seberapa besar per bulannya. Bantu mereka untuk mengetahui apakah kampanye di Google Ads ini efektif atau tidak. Gunakan dataset `google_political_ads` di Google Cloud Platform BigQuery.

2. Departemen Pengawasan Lalu Lintas Kementerian Perhubungan Amerika Serikat ingin mengetahui kondisi kasus kecelakaan yang terjadi di jalan selama tahun 2016 yang berguna untuk diterapkan kebijakan baru supaya dapat mengurangi angka kecelakaan di kemudian hari. Gunakan dataset `nhtsa_traffic_fatalities` di Google Cloud Platform BigQuery.

3. Kementerian Lingkungan Hidup Amerika Serikat ingin membuat regulasi mengenai emisi industri dan kendaraan bermotor yang kini sangat merusak kualitas udara di negara tersebut. Namun untuk membuat regulasi tersebut, harus diketahui kondisi kualitas udara saat ini di berbagai negara bagian agar mudah menentukan negara bagian mana saja yang harus diterapkan regulasi tersebut terlebih dahulu. Gunakan dataset `epa_historical_air_quality` di Google Cloud Platform BigQuery.

4. CEO toko online "The Look" mencurigai bahwa ada yang tidak beres dari sistem penjualan di tokonya, dari performa penjualan produk, pengiriman barang, dsb. Mohon bantu ungkapkan apakah bermasalah atau tidak dari sistem penjualan di platformnya. Gunakan dataset `thelook_ecommerce` di Google Cloud Platform BigQuery.

---

# Assignment Instructions
## General Instructions
1. Pilihlah salah satu masalah yang ingin kamu selesaikan.

2. Gunakan dataset yang diinstruksikan dari Google Cloud Platform BigQuery. `Tabel yang dipakai dibebaskan tergantung dari analisis yang dilakukan`.

3. Sebelum menentukan tabel, kolom, atau hal lain dalam dataset mana yang akan dijadikan analisis dan visualisasi data, lakukan identifikasi dan penjabaran masalah supaya dapat memudahkan kamu dalam melakukan analisis. Kamu bisa menggunakan metode apapun seperti analisis SWOT, Fish bone diagram, 5W+1H, dsb.
  - **Contoh:**
  - Permasalahan: `Mengetahui Preferensi dan Perilaku Konsumsi Makanan di Area Urban di Indonesia`

  - Penjabaran masalah dengan metode 5W+1H:

    - Kota mana dengan rata-rata % pengeluaran makan paling besar?
    - Bagaimana perilaku pemilihan makanan berdasarkan harga terhadap social class masyarakat?
    - Apakah tingkat pendidikan sarjana memiliki preferensi memilih makanan-makanan yang sehat?
    - Apakah warga DKI Jakarta masih mengonsumsi makanan tradisional?
    - Usia berapa saja yang masih mengonsumsi makanan tradisional?
    - dsb.
  - Pertanyaan-pertanyaan/penjabaran masalah di atas dapat dijawab dengan data visualisasi dan analisis statistik.

4. Setelah melakukan identifikasi dan penjabaran masalah, tentukan metrik/data apa saja yang diperlukan lalu tarik data yang diperlukan dari dataset yang sudah ditentukan menggunakan SQL. `Cantumkan semua query yang dibuat untuk menarik semua data yang diperlukan dalam milestone ini`.
5. **Perlu diperhatikan** bahwa penjabaran masalah untuk dijawab menggunakan data visualisasi dan analisis statistik **HARUS** mengikuti kriteria berikut:
  - Minimal terdapat `6 penjabaran` masalah dimana 4 penjabaran untuk `visualisasi data`, 1 penjabaran untuk `statistik deskriptif`, dan 1 penjabaran untuk `statistik inferensial`.
6. Untuk `Data Visualisasi` dibebaskan menggunakan tipe visualisasi (batang, garis, dsb) dan library (matplotlib, pyplot, seaborn, dsb) apapun, disesuaikan dengan penjabaran masalahnya. `Minimal 4 visualisasi sesuai dengan jumlah minimum penjabaran untuk bagian visualisasi data`. **WAJIB** memberikan insight di tiap visualisasi data.
7. Untuk `Statistik Deskriptif`, pilih minimal salah satu perhitungan/analisis statistik deskriptif seperti *central tendency*, *measure of variance*, *outlier analysis*, *distribution*, dsb. `Sesuaikan dengan penjabaran masalah yang ditentukan`.
8. Untuk `Statistik Inferensial`, pilih minimal salah satu perhitungan/analisis statistik inferensial seperti *confidence interval*, *statistical significance*, *statistical testing*, *hypothesis testing: one sample, two sample independent, paired test, ANOVA, chi-square*, dsb. `Sesuaikan dengan penjabaran masalah yang ditentukan`.
9. Output dari milestone ini adalah dashboard data visualisasi menggunakan `streamlit` dan analisis serta pengolahan data di `jupyter notebook`.

## Notebook Instructions
1. Lakukan data cleaning dan preprocessing pada notebook
2. Notebook harus mengikuti format berikut:
  1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas.

  2. Identifikasi Masalah
      > Bab ini harus menyantumkan topik permasalahan serta penjabaran masalah yang ingin dianalisis menggunakan metode statistik dan data Visualisasi.

  3. Data Loading & Queries
      > Bagian ini berisi proses *data loading* dan eksplorasi data sederhana. Cantumkan query SQL masing-masing data yang di-load.

  4. Data Cleaning
      > Bagian ini berisi proses penyiapan data berupa data cleaning sebelum dilakukan *explorasi data* lebih lanjut. Proses cleaning dapat berupa memberi nama baru untuk setiap kolom, mengisi missing values, menghapus kolom yang tidak dipakai, dan lain sebagainya.

  5. Analisis dan perhitungan
      > Bagian ini berisi proses analisis, penjelasan, perhitungan statistik deskriptif, inferensial, serta pembuatan visualisasi data. Untuk visualisasi data wajib memberikan insight di tiap visualisasinya.

  6. Pengambilan Kesimpulan
      > Pada bab terakhir ini, **harus berisi** kesimpulan yang mencerminkan solusi/rekomendasi/jawaban atas permasalahan yang diangkat serta menarik benang merah dari seluruh analisis dan perhitungan secara singkat, jelas, dan padat.

3. Simpan notebook dengan judul h8dsft_Milestone1_<nama-student>.ipynb, misal h8dsft_Milestone1_raka_ardhi.ipynb

## Dashboard Instructions

1. Dashboard dibuat menggunakan library `streamlit`.
2. Dashboard yang dibuat terdiri dari minimal 2 layout : `Visualisasi` dan `Statistical Analysis`.
3. Untuk layout Visualisasi :
  - Minimal ada 4 figure/visualisasi data yang ditampilkan dalam halaman `Visualisasi` yang sesuai dengan yang dibuat pada Notebook.
  - Minimal ada 1 streamlit interactivity
  - Tidak perlu menulis insightnya, dashboard visualisasi sejatinya hanya kumpulan visualisasi data
4. Untuk layout Statistical Analysis:
  - Tulis proses analisis statistik deskriptif dan inferential yang dilakukan di notebook dari masalah yang diangkat hingga kesimpulan dari hasil analisis statistik.

5. Deploy dashboard yang telah dibuat ke heroku dengan format url berupa nama_student-batch-p0m1.herokuapp.com, misal raka-ardhi-ftds-001-p0m1.herokuapp.com.

6. Presentasikan dashboard yang telah dibuat pada P1W1D4PM.

---

# Assignment Submission

1. Tambahkan URL deployment Heroku di bagian paling atas `.ipynb` dan di README.
2. Tidak adanya URL Heroku di file .ipynb akan menyebabkan tidak dinilainya deployment Streamlit.
3. File yang berkaitan dengan Streamlit juga wajib dipush ke Github Classroom. Akan lebih bagus jika file deployment Streamlit masuk ke dalam folder yang berbeda dengan file `.ipynb`. Contoh hasil commit tugas yang baik :
   * `h8dsft_Milestone1_raka_ardhi.ipynb`
   * `/deployment`
     - `requirements.txt`
     - `Procfile`
     - `app.py`
     - etc

4. Ketidaklengkapan jawaban yang diupload, seperti hanya melampirkan file `ipynb` saja atau hanya melampirkan file deployment Streamlit saja, akan menyebabkan pengurangan nilai yang signifikan pada tugas kali ini.

5. Push Assigment yang telah dibuat ke akun Github masing-masing student dan Github Classroom.

---

## Assignment Rubrics

### Code Review

| Criteria|Meet Expectations|Points|
| --- | --- | --- |
| Streamlit Figure | Mampu membuat minimal 4 figure dengan Streamlit | 10 pts each (Max 40) |
| Streamlit Callback/Interactivity | Mampu membuat callback/interactivity dengan Streamlit | 20 pts |
| Statistical Descriptive Analysis | Mampu melakukan statistical descriptive analysis dan menampilkannya dengan Streamlit | 20 pts |
| Statistical Inferential Analysis | Mampu melakukan statistical inferential analysis dan menampilkannya dengan Streamlit | 20 pts |

### Readability (Notebook)

| Criteria | Meet Expectations | Points|
| --- | --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan menggunakan Markdown untuk penjelasan kode. | 10 pts |
| Insight | Menampilkan insight di tiap visualisasi. | 10 pts |
| Storytelling | Menuliskan data storytelling dengan alur analisis yang baik dari identifikasi permasalahan sampai kesimpulan. | 20 pts |

### Analysis

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan perhitungan dan analisa yang dilakukan. | 20 pts |

### Deployment

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Deploy Heroku | Deploy streamlit dashboard di Heroku. | 20 pts |

---

```
Total Points : 180

Catatan : Penilaian Milestone  juga dapat dipengaruhi oleh aktivitas student selama Phase 0 berlangsung, baik sesi kelas maupun sesi mentoring dengan buddy-nya masing-masing sehingga terdapat kemungkinan adanya penambahan atau pengurangan nilai diluar rubric yang telah disebutkan diatas.
```

## Score Reduction

Pengurangan poin akan diberlakukan jika Student terlambat mengumpulkan tugas yang telah diberikan. Adapun besarnya pengurangan adalah :

| Criteria | Max Points P0M1 |
| --- | --- |
| Keterlambatan kurang dari 1 jam setelah deadline | 135 pts (75 %) |
| Keterlambatan lebih dari 1 jam - 1 hari setelah deadline | 90 pts (50 %) |
| Keterlambatan lebih dari 1 hari setelah deadline | 0 pts (0 %) |
