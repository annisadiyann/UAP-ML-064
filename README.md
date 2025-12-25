# 🏠 Klasifikasi Rumah Adat Indonesia Menggunakan Deep Learning

Proyek ini merupakan sistem identifikasi jenis rumah adat Indonesia berbasis citra menggunakan tiga arsitektur *Deep Learning*: **CNN Custom**, **VGG16**, dan **ResNet50**. Sistem ini dilengkapi dengan dashboard interaktif berbasis web menggunakan **Streamlit**.

## 📋 Daftar Isi

1. [Deskripsi Proyek](#-deskripsi-proyek)
2. [Dataset](#-dataset)
3. [Preprocessing](#-preprocessing)
4. [Penjelasan Model](#-penjelasan-model)
5. [Evaluasi Model](#-evaluasi-model)
6. [Analisis Perbandingan](#-analisis-perbandingan)
7. [Panduan Menjalankan Sistem](#-panduan-menjalankan-sistem)
8. [Link Live Demo](#-link-live-demo)

---

## 📖 Deskripsi Proyek
Proyek ini bertujuan untuk mengklasifikasikan 5 jenis rumah adat: **Gadang, Honai, Joglo, Panjang, dan Tongkonan** menggunakan teknologi *Computer Vision*.

## 📊 Dataset
* **Jumlah Kelas**: 5 (Gadang, Honai, Joglo, Panjang, Tongkonan).
* **Format**: RGB Images.
* **Sumber**: [Kaggle - Rumah Adat](https://www.kaggle.com/datasets/rariffirmansah/rumah-adat).

## ⚙️ Preprocessing
* **Resizing**: Standarisasi citra ke ukuran 224x224 piksel.
* **Augmentasi**: Rotation, Zoom, Horizontal Flip.
* **Normalisasi**: Rescale 1/255 (CNN) dan Preprocess Input (VGG16 & ResNet50).

---

### 🔴 Evaluasi Model 🟢

Di bawah ini adalah hasil evaluasi performa untuk ketiga arsitektur model yang telah dilatih.

#### 1. Confusion Matrix

Matriks ini menunjukkan ketepatan prediksi model pada data uji untuk setiap kelas rumah adat.

| CNN Custom | VGG16 | ResNet50 |
| --- | --- | --- |
| <img src="assets/CM%20CNN.png" width="300"> | <img src="assets/CM%20VGG.png" width="300"> | <img src="assets/CM%20RESNET.png" width="300"> |

#### 2. Learning Curves 📈

Grafik di bawah ini menunjukkan proses belajar model (Loss & Accuracy) selama fase pelatihan (*training*) dan validasi (*validation*).

| CNN Custom | VGG16 | ResNet50 |
| --- | --- | --- |
| <img src="assets/PLOT%20CNN.png" width="300"> | <img src="assets/VGG%20PLOT.png" width="300"> | <img src="assets/PLOT%20RES.png" width="300"> |

---

## 📈 Analisis Perbandingan

| Nama Model | Akurasi | Hasil Analisis |
| --- | --- | --- |
| **CNN Custom** | **92%** | Menunjukkan sedikit fluktuasi pada learning curve, menandakan *overfitting* ringan. |
| **VGG16** | **100%** | Sangat stabil dengan akurasi sempurna pada seluruh data uji. |
| **ResNet50** | **100%** | **Model Terbaik**. Kurva loss paling rendah dan konvergensi paling cepat. |

---

## 🚀 Panduan Menjalankan Sistem Secara Lokal

Ikuti langkah-langkah di bawah ini untuk menjalankan dashboard interaktif **Streamlit** di perangkat Anda.

### 1. Persiapan Lingkungan (Prerequisites)

Pastikan Anda telah menginstal **Python (versi 3.9 - 3.11 direkomendasikan)** dan memiliki koneksi internet untuk mengunduh dependensi.

### 2. Clone Repositori

Buka terminal atau Command Prompt (CMD), lalu jalankan perintah berikut untuk mengunduh proyek:

```bash
git clone https://github.com/annisadiyann/UAP-ML-064.git
cd UAP-ML-064

```

### 3. Membuat Virtual Environment (Opsional namun Disarankan)

Untuk menjaga agar library tidak bentrok dengan proyek lain:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

```

### 4. Instalasi Dependensi

Instal semua pustaka yang diperlukan (TensorFlow, Streamlit, OpenCV, dll.) melalui file `requirements.txt`:

```bash
pip install -r requirements.txt

```

### 5. Menjalankan Aplikasi Streamlit

Setelah instalasi selesai, jalankan perintah berikut untuk membuka dashboard di browser Anda:

```bash
streamlit run src/app.py

```

Aplikasi biasanya akan otomatis terbuka di alamat `http://localhost:8501`.

---

## 🛠️ Cara Penggunaan Dashboard

1. **Pilih Model**: Pada sidebar atau menu utama, pilih salah satu dari tiga model tersedia (**CNN Custom, VGG16,** atau **ResNet50**).
2. **Unggah Gambar**: Klik tombol "Browse files" dan masukkan foto rumah adat (Gadang, Honai, Joglo, Panjang, atau Tongkonan).
3. **Prediksi**: Sistem akan memproses gambar dan menampilkan hasil klasifikasi beserta tingkat kepercayaan (*confidence score*).

---

## 🔗 Link Live Demo

👉 [https://uap-ml-064.streamlit.app/](https://uap-ml-064.streamlit.app/)

---

**Dibuat oleh: Annisa Diyan Novitasari (202210370311064)**

```
