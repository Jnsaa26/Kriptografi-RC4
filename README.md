# Kriptografi-RC4
Tugas Keamanan Data &amp; Informasi

# Implementasi Algoritma Kriptografi RC4 🔐

Repositori ini berisi implementasi algoritma kriptografi simetris **RC4 (Rivest Cipher 4)** berjenis *stream cipher*. Program ini dibuat dari awal (*from scratch*) menggunakan Python tanpa menggunakan *library* enkripsi instan, sebagai bagian dari penyelesaian Tugas Mata Kuliah Keamanan Data dan Informasi.

## 📝 Fitur
Program ini mencakup demonstrasi langkah demi langkah dari:
1. **KSA (Key-Scheduling Algorithm):** Mengacak *array* 0-255 menggunakan Kunci Rahasia.
2. **PRGA (Pseudo-Random Generation Algorithm):** Menghasilkan *Keystream* acak.
3. **Enkripsi:** Melakukan operasi XOR antara *Plaintext* dan *Keystream* untuk menghasilkan *Ciphertext* (ditampilkan dalam format Hexadesimal).
4. **Dekripsi:** Mengembalikan *Ciphertext* menjadi *Plaintext* utuh menggunakan fungsi yang sama persis.

## 💻 Prasyarat
- Python 3.x telah terinstal di komputer Anda.

## 🚀 Cara Menjalankan Program

1. *Clone* repositori ini atau *download* file `rc4_demo.py` ke komputer anda.
   git clone [https://github.com/USERNAME_ANDA/Tugas-Kriptografi-RC4.git](https://github.com/jnsaa__/Tugas-Kriptografi-RC4.git)

2. Buka terminal atau command prompt, lalu navigasikan ke direktori tempat file disimpan.

3. Jalankan perintah berikut: python rc4_demo.py

⚠️ Catatan Keamanan
Algoritma RC4 saat ini sudah dianggap tidak aman (deprecated) untuk penggunaan di dunia nyata (seperti pada WEP atau SSL) karena rentan terhadap serangan analisis keystream. Kode ini dibuat khusus untuk tujuan edukasi dan demonstrasi pemahaman cara kerja algoritma kriptografi.

Made it by: Julian Esa Mahendra Putra (24051204018)
