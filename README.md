## Tugas Individu
### Kevin Cornellius Widjaja - NPM: 2406428781 - Kelas: PBP E 
#### Link Deployment: https://kevin-cornellius-kickstack.pbp.cs.ui.ac.id/


<details><summary>Tugas 6: Javascript dan AJAX
</summary>

## **Q1:** Apa perbedaan antara synchronous request dan asynchronous request?

**A:** Synchronous request adalah jenis permintaan di mana klien (seperti browser) mengirimkan permintaan ke server dan menunggu respons sebelum melanjutkan eksekusi kode berikutnya.

Sedangkan, Asynchronous request memungkinkan klien untuk mengirim permintaan ke server dan melanjutkan eksekusi kode tanpa menunggu respons dari server. Respons akan ditangani melalui callback atau promise ketika sudah tersedia.

---

## **Q2:** Bagaimana AJAX bekerja di Django (alur request–response)?

**A:**
1. Client (melalui Javascript) mengirimkan permintaan AJAX ke server Django menggunakan metode HTTP seperti GET atau POST.
2. Django URL routing menangani permintaan tersebut dan mengarahkan ke view yang sesuai.
3. View Django memproses permintaan, berinteraksi dengan model atau database jika diperlukan, dan menyiapkan data yang akan dikirim kembali ke client. Dan mengimbalikan data dalam format JSON atau HTML.
4. AJAX di sisi client menerima respons dari server, dan menggunakan data tersebut untuk memperbarui bagian tertentu dari halaman web tanpa perlu memuat ulang seluruh halaman.

---

## **Q3:** Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?

**A:** Keuntungan menggunakan AJAX dibandingkan render biasa di Django antara lain:
1. AJAX hanya memuat data yang diperlukan, bukan seluruh halaman, sehingga mengurangi beban jaringan dan mempercepat waktu respons.
2. Data dikirim dalam format yang ringan (seperti JSON), sehingga menghemat bandwidth dan mengurangi beban server.
3. Pengguna bisa berinteraksi dengan halaman web tanpa perlu menunggu seluruh halaman dimuat ulang, sehingga meningkatkan pengalaman pengguna (user experience).
4. AJAX memungkinkan pembaruan konten secara dinamis, sehingga aplikasi web terasa lebih responsif dan interaktif.
---

## **Q4:** Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

**A:** Keamanan AJAX untuk fitur Login dan Register di Django dapat dipastikan dengan beberapa cara, Pertama, semua permintaan AJAX harus dilakukan melalui HTTPS untuk mengenkripsi data yang dikirim antara client dan server. Kedua, pastikan setiap request POST menggunakan CSRF token untuk mencegah serangan CSRF. Ketiga, validasi dan sanitasi semua input dari pengguna di sisi server untuk mencegah serangan injeksi. Gunakan API autentikasi bawaan Django untuk mengelola sesi dan token autentikasi. 

Jangan kirimkan informasi sensitif seperti password dalam respons AJAX. Terakhir, batasi jumlah percobaan login untuk mencegah serangan brute force.

---

## **Q5:** Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

**A:** AJAX meningkatkan pengalaman pengguna (User Experience) pada website dengan memungkinkan interaksi yang lebih cepat dan responsif. Dengan AJAX, pengguna dapat melakukan tindakan seperti mengirim formulir, memuat konten baru, atau memperbarui bagian halaman tanpa perlu memuat ulang seluruh halaman. Hal ini mengurangi waktu tunggu dan membuat aplikasi web terasa lebih dinamis dan interaktif.

---

## Checklist Tugas
- [X] Mengubah fitur - fitur tugas sebelumnya menggunakan AJAX
  - [X] Fitur CRUD (Create Read Update Delete) product menggunakan AJAX (tidak boleh menggunakan dari context render kecuali untuk keperluan AJAX)
  - [X] Mengubah Login dan Register menggunakan AJAX.
