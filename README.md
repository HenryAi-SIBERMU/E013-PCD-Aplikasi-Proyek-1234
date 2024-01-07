
# E013 PCD (Pengolahan Citra Digital) - Aplikasi Proyek 1,2,3,4

## 📍 Note Project 1 - Koordinat Gambar
1. Git Clone/Download repo
   
3. Tambahkan Script Berikut dibawah  `if __name__=="__main__` : 
```bash
   img = cv2.imread('image.jpeg', 1) 
   cv2.imshow('image', img) 
```

## 📍 Note Project 2 - OCR
1. Git Clone/Download repo
   
3. Install Tesseract OCR for windows/mac user
- [Tesseract OCR for Windows/Mac](https://github.com/UB-Mannheim/tesseract/wiki)

3. Copy Path Instalan Wajib di local seperti
- C:\Users\yooma\AppData\Local\Tesseract-OCR\tesseract.exe
  (Ganti `yooma` dengan user computer masing masing)

- Tambahkan Script Berikut dibawah `import pytesseract` (Ganti  `yooma` dengan nama user komputer masing masing): 
```bash
 pytesseract.pytesseract.tesseract_cmd = r'C:\Users\yooma\AppData\Local\Tesseract-OCR\tesseract.exe'
```
