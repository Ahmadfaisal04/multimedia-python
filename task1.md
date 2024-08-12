# 🎓 Praktikum 1: Memeriksa Instalasi Pustaka Multimedia di Python

## 📋 Tujuan

Memastikan bahwa pustaka multimedia yang dibutuhkan untuk pemrograman multimedia dengan Python telah terinstal dengan benar.

## 🛠 Pustaka yang Diperlukan

1. Pygame
2. Pillow
3. OpenCV
4. MoviePy
5. Pydub
6. Tkinter

## 📦 Instalasi

### Langkah 1: Instalasi Pustaka

1. Buka terminal atau command prompt.
2. Jalankan perintah berikut untuk menginstal pustaka yang diperlukan:

   ```bash
   pip install pygame pillow opencv-python moviepy pydub
   ```

### Langkah 2: Instalasi Tkinter

Tkinter biasanya sudah terinstal secara default bersama dengan Python. Jika belum, ikuti langkah berikut:

- **Windows:**
  Tkinter sudah termasuk dalam instalasi Python di Windows.

- **Linux:**
  Jalankan perintah berikut:

  ```bash
  sudo apt-get install python3-tk
  ```

## 📜 Kode untuk Memeriksa Instalasi

Buat file Python baru dengan nama `check_installation.py`, kemudian salin kode berikut:

```python
import pygame
import PIL
import cv2
import moviepy.editor as mp
import pydub
import tkinter as tk

def check_installation():
    print("✅ Pygame version:", pygame.__version__)
    print("✅ Pillow version:", PIL.__version__)
    print("✅ OpenCV version:", cv2.__version__)
    print("✅ MoviePy version:", mp.__version__)
    print("✅ Pydub version:", pydub.__version__)
    print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()
```

## 🚀 Menjalankan Praktikum

1. Buka terminal atau command prompt.
2. Arahkan ke direktori tempat file `check_installation.py` disimpan.
3. Jalankan perintah berikut:

   ```bash
   python check_installation.py
   ```

## 🔍 Hasil yang Diharapkan

Jika semua pustaka terinstal dengan benar, Anda akan melihat output seperti berikut:

```
✅ Pygame version: <versi pygame>
✅ Pillow version: <versi pillow>
✅ OpenCV version: <versi opencv>
✅ MoviePy version: <versi moviepy>
✅ Pydub version: <versi pydub>
✅ Tkinter is installed and working!
```

Ambil screenshot hasil dari output tersebut sebagai bukti bahwa semua pustaka telah terinstal dengan benar.

## 📝 Catatan

- Pastikan Python telah terinstal pada sistem Anda. Anda bisa mengunduhnya dari [python.org](https://www.python.org/).
- Jika ada masalah dengan instalasi, pastikan Anda menggunakan versi Python yang didukung oleh pustaka-pustaka tersebut.

## 📚 Referensi

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [MoviePy Documentation](https://zulko.github.io/moviepy/)
- [Pydub Documentation](https://pydub.com/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

---