- [X] Tampilan baru
  - [X] Membuat tombol yang akan menampilkan modal untuk create dan update product dalam bentuk form.
  - [X] Membuat modal konfirmasi saat pengguna ingin menghapus product
  - [X] Saat melakukan aksi dari modal, product akan di-refresh tanpa perlu melakukan reload halaman (Refresh melalui browser).
  - [X] Membuat tombol refresh yang akan menampilkan list product terbaru tanpa perlu reload halaman (Refresh melalui browser)
  - [X] Membuat Loading, Empty, dan Error state melalui Javascript.
  - [X] Menampilkan Toast saat create, update, atau delete product dan saat login, logout, dan register (tidak boleh sama persis dengan tutorial).
- [X] Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
  - [X] Apa perbedaan antara synchronous request dan asynchronous request?
  - [X] Bagaimana AJAX bekerja di Django (alur request–response)?
  - [X] Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
  - [X] Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
  - [X] Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
- [X] Melakukan add-commit-push ke GitHub.
</details>


<details><summary>Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS</summary>

---
## **Q1:** Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

**A**: Urutan prioritas pengambilan CSS selector adalah sebagai berikut:
1. `!important` - Jika sebuah aturan CSS memiliki `!important`, maka aturan tersebut akan memiliki prioritas tertinggi, mengabaikan aturan lain. 
Contoh: 
```css
p { color: blue !important; }
```
  
2. Inline Styles - Gaya yang diterapkan langsung pada elemen HTML menggunakan atribut `style` memiliki prioritas lebih tinggi daripada aturan dalam file CSS eksternal atau internal. 
Contoh: 
```html
<p style="color: red;">Teks</p>
```

3. ID Selectors - Selector yang menggunakan ID (`#id`) memiliki prioritas lebih tinggi daripada class, attribute, dan pseudo-class selectors. 
Contoh: 
```css
#header { color: blue; }
```

4. Class, Attribute, dan Pseudo-class Selectors - Selector yang menggunakan class (`.class`), atribut (`[type="text"]`), atau pseudo-class (`:hover`) memiliki prioritas lebih rendah daripada ID selectors tetapi lebih tinggi daripada element selectors.
Contoh:
```css
.teks { color: green; }
[type="text"] { ... }
p:hover { ... }
```

5. Element Selectors - Selector yang menggunakan nama elemen HTML (seperti `div`, `p`, `h1`) memiliki prioritas paling rendah.
Contoh:
```css
p { color: black; }
p::first-letter { ... }
```

> Jika specificity sama, yang didefinisikan terakhir dalam CSS (lebih bawah dalam file atau terakhir dimuat) akan menang.

> Selector gabungan menambah specificity: `div#header .menu a:hover > #header a.`

---

## **Q2**: Mengapa *responsive design* menjadi konsep yang penting dalam pengembangan aplikasi *web*? Berikan contoh aplikasi yang sudah dan belum menerapkan *responsive design*, serta jelaskan mengapa!

**A**: Responsive design penting karena memastikan aplikasi web dapat diakses dan digunakan dengan baik di berbagai perangkat (desktop, tablet, smartphone) dengan ukuran layar dan resolusi yang berbeda. Dengan responsive design, elemen-elemen pada halaman web dapat menyesuaikan tata letak, ukuran, dan interaktivitasnya sesuai dengan perangkat yang digunakan, sehingga meningkatkan pengalaman pengguna (user experience).


