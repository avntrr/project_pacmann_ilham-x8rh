# project_pacmann_ilham-x8rh
## Prediksi Kualitas Udara DKI Jakarta

Project ini mencoba untuk melakukan prediksi kualitas udara DKI Jakarta.
Dataset yang digunakan berasal dari Open Data Jakarta pada tautan berikut: https://data.jakarta.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-2021
Dataset berupa Indeks Standar Pencemar Udara (ISPU) yang diukur dari 5 stasiun pemantau kualitas udara (SPKU) yang ada di Provinsi DKI Jakarta Tahun 2021.
Aplikasi dibangun menggunakan Streamlit.


<b>Penggunaan</b>
- Download seluruh file
- Pastikan sudah terinstall Streamlit pada perangkat
- Buka file tugas_akhir_pacmann.ipynb dan lakukan update directory: params.yml dan semua file dengan ekstensi .pkl
- Buka file master.py
- Lakukan update directory params.yml sesuai dengan directory yang baru
<img width="436" alt="Screenshot 2022-12-03 at 21 10 56" src="https://user-images.githubusercontent.com/54851225/205445103-223e838c-c3c5-4487-8d71-a6545dd46bcf.png">

- Buka Streamlit via Terminal atau Command Promp dan jalankan:
```
Streamlit run master.py
```
- Masukkan nilai pada parameter yang disediakan:
<img width="304" alt="image" src="https://user-images.githubusercontent.com/54851225/205445795-bdf6dab0-686b-4523-9885-40aa89b72042.png">

- Klik Predict
- Hasil prediksi ditampilkan
<img width="342" alt="image" src="https://user-images.githubusercontent.com/54851225/205445818-f8b7421e-bfd4-45c7-ad37-b0532effaed8.png">
