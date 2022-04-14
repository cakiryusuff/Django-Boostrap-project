from django.db import models
#TABLO EKLEMEK İÇİN OLAN BÖLÜM MODELS KISMI
# Create your models here.
#MODEL İÇİN HER YAPILAN DEĞİŞİKLİKTEN SONRA MAKEMİGRATİONS KOMUTU KULLANILMASI GEREKİYOR
class Waifus(models.Model): #https://docs.djangoproject.com/en/4.0/ref/models/fields/ burdan nelerin kullanıldığına bakabilirsin
    name = models.CharField(max_length=100,verbose_name="Karakter adı") #name varchar olarak tanımlandı
    description = models.TextField(verbose_name="Karakter açıklaması")
    image = models.CharField(max_length=50 ,verbose_name="Karakter Resmi")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Eklenme Tarihi") #anlık olarak güncel zamanı girme

    def get_image_path(self):
        return  "/img/"+self.image