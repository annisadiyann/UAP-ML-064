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

## 🔴 Evaluasi Model 🟢

Di bawah ini adalah hasil evaluasi untuk ketiga model yang telah dilatih.

### Confusion Matrix
Matriks ini menunjukkan performa prediksi model pada data uji untuk setiap kelas.

| CNN Custom | VGG16 | ResNet50 |
| :---: | :---: | :---: |
| ![CM CNN](path/ke/gambar/cm_cnn.png) | ![CM VGG] <img width="519" height="435" alt="image" src="https://github.com/user-attachments/assets/c83549fa-7560-4176-93a8-488858360955" />
 | ![CM ResNet](path/ke/gambar/cm_resnet.png) |


### Learning Curves 📈
Grafik di bawah ini menunjukkan proses belajar model (Loss & Accuracy) selama fase pelatihan dan validasi.

| CNN Custom | VGG16 / ResNet50 |
| :---: | :---: |
| ![Plot CNN](path/ke/gambar/plot_cnn.png) | ![Plot VGG](path/ke/gambar/plot_vgg.png) |


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
