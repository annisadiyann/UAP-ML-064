# 🏠 Klasifikasi Rumah Adat Indonesia Menggunakan Deep Learning

Proyek ini merupakan sistem identifikasi jenis rumah adat Indonesia berbasis citra menggunakan tiga arsitektur *Deep Learning*: **CNN Custom**, **VGG16**, dan **ResNet50**. Sistem ini dilengkapi dengan dashboard interaktif berbasis web menggunakan **Streamlit**.

## 📋 Daftar Isi
1. [Deskripsi Proyek](#deskripsi-proyek)
2. [Dataset](#dataset)
3. [Preprocessing](#preprocessing)
4. [Penjelasan Model](#penjelasan-model)
5. [Evaluasi Model](#evaluasi-model)
6. [Analisis Perbandingan](#analisis-perbandingan)
7. [Panduan Menjalankan Sistem](#panduan-menjalankan-sistem)
8. [Link Live Demo](#link-live-demo)

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

Tampilan tabel Anda terlihat berantakan karena nilai atribut `width` dan `height` yang ada pada tag `<img>` saat ini mengikuti resolusi asli gambar yang sangat besar (seperti `1387x1489`). GitHub akan mencoba menampilkan ukuran tersebut apa adanya kecuali kita membatasinya.

Untuk menyamakan ukurannya agar rapi dan simetris, Anda perlu menghapus atribut `height` dan mengatur `width` ke angka yang sama (misalnya `300` atau `100%`).

Berikut adalah perbaikan kode untuk bagian **Evaluasi Model** Anda:

---

### 🔴 Evaluasi Model 🟢

Di bawah ini adalah hasil evaluasi performa untuk ketiga arsitektur model yang telah dilatih.

#### 1. Confusion Matrix

Matriks ini menunjukkan ketepatan prediksi model pada data uji untuk setiap kelas rumah adat.

| CNN Custom | VGG16 | ResNet50 |
| --- | --- | --- |
| <img src="CM CNN.png" width="300"> | <img src="CM VGG.png" width="300"> | <img src="CM RESNET.png" width="300"> |

#### 2. Learning Curves 📈

Grafik di bawah ini menunjukkan proses belajar model (Loss & Accuracy) selama fase pelatihan (*training*) dan validasi (*validation*).

| CNN Custom | VGG16 | ResNet50 |
| --- | --- | --- |
| <img src="PLOT CNN.png" width="300"> | <img src="VGG PLOT.png" width="300"> | <img src="PLOT RES.png" width="300"> |

## 📈 Analisis Perbandingan

| Nama Model | Akurasi | Hasil Analisis |
| --- | --- | --- |
| **CNN Custom** | **92%** | Menunjukkan sedikit fluktuasi pada learning curve, menandakan *overfitting* ringan. |
| **VGG16** | **100%** | Sangat stabil dengan akurasi sempurna pada seluruh data uji. |
| **ResNet50** | **100%** | **Model Terbaik**. Kurva loss paling rendah dan konvergensi paling cepat. |

---

## 🚀 Panduan Menjalankan Sistem
1. **Clone & Install**:
   ```bash
   git clone [https://github.com/annisadiyann/UAP-ML-064.git](https://github.com/annisadiyann/UAP-ML-064.git)
   pip install -r requirements.txt

```

2. **Run Streamlit**:
```bash
streamlit run src/app.py

```



## 🔗 Link Live Demo

👉 [https://uap-ml-064.streamlit.app/](https://uap-ml-064.streamlit.app/)

---

**Dibuat oleh: Annisa Diyan Novitasari (202210370311064)**

```
