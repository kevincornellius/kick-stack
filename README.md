## Tugas Individu
### Kevin Cornellius Widjaja - NPM: 2406428781 - Kelas: PBP E 
#### Link Deployment: https://kevin-cornellius-kickstack.pbp.cs.ui.ac.id/

<details><summary>Tugas 3: Implementasi Form dan Data Delivery pada Django</summary>

---
## **Q1:** Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

**A:** Data delivery sangat penting dalam suatu aplikasi, karena berfungsi sebagai penghubung yang memastikan data berpindah dan digunakan secara akurat, konsisten, dan real-time antar komponen seperti frontend, backend, database, maupun layanan eksternal lainnya, sehingga aplikasi dapat berjalan dengan lancar dan responsif. Contohnya, saat pengguna mengunggah data melalui frontend, data tersebut dikirim ke backend untuk diproses, disimpan ke database, lalu hasilnya ditampilkan kembali ke pengguna.

---

## **Q2:** Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

**A:** Saya sendiri sangat jarang menggunakan XML, dan lebih memilih JSON. Menurut saya, struktur JSON lebih intuitif karena menggunakan `key-value`. Karena strukturnya yang sederhana juga, membuat JSON lebih ringan dan ukuran datanya lebih kecil (dibandingan dengan XML yang memerlukan opening & closing tags). Proses parsing JSON juga lebih cepat karena tidak perlu membaca struktur tag yang kompleks seperti XML. Terlebih lagi, JSON sudah didukung secara langsung oleh hampir semua bahasa pemrograman modern. Karena alasan-alasan ini juga JSON lebih populer dibandingkan XML.

---
## **Q3:** Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

**A:** `is_valid()` pada form Django berfungsi untuk memeriksa apakah data yang dikirim ke form sesuai dengan aturan validasi yang telah ditentukan didalam form tersebut (misalnya `required`, tipe data, `max_length`, dll). Method ini mengembalikan nilai `True` jika data valid, dan `False` jika tidak. Kita membutuhkan method ini untuk memastikan bahwa data yang akan diproses atau disimpan ke database sudah benar dan sesuai dengan yang diharapkan, sehingga mencegah kesalahan atau inkonsistensi data.

Tanpa validasi ini, data yang tidak sesuai bisa masuk ke database, yang dapat menyebabkan masalah pada aplikasi, seperti error saat pengambilan data atau data yang tidak lengkap.

---

## **Q4:** Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

**A:** `csrf_token` dibutuhkan saat membuat form di Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery) yaitu serangan di mana penyerang memanfaat sesi login milik korban untuk mengirim permintaan ke server secara tidak bertanggung jawab, dan server akan mengira request tersebut valid karena berasal dari sesi yang valid.

`csrf_token` mencegah hal ini dengan menyisipkan token acak yang unik ke setiap permintaan POST. Dengan cara ini, penyerang tidak bisa memalsukan permintaan karena mereka tidak mengetahui token sah milik korban.

---

## **Q5:** Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**A:** Dalam mengerjakan tugas ini, saya banyak membaca tutorial sebelumnya karena materinya sangat mirip, saya juga membaca banyak dokumentasi dari internet dan bertanya ke LLM jika ada sesuatu yang lebih detail yang ingin saya ketahui. Secara singkat, step-by-step saya adalah:
1. Membuat fungsi & routing untuk melihat `Product` yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID. (Dengan melihat contoh tutorial)
2. Menambahkan halaman `/add-product` untuk menambahkan `Product` baru via form, dan `/product/<str:id>` untuk menampilkan setiap `Product` secara detail.
3. Mempercantik UI dengan vanilla CSS dan TailwindCSS
4. Melakukan commit ke GitHub, dan deployment ke PWS
5. Menjawab pertanyaan dalam `README.md` & Testing API `GET` via POSTMAN

---

## **Q6:** Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

**A:** Sudah sangat baik & ada sesi live coding di awal kelas.

---
## Dokumentasi Postman:

---
### Checklist Tugas

- [X] Tambahkan 4 fungsi `views` baru untuk melihat objek yang sudah ditambahkan dalam format:
    - [X] XML
    - [X] JSON
    - [X] XML by ID
    - [X] JSON by ID
- [X] Buat **routing URL** untuk masing-masing `views` yang telah ditambahkan.
- [X] Buat halaman yang menampilkan data objek model. Halaman ini harus memiliki:
    - [X] Tombol "Add" yang akan mengarah ke halaman formulir.
    - [X] Tombol "Detail" pada setiap data objek model untuk menampilkan halaman detail objek.
- [X] Buat halaman **formulir** untuk menambahkan objek model pada aplikasi sebelumnya.
- [X] Buat halaman yang menampilkan detail dari setiap data objek model.
- [X] Jawab pertanyaan-pertanyaan berikut pada berkas `README.md` di _root folder_:
    - [X] Mengapa kita memerlukan **data delivery** dalam pengimplementasian sebuah _platform_?
    - [X] Mana yang lebih baik antara **XML** dan **JSON**? Mengapa **JSON** lebih populer dibandingkan **XML**?
    - [X] Jelaskan fungsi dari method `is_valid()` pada formulir Django dan mengapa kita membutuhkannya.
    - [X] Mengapa kita membutuhkan `csrf_token` saat membuat formulir di Django? Apa yang dapat terjadi jika tidak ada `csrf_token`? Bagaimana hal ini dapat dimanfaatkan oleh penyerang?
    - [X] Jelaskan implementasi **_step-by-step_** dari daftar periksa di atas.
    - [X] Berikan _feedback_ untuk asdos pada tutorial 2.
- [X] Akses keempat URL di poin 2 menggunakan **Postman**.
- [ ] Buat **_screenshot_** dari hasil akses URL pada Postman dan tambahkan ke `README.md`.
- [X] Lakukan `add-commit-push` ke GitHub.
</details>



<details><summary>Tugas 2: Implementasi Model-View-Template (MVT) pada Django</summary>


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

</details>