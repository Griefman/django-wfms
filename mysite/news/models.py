from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)  # Поле необязательно к заполнению
    created_at = models.DateTimeField(auto_now_add=True)  # содержит и дату и время в отл. от DateField
    # auto_now_add=True дата создается при добавлении новости и не меняется при редактировании
    # auto_now=True дата создается при добавлении новости и  меняется при редактировании
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')  # ImageField -только изображения, ImageField -любой формат
    # upload_to='photos' чтобы не хранить файлы в файле БД прописываем путь куда их складывать
    # %Y/%m/%d/ папки по времени
    # в upload_to= можно загрузить название метода, который определит загрузку файлов
    is_published = models.BooleanField(default=True)
    # Опубликовано или черновик
    # BooleanField() = None если не указано значение по умолчанию default=True, буде = 1
