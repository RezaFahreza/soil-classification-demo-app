# 🌱 Soil Classification App

Aplikasi web untuk klasifikasi jenis tanah menggunakan deep learning dan Streamlit.

## 🚀 Live Demo

[🔗 Coba aplikasi di sini](https://soil-classification-demo.streamlit.app/)

## 🎯 Fitur

- 📤 Upload foto tanah (JPG, JPEG, PNG)
- 🤖 Prediksi jenis tanah menggunakan AI
- 📊 Menampilkan confidence score
- 📋 Detail probabilitas untuk semua kelas
- 🎨 Interface yang user-friendly

## 🏷️ Jenis Tanah yang Dapat Dideteksi

1. **Aluvial** - Tanah endapan
2. **Andosol** - Tanah vulkanik
3. **Entisol** - Tanah muda
4. **Humus** - Tanah organik
5. **Inceptisol** - Tanah berkembang sedang
6. **Laterit** - Tanah tropis
7. **Kapur** - Tanah berkapur
8. **Pasir** - Tanah berpasir

## 🛠️ Tech Stack

- **Framework:** Streamlit
- **Machine Learning:** TensorFlow/Keras
- **Image Processing:** PIL (Pillow)
- **Deployment:** Streamlit Community Cloud

## 🏃‍♂️ Menjalankan Aplikasi Lokal

### Prasyarat
- Python 3.8+
- pip

### Langkah-langkah

1. **Clone repository:**
```bash
git clone https://github.com/RezaFahreza/soil-classification-app.git
cd soil-classification-app
```

2. **Buat virtual environment:**
```bash
python -m venv soil_classifier_env

# Windows
soil_classifier_env\Scripts\activate

# Mac/Linux
source soil_classifier_env/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Jalankan aplikasi:**
```bash
streamlit run app.py
```

5. **Buka browser:** http://localhost:8501

## 📊 Model Information

- **Architecture:** Convolutional Neural Network (CNN) with Transfer Learning Xception Architecture
- **Input Size:** 299x299 pixels
- **Classes:** 8 jenis tanah
- **Framework:** TensorFlow/Keras

## 📁 Struktur Project

```
soil-classification-app/
├── __init__.py          # Init file   
├── app.py               # Main application
├── Model_Terbaik.h5     # Trained model
├── requirements.txt     # Dependencies
├── .gitignore           # Git ignore rules
├── .gitattributes       # Specific attribute (.h5) file path  
└── README.md            # Documentation
```

## 🚀 Deployment

Aplikasi ini di-deploy menggunakan [Streamlit Community Cloud](https://streamlit.io/cloud). Setiap push ke repository akan otomatis trigger re-deployment.

## 🤝 Contributing

Contributions, issues, dan feature requests sangat welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👤 Author

**[Nama Anda]**
- GitHub: [@RezaFahreza](https://github.com/RezaFahreza)
- Email: rafahreza30@gmail.com

## 🙏 Acknowledgments

- Dataset dan model training
- Streamlit community
- TensorFlow team