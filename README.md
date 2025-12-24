# 🏠 Klasifikasi Rumah Adat Indonesia Menggunakan Deep Learning

Proyek ini merupakan sistem identifikasi jenis rumah adat Indonesia berbasis citra menggunakan tiga arsitektur *Deep Learning*: **CNN Custom**, **VGG16**, dan **ResNet50**. Sistem ini dilengkapi dengan dashboard interaktif berbasis web menggunakan **Streamlit** untuk memfasilitasi pengguna dalam melakukan prediksi secara *real-time*.

## 📋 Daftar Isi

1. [Deskripsi Proyek](##deskripsi-proyek)
2. [Dataset dan Preprocessing](#dataset-dan-preprocessing)
3. [Penjelasan Model](#penjelasan-model)
4. [Hasil Evaluasi dan Analisis Perbandingan](#hasil-evaluasi-dan-analisis-perbandingan)
5. [Panduan Menjalankan Sistem](#panduan-menjalankan-sistem)
6. [Link Live Demo](#link-live-demo)
---

## 📖 Deskripsi Proyek

Proyek ini bertujuan untuk melestarikan budaya Indonesia melalui pemanfaatan teknologi kecerdasan buatan. Fokus utama proyek ini adalah mengklasifikasikan 5 jenis rumah adat: **Gadang, Honai, Joglo, Panjang, dan Tongkonan**.

## 📊 Dataset dan Preprocessing

Dataset terdiri dari ribuan gambar yang terbagi ke dalam 5 kategori rumah adat. Langkah-langkah pengolahan data meliputi:

* **Resizing**: Penyeragaman dimensi citra menjadi  piksel.
* **Augmentasi Data**: Penerapan teknik *rotation, zoom, horizontal flip,* dan *shift* untuk memperkaya variasi data training.
* **Normalisasi Spesifik**:
* **CNN Custom**: Menggunakan teknik *rescale*  untuk menstandarisasi nilai piksel.
* **VGG16 & ResNet50**: Menggunakan fungsi `preprocess_input` untuk menyesuaikan format input dengan standar *pre-trained model* (Zero-centering).



## 🧠 Penjelasan Model

Sistem ini membandingkan tiga pendekatan arsitektur yang berbeda:

1. **CNN Custom**: Arsitektur *Sequential* buatan sendiri yang terdiri dari lapisan *Convolutional*, *Max Pooling*, dan *Dropout*.
2. **VGG16 (Transfer Learning)**: Model yang memiliki kedalaman 16 lapisan, sangat efektif dalam mengekstraksi fitur tekstur bangunan yang detail.
3. **ResNet50 (Transfer Learning)**: Menggunakan mekanisme *Residual Blocks* untuk mengatasi masalah *vanishing gradient*, memberikan stabilitas tinggi pada model yang sangat dalam.

---

## 📈 Hasil Evaluasi dan Analisis Perbandingan

Berdasarkan pengujian pada data uji, berikut adalah ringkasan performa ketiga model:

| Nama Model | Akurasi | Hasil Analisis |
| --- | --- | --- |
| **CNN Custom** | **92%** | Memiliki performa solid namun kurva validasi menunjukkan fluktuasi, menandakan sedikit *overfitting*. Kesalahan terbanyak terjadi pada kemiripan antara rumah **Gadang** dan **Panjang**. |
| **VGG16** | **100%** | Memberikan hasil klasifikasi sempurna. Model sangat stabil dalam mengenali fitur unik tiap rumah adat tanpa adanya deviasi pada kurva akurasi. |
| **ResNet50** | **100%** | **Model Terbaik**. Menghasilkan akurasi maksimal dengan kurva *loss* yang paling mendekati nol. Sangat konsisten dalam membedakan pola halus pada seluruh data uji. |

---

## 🚀 Panduan Menjalankan Sistem

### 1. Persiapan Lingkungan

Clone repositori ini dan masuk ke direktori proyek:

```bash
git clone https://github.com/annisadiyann/UAP-ML-064.git
cd UAP-ML-064

```

### 2. Instalasi Dependensi

Pastikan Python sudah terinstal, lalu jalankan:

```bash
pip install -r requirements.txt

```

### 3. Menjalankan Website Secara Lokal

Jalankan perintah Streamlit untuk membuka dashboard:

```bash
streamlit run src/app.py

```
## 🔗 Link Live Demo
Anda dapat mengakses aplikasi secara langsung melalui tautan berikut:
[https://uap-ml-064.streamlit.app/](https://uap-ml-064.streamlit.app/)
---

## 🔗 Tautan Dataset
(https://www.kaggle.com/datasets/rariffirmansah/rumah-adat)
---

**Dibuat oleh: Annisa Diyan Novitasari (202210370311064)**

---