Contoh aplikasi yang sudah menerapkan responsive design adalah [YouTube](https://www.youtube.com) dan [Laman PBP 25/26](https://pbp-fasilkom-ui.github.io/ganjil-2026/). Kedua situs ini menyesuaikan tata letak dan ukuran elemen secara otomatis berdasarkan ukuran layar perangkat, sehingga pengguna dapat dengan mudah menavigasi dan mengakses konten tanpa harus memperbesar atau memperkecil halaman.

Contoh aplikasi yang belum menerapkan responsive design adalah [SiakNG](https://academic.ui.ac.id). Situs ini memiliki tata letak yang tetap dan tidak menyesuaikan dengan ukuran layar perangkat, sehingga pada perangkat dengan layar kecil (seperti smartphone), pengguna harus memperbesar halaman untuk melihat konten, yang dapat mengurangi kenyamanan dan kemudahan penggunaan.

---

## **Q3**: Jelaskan perbedaan antara *margin*, *border*, dan *padding*, serta cara untuk mengimplementasikan ketiga hal tersebut!
**A**: Dalam CSS, *margin*, *border*, dan *padding* adalah properti yang digunakan untuk mengatur ruang di sekitar elemen HTML, tetapi mereka memiliki fungsi dan lokasi yang berbeda:

1. Margin: 
   - Margin adalah ruang di luar border elemen. 
   - Fungsinya untuk memberikan jarak antara elemen dengan elemen lainnya di sekitarnya.
   - Cara mengimplementasikan margin:
     ```css
     .element {
       margin: 20px; /* Memberikan margin 20px di semua sisi */
       margin-top: 10px; /* Margin atas 10px */
       margin-right: 15px; /* Margin kanan 15px */
       margin-bottom: 10px; /* Margin bawah 10px */
       margin-left: 15px; /* Margin kiri 15px */
     }
     ```
2. Border:
   - Border adalah garis yang mengelilingi elemen, berada di antara padding dan margin.
   - Fungsinya untuk memberikan batas visual pada elemen.
   - Cara mengimplementasikan border:
     ```css
     .element {
       border: 2px solid black; /* Border 2px, solid, warna hitam */
       border-top: 1px dashed red; /* Border atas 1px, dashed, warna merah */
       border-radius: 5px; /* Membuat sudut border melengkung */
     }
     ```

3. Padding:
    - Padding adalah ruang di dalam border elemen, antara konten elemen dan border.
    - Fungsinya untuk memberikan jarak antara konten elemen dengan border.
    - Cara mengimplementasikan padding:
      ```css
      .element {
        padding: 15px; /* Memberikan padding 15px di semua sisi */
        padding-top: 10px; /* Padding atas 10px */
        padding-right: 20px; /* Padding kanan 20px */
        padding-bottom: 10px; /* Padding bawah 10px */
        padding-left: 20px; /* Padding kiri 20px */
      }
      ```

---

## **Q4**: Jelaskan konsep *flex box* dan *grid layout* beserta kegunaannya!

**A**: 
- **Flexbox (Flexible Box Layout)** adalah model tata letak satu dimensi yang dirancang untuk mengatur elemen dalam satu baris atau kolom.
  - Kegunaan Flexbox:
    - Mengatur elemen secara horizontal atau vertikal dengan mudah.
    - Menyediakan kontrol yang baik atas perataan, distribusi ruang, dan ukuran elemen.
    - Memudahkan pembuatan tata letak yang responsif.
  - Contoh penggunaan Flexbox:
    ```css
    .container {
      display: flex; /* Mengaktifkan Flexbox */
      justify-content: center; /* Mengatur elemen di tengah secara horizontal */
      align-items: center; /* Mengatur elemen di tengah secara vertikal */
    }
    ```
- **Grid Layout** adalah model tata letak dua dimensi yang memungkinkan elemen untuk disusun dalam baris dan kolom. Grid Layout sangat berguna untuk membuat tata letak yang kompleks dan terstruktur. Beberapa kegunaan Grid Layout antara lain:
  - Mengatur elemen dalam grid yang terdiri dari baris dan kolom.
  - Memudahkan pembuatan tata letak yang responsif dengan menggunakan unit ukuran yang fleksibel.
  - Menyediakan kontrol yang lebih baik atas posisi dan ukuran elemen dalam grid.
  - Contoh penggunaan Grid Layout:
    ```css
    .container {
      display: grid; /* Mengaktifkan Grid Layout */
      grid-template-columns: repeat(3, 1fr); /* Membuat 3 kolom dengan lebar yang sama */
      gap: 10px; /* Jarak antara elemen grid */
    }
    ```

---

## **Q5**: Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)!

**A**: Dalam mengerjakan tugas ini, saya banyak membaca tutorial sebelumnya karena materinya sangat mirip, saya juga membaca banyak dokumentasi dari internet dan bertanya ke LLM jika ada sesuatu yang lebih detail yang ingin saya ketahui. Secara singkat, step-by-step saya adalah:

1. Mengimplementasikan fungsi untuk menghapus dan mengedit product di `views.py` dan menambahkan routing URL di `urls.py`.
2. Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan TailwindCSS dan DaisyUI.
3. Setup Static Files di Django untuk menghubungkan file CSS eksternal & Assets.
4. Menjawab beberapa pertanyaan dalam `README.md`.
5. Melakukan commit ke GitHub dan deployment ke PWS.

---
## Checklist untuk tugas ini adalah sebagai berikut:

- [X] Implementasikan fungsi untuk menghapus dan mengedit **product**.

- [X] Kustomisasi desain pada *template* HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS *framework* (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
  - [X] Kustomisasi halaman **login**, **register**, tambah **product**, edit **product**, dan detail **product** semenarik mungkin.
  - [X] Kustomisasi halaman daftar **product** menjadi lebih menarik dan *responsive*. Kemudian, perhatikan kondisi berikut:
    - [X] Jika pada aplikasi belum ada **product** yang tersimpan, halaman daftar **product** akan menampilkan gambar dan pesan bahwa belum ada **product** yang terdaftar.
    - [X] Jika sudah ada **product** yang tersimpan, halaman daftar **product** akan menampilkan detail setiap **product** dengan menggunakan *card* (tidak boleh sama persis dengan desain pada Tutorial!).
    - [X] Untuk setiap *card product*, buatlah dua buah *button* untuk mengedit dan menghapus **product** pada *card* tersebut!
  - [X] Buatlah *navigation bar* (navbar) untuk fitur-fitur pada aplikasi yang *responsive* terhadap perbedaan ukuran *device*, khususnya *mobile* dan *desktop*.
- [X] Menjawab beberapa pertanyaan berikut pada `README.md` pada *root folder* (silakan modifikasi `README.md` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
  - [X] Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
  - [X] Mengapa *responsive design* menjadi konsep yang penting dalam pengembangan aplikasi *web*? Berikan contoh aplikasi yang sudah dan belum menerapkan *responsive design*, serta jelaskan mengapa!
  - [X] Jelaskan perbedaan antara *margin*, *border*, dan *padding*, serta cara untuk mengimplementasikan ketiga hal tersebut!
  - [X] Jelaskan konsep *flex box* dan *grid layout* beserta kegunaannya!
  - [X] Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)!

- [X] Melakukan `add-commit-push` ke GitHub.
</details>
<details><summary>Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django</summary>


---
## **Q1:** Apa itu `Django AuthenticationForm`? Jelaskan juga kelebihan dan kekurangannya.

**A:** `AuthenticationForm` adalah form bawaan Django yang digunakan untuk melakukan proses login pengguna.

Contoh penggunaan dasar `AuthenticationForm` dalam sebuah view:

```py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})
```

- Kelebihan dari `AuthenticationForm` adalah:
Kelebihan AuthenticationForm:

1. Siap pakai: Form ini bisa langsung digunakan tanpa banyak konfigurasi untuk login standar.

2. Aman secara default: Django sudah menangani hashing password dan validasi user sehingga risiko keamanan lebih kecil.

3. Terintegrasi dengan sistem Django: Mendukung session, middleware, dan decorator seperti @login_required.

4. Feedback otomatis: Memberikan notifikasi error jika username atau password salah.

- Kekurangan `AuthenticationForm`:

1. Kustomisasi terbatas: Untuk login dengan email, OTP, atau social login, perlu membuat form sendiri.

2. Tampilan minimal: Tidak ada styling bawaan, jadi perlu desain tambahan agar sesuai UI.

3. Fitur terbatas: Hanya untuk autentikasi dasar; fitur lanjutan seperti 2FA atau captcha harus ditambahkan manual.
  
---
## **Q2:** Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

**A:** Singkatnya, autentikasi adalah proses verifikasi identitas pengguna, memastikan bahwa mereka adalah siapa yang mereka klaim. Otorisasi adalah proses menentukan hak akses atau izin yang dimiliki pengguna setelah mereka terautentikasi.

Django mengimplementasikan kedua konsep ini melalui sistem `django.contrib.auth` yang menyediakan model User, grup, dan izin. Autentikasi dilakukan menggunakan form login seperti `AuthenticationForm` dan middleware yang memeriksa sesi pengguna, sementara otorisasi diatur melalui sistem izin, grup, serta decorator seperti `@login_required`, yang memungkinkan pengembang menentukan siapa yang dapat mengakses atau memodifikasi sumber daya tertentu berdasarkan peran atau izin pengguna.

---
## **Q3:** Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

**A:** Cookies disimpan di browser pengguna, sehingga tidak membebani server dan bisa bertahan antar-sesi jika diberi tanggal kedaluwarsa. Cookies juga mudah diakses dari sisi klien menggunakan JavaScript. Namun, ukurannya terbatas (sekitar 4KB per cookie) dan rentan terhadap manipulasi jika tidak dienkripsi atau di-sign. Selain itu, cookies dikirim ke server di setiap request, yang menambah overhead jaringan, dan bisa diblokir oleh pengguna atau browser karena kebijakan privasi.

Session menyimpan data di server, sehingga lebih aman dan tidak mudah dimanipulasi oleh pengguna. Session juga bisa menyimpan data yang lebih besar dibanding cookies. Kekurangannya, session membebani server karena setiap sesi memakan memori atau penyimpanan backend, biasanya tidak bertahan lama antar-browser kecuali diatur secara khusus, dan tetap bergantung pada session ID yang biasanya disimpan di cookie untuk tracking pengguna.

---
## **Q4:** Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

**A:** Penggunaan cookies tidak selalu aman karena disimpan di browser dan bisa diubah atau dicuri jika tidak dijaga dengan benar. Risiko utamanya adalah manipulasi cookie, pencurian session (session hijacking), dan serangan XSS yang dapat membaca cookie.

Django menangani hal ini dengan **signed cookies** untuk mendeteksi perubahan, **HttpOnly** agar cookie tidak bisa diakses JavaScript, serta opsi **Secure** agar hanya dikirim lewat HTTPS. Selain itu, Django menggunakan **token CSRF** untuk mencegah serangan Cross-Site Request Forgery, sehingga penggunaan cookie untuk autentikasi dan session relatif aman jika dijalankan di lingkungan HTTPS.


---

## **Q5:**  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**A:** Dalam mengerjakan tugas ini, saya banyak membaca tutorial sebelumnya karena materinya sangat mirip, saya juga membaca banyak dokumentasi dari internet dan bertanya ke LLM jika ada sesuatu yang lebih detail yang ingin saya ketahui. Secara singkat, step-by-step saya adalah:

1. Menambahkan `User` model dari `django.contrib.auth.models` untuk menghubungkan produk dengan pengguna.
2. Membuat fungsi registrasi, login, dan logout di `views.py` dengan menggunakan `UserCreationForm` dan `AuthenticationForm`.
3. Membuat template HTML untuk halaman registrasi, login, dan logout.
4. Menambahkan routing URL untuk fungsi-fungsi tersebut di `urls.py`.
5. Memodifikasi halaman utama untuk menampilkan informasi pengguna yang sedang login, seperti username dan last_login menggunakan cookies.
6. Membuat dua akun pengguna dan menambahkan tiga produk dummy untuk masing-masing akun melalui admin panel Django.
7. Melakukan styling pada halaman dengan TailwindCSS agar tampilan lebih menarik.
8. Melakukan commit ke GitHub dan deployment ke PWS.

---
 
- [X] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
- [X] Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
- [X] Menghubungkan model Product dengan User.
- [X] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
- [X] Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
  - [X] Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
  - [X] Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?
  - [X] Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
  - [X] Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
  - [X] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [X] Melakukan add-commit-push ke GitHub.

</details>

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
<img width="1375" height="937" alt="image" src="https://github.com/user-attachments/assets/09328b65-9fda-49ac-b810-c5f0acbefbb0" />
<img width="1436" height="942" alt="image" src="https://github.com/user-attachments/assets/8fe5672f-6cba-4b5f-ac7c-b25054934f61" />
<img width="1436" height="918" alt="image" src="https://github.com/user-attachments/assets/39be01e6-263f-4324-8e74-4f002997f590" />
<img width="1430" height="920" alt="image" src="https://github.com/user-attachments/assets/e8dbc5e4-19e9-46f1-9f27-fa392fc9011c" />

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
- [X] Buat **_screenshot_** dari hasil akses URL pada Postman dan tambahkan ke `README.md`.
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
