# 🖼️🎵 Praktikum 2 Manipulasi Gambar dan Audio dengan Python

## 📋 Tujuan

Memastikan bahwa pustaka Pillow dan Pydub telah terinstal dengan benar serta memahami dan mengimplementasikan manipulasi gambar dan audio menggunakan pustaka tersebut.

## 🛠 Pustaka yang Diperlukan

1. Pillow
2. Pydub

## 📦 Instalasi

### Langkah 1: Instalasi Pillow

1. Buka terminal atau command prompt.
2. Jalankan perintah berikut untuk menginstal Pillow:

   ```bash
   pip install pillow
   ```

### Langkah 2: Instalasi Pydub

1. Buka terminal atau command prompt.
2. Jalankan perintah berikut untuk menginstal Pydub:

   ```bash
   pip install pydub
   ```

3. Pastikan Anda juga memiliki `ffmpeg` terinstal, karena diperlukan oleh Pydub untuk memproses file audio. Ikuti petunjuk instalasi di [FFmpeg Documentation](https://ffmpeg.org/download.html).

## 📜 Kode untuk Memeriksa Instalasi dan Menjalankan Operasi Lanjutan

### 🖼️ Manipulasi Gambar dengan Pillow

Buat file Python baru dengan nama `image_manipulation.py`, kemudian salin kode berikut:

```python
from PIL import Image, ImageFilter, ImageEnhance

def manipulate_image(input_path, output_path):
    try:
        # Memuat gambar
        image = Image.open(input_path)
        print("✅ Gambar berhasil dimuat")

        # Operasi Cropping dengan validasi ukuran
        if image.width > 200 and image.height > 200:
            cropped_image = image.crop((10, 10, 200, 200))
            cropped_image.save('cropped_' + output_path)
            print("✅ Cropping berhasil")
        else:
            raise ValueError("Gambar terlalu kecil untuk di-crop ke ukuran 200x200")

        # Operasi Resizing dengan rasio aspek yang dipertahankan
        resized_image = cropped_image.resize((100, 100), Image.ANTIALIAS)
        resized_image.save('resized_' + output_path)
        print("✅ Resizing berhasil")

        # Operasi Filtering
        filtered_image = resized_image.filter(ImageFilter.BLUR)
        filtered_image.save('filtered_' + output_path)
        print("✅ Filtering berhasil")

        # Operasi Pengaturan Kecerahan
        enhancer = ImageEnhance.Brightness(filtered_image)
        bright_image = enhancer.enhance(1.5)
        bright_image.save('bright_' + output_path)
        print("✅ Pengaturan kecerahan berhasil")

        # Operasi Penggabungan Gambar
        combined_image = Image.blend(filtered_image, bright_image, alpha=0.5)
        combined_image.save('combined_' + output_path)
        print("✅ Penggabungan gambar berhasil")

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_image('example.jpg', 'result.jpg')
```

### 🎵 Manipulasi Audio dengan Pydub

Buat file Python baru dengan nama `audio_manipulation.py`, kemudian salin kode berikut:

```python
from pydub import AudioSegment
from pydub.playback import play

def manipulate_audio(input_path, output_path):
    try:
        # Memuat file audio
        audio = AudioSegment.from_file(input_path)
        print("✅ Audio berhasil dimuat")

        # Operasi Pemotongan dengan validasi durasi
        if len(audio) > 10000:
            clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
            clipped_audio.export('clipped_' + output_path, format='mp3')
            print("✅ Pemotongan berhasil")
        else:
            raise ValueError("Durasi audio terlalu pendek untuk dipotong 10 detik")

        # Operasi Penggabungan dengan validasi durasi
        combined_audio = audio + clipped_audio
        combined_audio.export('combined_' + output_path, format='mp3')
        print("✅ Penggabungan berhasil")

        # Operasi Konversi Format
        audio.export('result.wav', format='wav')
        print("✅ Konversi format berhasil")

        # Operasi Pengaturan Volume dengan validasi
        if audio.dBFS < -10:
            louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
            louder_audio.export('louder_' + output_path, format='mp3')
            print("✅ Pengaturan volume berhasil")
        else:
            raise ValueError("Volume audio sudah terlalu tinggi")

        # Operasi Pemutaran Audio
        print("🔊 Memutar audio hasil manipulasi...")
        play(louder_audio)

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_audio('example.mp3', 'result.mp3')
```

## 🚀 Menjalankan Praktikum

1. **Manipulasi Gambar:**

   - Buka terminal atau command prompt.
   - Arahkan ke direktori tempat file `image_manipulation.py` disimpan.
   - Jalankan perintah berikut:

     ```bash
     python image_manipulation.py
     ```

2. **Manipulasi Audio:**

   - Buka terminal atau command prompt.
   - Arahkan ke direktori tempat file `audio_manipulation.py` disimpan.
   - Jalankan perintah berikut:

     ```bash
     python audio_manipulation.py
     ```

## 🔍 Hasil yang Diharapkan

### Manipulasi Gambar

Output di terminal:

```
✅ Gambar berhasil dimuat
✅ Cropping berhasil
✅ Resizing berhasil
✅ Filtering berhasil
✅ Pengaturan kecerahan berhasil
✅ Penggabungan gambar berhasil
```

File yang dihasilkan:

- `cropped_result.jpg`
- `resized_result.jpg`
- `filtered_result.jpg`
- `bright_result.jpg`
- `combined_result.jpg`

### Manipulasi Audio

Output di terminal:

```
✅ Audio berhasil dimuat
✅ Pemotongan berhasil
✅ Penggabungan berhasil
✅ Konversi format berhasil
✅ Pengaturan volume berhasil
🔊 Memutar audio hasil manipulasi...
```

File yang dihasilkan:

- `clipped_result.mp3`
- `combined_result.mp3`
- `result.wav`
- `louder_result.mp3`

Ambil screenshot hasil dari output di terminal sebagai bukti bahwa semua operasi telah berhasil.

## 📝 Catatan

- Pastikan Anda memiliki file gambar `example.jpg` dan file audio `example.mp3` di direktori yang sama dengan file Python.
- Jika ada masalah dengan instalasi atau eksekusi, pastikan Anda menggunakan versi Python yang didukung oleh pustaka-pustaka tersebut.
- Pastikan `ffmpeg` terinstal di sistem Anda untuk memproses file audio dengan Pydub.

## 📚 Referensi

- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
- [Pydub Documentation](https://pydub.com/)
- [FFmpeg Documentation](https://ffmpeg.org/download.html)

---
