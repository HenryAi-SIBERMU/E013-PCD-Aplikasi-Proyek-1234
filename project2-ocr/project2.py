# Impor paket yang diperlukan
import cv2
import pytesseract

# Sebutkan lokasi yang diinstal Tesseract-OCR di sistem Anda
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\yooma\AppData\Local\Tesseract-OCR\tesseract.exe'

# Baca gambar dari mana teks perlu diekstrak
img = cv2.imread("sample3.jpg")

# Pemrosesan awal gambar dimulai
# Ubah gambar menjadi skala abu-abu
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Melakukan ambang OTSU
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU |
cv2.THRESH_BINARY_INV)

# Tentukan bentuk struktur dan ukuran kernel.
# Ukuran kernel meningkatkan atau mengurangi area
# persegi panjang yang akan terdeteksi.
# Nilai kernel yang lebih kecil seperti (10, 10) akan mendeteksi
# setiap kata daripada kalimat.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Menerapkan dilasi pada gambar ambang
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

# Menemukan kontur
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_NONE)

# Membuat salinan gambar
im2 = img.copy()

# Sebuah file teks dibuat dan dikosongkan
file = open("recognized.txt", "w+")
file.write("")
file.close()

# Melalui kontur yang teridentifikasi
# Kemudian bagian berbentuk persegi panjang dipotong dan diteruskan
# ke pytesseract untuk mengekstrak teks darinya
# Teks yang diekstrak kemudian ditulis ke dalam file teks
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

# Menggambar persegi panjang pada gambar yang disalin
rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Memotong blok teks untuk memberikan masukan ke OCR
cropped = im2[y:y + h, x:x + w]

# Buka file dalam mode penambahan
file = open("recognized.txt", "a")

# Terapkan OCR pada gambar yang dipotong
text = pytesseract.image_to_string(cropped)

# Menambahkan teks ke dalam file
file.write(text)
file.write("\n")

# Tutup file
file.close