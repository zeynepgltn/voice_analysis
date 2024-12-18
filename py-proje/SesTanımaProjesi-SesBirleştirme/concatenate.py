from pydub import AudioSegment

def combine_wav_files(file_list, output_file):
    # İlk dosyayı açarak başlıyoruz
    combined = AudioSegment.from_wav(file_list[0])
    
    # Diğer dosyaları sırayla ekliyoruz
    for file in file_list[1:]:
        audio = AudioSegment.from_wav(file)
        combined += audio  # Sesleri sırayla birleştir
    
    # Birleştirilmiş sesi WAV formatında dışa aktar
    combined.export(output_file, format="wav")
    print(f"WAV dosyaları başarıyla '{output_file}' olarak birleştirildi!")

# Kullanım
wav_dosyalari = ["voice_data/Rabia.wav", "voice_data/rabia2.wav"]  # WAV dosyalarının yolları
cikis_dosyasi = "birlesmis_ses.wav"
combine_wav_files(wav_dosyalari, cikis_dosyasi)
