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
|<img width="1387" height="1489" alt="image" src="https://github.com/user-attachments/assets/b34d5f22-cb53-4997-bcfd-5151af9a1786" />|<img width="519" height="435" alt="image" src="https://github.com/user-attachments/assets/c83549fa-7560-4176-93a8-488858360955" />|<img width="777" height="836" alt="image" src="https://github.com/user-attachments/assets/d8749d11-af0c-401b-907b-d0a7a3d1c0a9" />|


### Learning Curves 📈
Grafik di bawah ini menunjukkan proses belajar model (Loss & Accuracy) selama fase pelatihan dan validasi.

| CNN Custom | VGG16 | ResNet50 |
| :---: | :---: |
|<img width="1189" height="390" alt="image" src="https://github.com/user-attachments/assets/c7c9f52f-a8ef-42e9-81ac-7130b849fcd7" />|<img width="990" height="374" alt="image" src="https://github.com/user-attachments/assets/52c5247b-2edc-4c1b-aae7-623aaf87a03e" />|<img width="565" height="435" alt="image" src="https://github.com/user-attachments/assets/9e440764-865a-4963-929c-235fe1b9f61a" />|

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
