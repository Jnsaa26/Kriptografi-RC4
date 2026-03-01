def KSA(key):
    """Fungsi Pembangkitan Kunci: Mengacak array 0-255 berdasarkan kunci rahasia"""
    key_length = len(key)
    # Membuat array S berisi angka 0 sampai 255
    S = list(range(256)) 
    j = 0
    
    for i in range(256):
        # Mengacak urutan menggunakan kunci
        j = (j + S[i] + key[i % key_length]) % 256
        # Menukar nilai S[i] dan S[j]
        S[i], S[j] = S[j], S[i] 
        
    return S

def PRGA(S, text_length):
    """Fungsi Menghasilkan Keystream (Aliran Kunci Acak)"""
    i = 0
    j = 0
    keystream = []
    
    for _ in range(text_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        # Tukar lagi
        S[i], S[j] = S[j], S[i]
        
        # Ambil nilai acak
        t = (S[i] + S[j]) % 256
        keystream.append(S[t])
        
    return keystream

def enkripsi_dekripsi_rc4(key_text, input_text):
    """Fungsi Utama untuk Enkripsi dan Dekripsi"""
    # Ubah teks kunci dan teks pesan menjadi deretan angka ASCII
    key = [ord(c) for c in key_text]
    text = [ord(c) for c in input_text]
    
    print("\n--- MULAI PROSES RC4 ---")
    
    # Tahap 1: KSA
    S = KSA(key)
    print("1. KSA Selesai! Array berisi angka 0-255 telah berhasil diacak oleh kunci.")
    
    # Tahap 2: PRGA
    keystream = PRGA(S, len(text))
    print(f"2. PRGA Selesai! Keystream yang dihasilkan: {keystream}")
    
    # Tahap 3: XOR
    hasil = []
    for i in range(len(text)):
        # Operasi XOR antara teks asli dengan keystream
        xor_result = text[i] ^ keystream[i]
        hasil.append(xor_result)
        print(f"   Step-by-step XOR Byte {i+1}: Data '{text[i]}' XOR Keystream '{keystream[i]}' = '{xor_result}'")
        
    return hasil

# BAGIAN UNTUK DEMO
if __name__ == '__main__':
    # 1. Tentukan Pesan dan Kunci
    pesan_asli = "RAHASIA"
    kunci = "KUNCI"
    
    print(f"Pesan Asli: {pesan_asli}")
    print(f"Kunci Rahasia: {kunci}")
    
    # 2. PROSES ENKRIPSI
    print("\n[PROSES ENKRIPSI]")
    ciphertext_angka = enkripsi_dekripsi_rc4(kunci, pesan_asli)
    
    # Ubah ciphertext ke format HEX agar bisa dicetak dan dibaca di layar
    ciphertext_hex = [hex(c) for c in ciphertext_angka]
    print(f"\n>> HASIL ENKRIPSI (Ciphertext format HEX): {ciphertext_hex}")
    
    # 3. PROSES DEKRIPSI
    print("\n=============================================")
    print("\n[PROSES DEKRIPSI]")
    # Ubah kembali data hasil enkripsi (angka) menjadi teks ASCII biasa
    ciphertext_teks = "".join([chr(c) for c in ciphertext_angka])
    
    # Dekripsi menggunakan fungsi yang SAMA PERSIS dengan kunci yang sama
    plaintext_angka = enkripsi_dekripsi_rc4(kunci, ciphertext_teks)
    plaintext_teks = "".join([chr(c) for c in plaintext_angka])
    
    print(f"\n>> HASIL DEKRIPSI: {plaintext_teks}")