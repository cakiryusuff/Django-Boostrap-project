# Django-Boostrap-project
django ve boostrap ile kullanıcı işlemleri olan site

Projeye önce templates klasörü altına attığım mainpage'in içinde olan olan uygulama1.html sayfasını oluşturarak başladım.
Ardından Visual Studio Code terminaline pip install Django yazarak djangoyu indirdim.
İndikten sonra terminale 'django-admin startproject characters' şeklinde projemi oluşturdum. Böylece gerekli dosyalar oluşturuldu.
Boostrap, js ve img dosyalarını static altına topladım. characters/settings.py de include ettim.
Sonra templates klasörümü eklemek için characters/settings.py TEMPLATES kısmına templates klasörümün konumunu yazdım.
Ardından ana sayfamı oluşturmak için 'manage.py startapp mainpage' şeklinde terminale yazdım. Oluşan Dosyalar arasına urls.py dosyası ekledim.
mainpage klasöründeki urls.py yi characters/urls.py kısmına include ettim.
Ana sayfaya uygulama1.html dosyasını yansıtmak için mainpage/views.py kısmından render ettim.
Ardından bilgileri sıralayacağım sayfa olan waifus u yaptım. Models kısmından karakterler için gerekli olan tabloları oluşturdum.
Karakter ekleme çıkarma işlemi içinde admin paneli oluşturdum.
Ardından kullanıcı işlemlerini yapacağım user kısmını oluşturdum login, register işlemleri için forumlar ayarladım.
user/views.py de login logout register fonksiyonları oluşturup işlevsellik kazandırdım.
