import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import os

# Daftar label kelas
class_labels = ["Aluvial", "Andosol", "Entisol", "Humus", "Inceptisol", "Laterit", "Kapur", "Pasir"]

# Memuat Model
@st.cache_resource
def load_model():
    try:
        model_path = "Model_Terbaik.h5"
        
        if not os.path.exists(model_path):
            st.error(f"❌ Model file '{model_path}' tidak ditemukan!")
            st.info("Pastikan file Model_Terbaik.h5 ada di folder yang sama dengan app.py")
            return None
        
        model = tf.keras.models.load_model(model_path)
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

# Fungsi untuk preprocessing gambar
def preprocess_image(image):
    """Preprocessing gambar sesuai dengan kebutuhan model"""
    # Resize ke 299x299
    image = image.resize((299, 299))
    
    # Convert ke RGB jika RGBA
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    # Convert ke numpy array
    image_array = np.array(image)
    
    # Normalisasi (0-1)
    image_array = image_array / 255.0
    
    # Tambahkan batch dimension
    image_array = np.expand_dims(image_array, axis=0)
    
    return image_array

# Streamlit App
def main():
    st.set_page_config(
        page_title="Klasifikasi Jenis Tanah",
        page_icon="🌱",
        layout="centered"
    )
    
    st.title("🌱 Klasifikasi Citra Jenis Tanah")
    st.write("Upload foto tanah untuk mengetahui jenis tanahnya!")
    
    # Load model
    with st.spinner("Memuat model..."):
        model = load_model()
    
    if model is None:
        st.error("❌ Model tidak dapat dimuat. Silakan coba lagi nanti.")
        st.stop()
    else:
        st.success("✅ Model berhasil dimuat!")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Pilih foto tanah", 
        type=["jpg", "jpeg", "png"],
        help="Format yang didukung: JPG, JPEG, PNG"
    )
    
    if uploaded_file is not None:
        try:
            # Load dan tampilkan gambar
            image = Image.open(uploaded_file)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.image(
                    image, 
                    caption="Foto yang diunggah", 
                    use_container_width=True
                )
            
            with col2:
                with st.spinner("Menganalisis gambar..."):
                    # Preprocessing
                    processed_image = preprocess_image(image)
                    
                    # Prediksi
                    prediction = model.predict(processed_image, verbose=0)
                    
                    # Ambil indeks dengan probabilitas tertinggi
                    predicted_index = np.argmax(prediction)
                    confidence = float(prediction[0][predicted_index])
                    
                    # Ambil label berdasarkan indeks
                    predicted_label = class_labels[predicted_index]
                    
                    # Tampilkan hasil
                    st.success("✅ Analisis selesai!")
                    st.write(f"**Jenis Tanah:** {predicted_label}")
                    st.write(f"**Confidence:** {confidence:.2%}")
                    
                    # Progress bar untuk confidence
                    st.progress(confidence)
                    
                    # Tampilkan probabilitas semua kelas
                    with st.expander("Lihat detail probabilitas"):
                        for i, (label, prob) in enumerate(zip(class_labels, prediction[0])):
                            st.write(f"{label}: {prob:.3f} ({prob:.1%})")
        
        except Exception as e:
            st.error(f"❌ Error dalam memproses gambar: {e}")
    
    # Info tambahan
    with st.expander("ℹ️ Informasi Aplikasi"):
        st.write("""
        **Cara Menggunakan:**
        1. Upload foto tanah menggunakan tombol di atas
        2. Tunggu proses analisis selesai
        3. Lihat hasil prediksi dan tingkat confidence
        
        **Jenis Tanah yang Dapat Dideteksi:**
        - Aluvial, Andosol, Entisol, Humus
        - Inceptisol, Laterit, Kapur, Pasir
        
        **Tips untuk Hasil Terbaik:**
        - Gunakan foto dengan pencahayaan yang baik
        - Pastikan tanah terlihat jelas
        - Hindari bayangan atau pantulan
        """)
    
    # Footer
    st.markdown("---")
    # st.markdown("*Dikembangkan dengan ❤️ menggunakan Streamlit & TensorFlow*")

if __name__ == "__main__":
    main()