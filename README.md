# Tugas 2: Implementasi Model-View-Template (MVT) pada Django

### Kevin Cornellius Widjaja - NPM: 2406428781 - Kelas: PBP E 
#### Link Deployment: https://kevin-cornellius-kickstack.pbp.cs.ui.ac.id/

---
## **Q1:** Jelaskan bagaimana cara kamu mengimplementasikan checklist secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**A:** Selain mengikuti Tutorial 0 dan Tutorial 1, saya mencoba untuk mengerti dengan dalam setiap step yang saya lakukan (fungsinya, dan cara menggunakannya), terutama dalam mengimplementasikan MVT, dalam prosesnya, saya banyak mengakses [dokumentasi Django](https://docs.djangoproject.com/en/5.2/) & bertanya kepada LLM untuk memahami lebih tentang development Django. Selain itu, saya mencoba untuk mengexplore lebih tentang Django dan HTML untuk mempersiapkan diri saya dengan baik untuk tugas kedepannya. Hal ini meliputi admin pages Django, dan styling HTML ([TailwindCSS](https://tailwindcss.com) & [DaisyUI](https://daisyui.com/)).

Untuk mengimplementasikan checklist, saya melakukan hal-hal berikut:
1. Membuat folder project baru, dan melakukan setup untuk python virtual environment, `requirements.txt`, dan menginstall dependencies yang diperlukan.
2. Membuat project Django baru dengan nama `kick_stack` dengan `django-admin startproject` di dalam folder.
3. Mengkonfigurasi `settings.py`, untuk menghubungkan project dengan database, dan `git` untuk version control (beserta `github`).
4. Mulai mengimplementasikan **MVT** dengan membuat app `main` dalam project.
5. Membuat model `Product` dalam `models.py` dan melakukan migrasi untuk mengaplikasikannya ke database
6. Membuat template dengan plain html didalam aplikasi `main` didalam directory `template`
7. Mengkonfigurasi url routing dengan `views.py` dalam app `main` dan `urls.py` dalam directory project (`kick_stack`) dan app `main`
8. Mengintegrasikan `TailwindCSS` dan `DaisyUI` untuk digunakan pada HTML di template untuk mempermudah styling.
9. Meregistrasikan model `Product` dalam `admin.py` untuk memungkinkan addition product, dan membuat kredensial admin dengan `python manage.py createsuperuser`
10. Melakukan deployment ke PWS

---



## **Q2:** Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

**A:** \
<img width="668" height="390" alt="image" src="https://github.com/user-attachments/assets/7525ffd1-44d6-4983-8ace-62423410198a" /> \
(Dibuat di [mermaid.live](https://www.mermaidchart.com/app/projects/74d4650b-a36b-41eb-855f-0600741939af/diagrams/45131de3-26e9-41b7-acf1-1e92f077bb38/version/v0.1/edit))

Alur request client ke web aplikasi berbasis Django: 
1. `urls.py` memeriksa pola URL -> jika cocok -> teruskan ke `views.py`, jika tidak -> `error 404`.
2. `views.py` memproses logika, memungkinkan untuk query data ke `models.py`.
3. `models.py` berinteraksi dengan database untuk mengirim balik data.
4. `views.py` merender `templates` HTML dengan data.
5. Hasilnya dibungkus dalam `HttpResponse` untuk dikirim ke client/browser.

---

## **Q3:** Jelaskan peran `settings.py` dalam proyek Django!

**A:** `settings.py` adalah file konfigurasi utama dalam proyek Django untuk mengatur jalannya aplikasi.
Konfigurasi ini meliputi hal-hal seperti (but not limited to):
1. Database: engine, nama database, user, password, host, dan port.
2. Installed Apps: daftar aplikasi bawaan maupun custom yang digunakan dalam proyek.
3. Middleware 
4. Static & Media Files: lokasi file statis (CSS, JS, gambar) dan file upload.
5. Security: `SECRET_KEY`, `ALLOWED_HOSTS`, `CSRF`, dan pengaturan autentikasi.
6. Debugging
7. Internationalization: bahasa (`LANGUAGE_CODE`) dan zona waktu (`TIME_ZONE`).

Singkatnya, `settings.py` berperan untuk memberitahu Django bagaimana untuk menjalankan aplikasi ini sesuai dengan konfigurasi & environment yang diinginkan

---
## **Q4:** Bagaimana cara kerja migrasi database di Django?

**A:** Migrasi database berguna untuk menyinkronisasi struktur tabel database dengan model yang ada pada aplikasi. Di Django, untuk melakukan migrasi, kita harus melakukan:
1. Mendefinisikan model di `models.py`
2. Jalankan command `python manage.py makemigrations` agar Django membaca perubahan model lalu membuat file migrasi (berisi instruksi SQL dalam bentuk Python).
3. Melakukan `python manage.py migrate`. Dimana Django menerjemahkan file migrasi tadi menjadi perintah SQL yang dijalankan ke database.
4. Django kemudian menyimpan catatan migrasi yang sudah dijalankan di `migrations`, sehingga tidak dieksekusi dua kali.

---
## **Q5:**  Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

**A:** Menurut saya, Django cocok digunakan sebagai pengenalan untuk pembelajaran perangkat lunak, karena penggunaanya yang relatif mudah, dengan menggunakan bahasa `Python` yang memiliki sintaks relatif mudah, Django juga sudah datang sepaket dengan fitur-fitur penting dalam pengembangan apps seperti ORM, Autentikasi, Admin Panel, Routing, Unit Test, dan lain-lain, yang membantu kita (khususnya pemula) dalam mengembangkan aplikasi fullstack dengan cepat. 

Selain itu, dokumentasi Django juga lumayan lengkap dan penggunaannya sudah lumayan masif, sehingga banyak komunitas yang dapat membantu kita dengan tutorial, blog, dan solusi dari permasalahan yang mungkin muncul dalam pengembangan.

Dengan kemudahannya, Django juga cukup kuat untuk project besar, dan banyak digunakan dalam dunia profesional, sehingga menurut saya Django pilihan yang sangat cocok untuk permulaan dalam membangun & mempelajari praktik **software engineering** yang baik.

---
## **Q6:**  Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

**A:** Menurut saya tutorial sudah sangat baik, dokumentasi dari tutorial sudah sangat lengkap dan memudahkan saya dalam mempelajari Django, mungkin sedikit feedback dari saya, untuk memprioritaskan pemahaman dibanding hasil akhir, sehingga mahasiswa tidak cenderung hanya "copy-paste", namun juga meluangkan waktu untuk memahami setiap stepnya dengan baik.

---

# Checklist Tugas

- [X] Membuat sebuah proyek Django baru.
- [X] Membuat aplikasi dengan nama main pada proyek tersebut.
- [X] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- [X] Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
  - [X] name sebagai nama item dengan tipe CharField.
  - [X] price sebagai harga item dengan tipe IntegerField.
  - [X] description sebagai deskripsi item dengan tipe TextField.
  - [X] thumbnail sebagai gambar item dengan tipe URLField.
  - [X] category sebagai kategori item dengan tipe CharField.
  - [X] is_featured sebagai status unggulan item dengan tipe BooleanField.
- [X] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [X] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- [X] Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [X] Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
  - [X] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  - [X] Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
  - [X] Jelaskan peran settings.py dalam proyek Django!
  - [X] Bagaimana cara kerja migrasi database di Django?
  - [X] Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
  - [X] Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
