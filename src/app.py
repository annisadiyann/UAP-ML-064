import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

# --- IMPORT PREPROCESSING KHUSUS ---
# Ini penting agar ResNet dan VGG tidak salah prediksi (tidak selalu menebak Honai)
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet_preprocess
from tensorflow.keras.applications.vgg16 import preprocess_input as vgg_preprocess

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Dashboard Klasifikasi Rumah Adat", layout="centered")

st.title("🏠 Dashboard Klasifikasi Rumah Adat")
st.write("Unggah foto rumah adat untuk diidentifikasi oleh model AI.")

# --- LOAD MODEL ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_options = {
    "CNN Custom (V1)": os.path.join(BASE_DIR, "models", "omah_classification_model_v1.h5"),
    "VGG16 Final": os.path.join(BASE_DIR, "models", "model_omah_vgg16_final.h5"),
    "ResNet50 Final": os.path.join(BASE_DIR, "models", "model_omah_resnet_final.h5")
}

selected_model_name = st.sidebar.selectbox("Pilih Model AI", list(model_options.keys()))

@st.cache_resource
def load_prediction_model(model_path):
    return tf.keras.models.load_model(model_path)

# Memuat model yang dipilih
try:
    model = load_prediction_model(model_options[selected_model_name])
    st.sidebar.success(f"Berhasil memuat {selected_model_name}")
except Exception as e:
    st.sidebar.error(f"Gagal memuat model: {e}")

# --- DAFTAR KELAS ---
# Urutan sesuai indices: 0=gadang, 1=honai, 2=joglo, 3=panjang, 4=tongkonan
class_names = ['Gadang', 'Honai', 'Joglo', 'Panjang', 'Tongkonan']

def predict(image, model, model_type):
    # Paksa ke RGB untuk menangani file PNG transparan
    image = image.convert('RGB')
    img = image.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # Preprocessing spesifik model
    if "ResNet" in model_type:
        img_array = resnet_preprocess(img_array)
    elif "VGG" in model_type:
        img_array = vgg_preprocess(img_array)
    else:
        img_array = img_array / 255.0  # Normalisasi standar untuk CNN Custom
        
    predictions = model.predict(img_array)
    
    # Mengambil indeks dengan probabilitas tertinggi
    predicted_index = np.argmax(predictions[0])
    confidence = np.max(predictions[0])
    
    return class_names[predicted_index], confidence

# --- ANTARMUKA UNGGAH GAMBAR ---
uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar yang diunggah', use_column_width=True)
    
    if st.button('Klasifikasi Sekarang'):
        with st.spinner('Sedang menganalisis...'):
            # PERBAIKAN: Menambahkan argumen ketiga 'selected_model_name'
            label, confidence = predict(image, model, selected_model_name)
            
            # --- TAMPILKAN HASIL ---
            st.success(f"### Hasil Prediksi: **{label}**")
            st.info(f"Tingkat Keyakinan: **{confidence*100:.2f}%**")
            
            # Visualisasi Keyakinan
            st.progress(float(confidence))