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
    manipulate_image('gambar.jpg', 'result.jpg')