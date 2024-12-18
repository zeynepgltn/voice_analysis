import pickle
import librosa
import numpy as np

#MFCC (Mel Frequency Cepstral Coefficients) özellikleri çıkaran fonksiyon
def extract_mfcc_features(audio_file):
    # Ses dosyasını yükler
    audio,sample_rate = librosa.load(audio_file, sr=None)
    # MFCC özelliklerini çıkarır
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
    # MFCC özelliklerini döndürür
    # Zaman boyutunda ortalama ve standart sapma alarak özetle
    mfccs_mean = np.mean(mfccs, axis=1)
    return mfccs_mean

#import model
model = pickle.load(open("ses_model.pkl", "rb"))
deneme_test_patch=extract_mfcc_features("voice_data/deneme.wav")
deneme_test_patch=deneme_test_patch.reshape(1,-1)
ses_tahmin=model.predict(deneme_test_patch)  
print(ses_tahmin)
