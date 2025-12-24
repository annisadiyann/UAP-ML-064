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

Di bawah ini adalah hasil evaluasi untuk ketiga model yang telah dilatih.

### Confusion Matrix

Matriks ini menunjukkan performa prediksi model pada data uji untuk setiap kelas.

| CNN Custom | VGG16 | ResNet50 |
| --- | --- | --- |
| <img src="[https://github.com/user-attachments/assets/b34d5f22-cb53-4997-bcfd-5151af9a1786](https://github.com/user-attachments/assets/b34d5f22-cb53-4997-bcfd-5151af9a1786)" width="300"> | <img src="[https://github.com/user-attachments/assets/c83549fa-7560-4176-93a8-488858360955](https://github.com/user-attachments/assets/c83549fa-7560-4176-93a8-488858360955)" width="300"> | <img src="[https://github.com/user-attachments/assets/d8749d11-af0c-401b-907b-d0a7a3d1c0a9](https://github.com/user-attachments/assets/d8749d11-af0c-401b-907b-d0a7a3d1c0a9)" width="300"> |

### Learning Curves 📈

Grafik di bawah ini menunjukkan proses belajar model (Loss & Accuracy) selama fase pelatihan dan validasi.

| CNN Custom | VGG16 | ResNet50 |
| --- | --- | --- |
| <img src="[https://github.com/user-attachments/assets/c7c9f52f-a8ef-42e9-81ac-7130b849fcd7](https://github.com/user-attachments/assets/c7c9f52f-a8ef-42e9-81ac-7130b849fcd7)" width="300"> | <img src="[https://github.com/user-attachments/assets/52c5247b-2edc-4c1b-aae7-623aaf87a03e](https://github.com/user-attachments/assets/52c5247b-2edc-4c1b-aae7-623aaf87a03e)" width="300"> | <img src="[https://github.com/user-attachments/assets/9e440764-865a-4963-929c-235fe1b9f61a](https://github.com/user-attachments/assets/9e440764-865a-4963-929c-235fe1b9f61a)" width="300"> |

---

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
