# Laporan Proyek Machine Learning
### Nama : Iqsai Indra Nugraha
### Nim : 191351041
### Kelas : If pagi B

## Domain Proyek

Dataset ini berfokus pada industri keuangan, khususnya data terkait dengan penggunaan kartu kredit.

## Business Understanding

Dalam konteks ini, kita ingin memahami perilaku pengguna kartu kredit dan tren penggunaan mereka. Data ini dapat memberikan wawasan tentang bagaimana pengguna menggunakan kartu kredit, pola pengeluaran, dan potensi risiko yang terkait. 

### Problem Statements

1.Bagaimana pola penggunaan kartu kredit pada dataset ini?
2.Apakah ada tren atau kecenderungan tertentu dalam pengeluaran pengguna kartu kredit?
3.Apakah ada faktor-faktor risiko yang dapat diidentifikasi dari data ini?

 ### Goals
 
1.Menganalisis pola penggunaan kartu kredit untuk mendapatkan pemahaman yang lebih baik tentang perilaku pengguna.
2.Mengidentifikasi tren pengeluaran yang dapat membantu perusahaan dalam perencanaan strategis.
3.Menemukan faktor-faktor risiko potensial yang mungkin memerlukan tindakan pencegahan.

  ### Solution statements
  - Menerapkan analisis deskriptif untuk menggambarkan distribusi variabel-variabel kunci pada dataset.
  - Menggunakan metode time series untuk mengidentifikasi tren pengeluaran dari waktu ke waktu.
  - Melakukan analisis korelasi dan klaster untuk mengidentifikasi hubungan antar variabel dan mengelompokkan pengguna berdasarkan perilaku penggunaan kartu kredit.

  ## Data Understanding
  Dataset ini berisi informasi tentang pengguna kartu kredit, termasuk berbagai atribut seperti limit kredit, saldo, pembelian, pembayaran minimum, dan sebagainya. Dengan memahami struktur dan isi dataset, kita dapat merancang analisis yang sesuai untuk mencapai tujuan proyek.

  https://www.kaggle.com/code/halflingwizard/interpret-k-means-clusters-on-credit-card-dataset

  ### Variabel-variabel pada Europe bike store sales adalah sebagai berikut:
  1. CUST_ID (ID Pelanggan) = object
  2. BALANCE (Saldo) = float
  3. BALANCE_FREQUENCY (Frekuensi Saldo) = float
  4. PURCHASES (Pembelian) = float
  5. ONEOFF_PURCHASES (Pembelian Tunggal Tertinggi) = float
  6. INSTALLMENTS_PURCHASES (Pembelian Angsuran) = float
  7. CASH_ADVANCE (Penarikan Tunai) = float
  8. PURCHASES_FREQUENCY (Frekuensi Pembelian) = float
  9. ONEOFF_PURCHASES_FREQUENCY (Frekuensi Pembelian Tunggal) = float
  10. PURCHASES_INSTALLMENTS_FREQUENCY (Frekuensi Pembelian Angsuran) = float
  11. CASH_ADVANCE_FREQUENCY (Frekuensi Penarikan Tunai) = float
  12. CASH_ADVANCE_TRX (Jumlah Transaksi Penarikan Tunai) = float
  13. PURCHASES_TRX (Jumlah Transaksi Pembelian) = float
  14. CREDIT_LIMIT (Batas Kredit) = float
  15. PAYMENTS (Pembayaran) = float
  16. MINIMUM_PAYMENTS (Pembayaran Minimum) = float
  17. PRC_FULL_PAYMENT (Persentase Pembayaran Penuh) = float
  18. TENURE (Jangka Waktu) = float

### Data Collection
Tahapan pengumpulan data mencakup proses memperoleh dataset yang akan digunakan untuk proyek analisis. Dalam konteks dataset "CC GENERAL.csv", data ini mungkin telah dikumpulkan dari berbagai sumber atau sistem pelaporan internal perusahaan kartu kredit. Proses pengumpulan data dapat melibatkan ekstraksi dari database internal, penyediaan data dari mitra bisnis, atau pengumpulan data dari berbagai transaksi dan kegiatan pelanggan.