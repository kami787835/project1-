from django.db import models
class Slider(models.Model):
    title = models.CharField('Заголовок', max_length=255, null=True, blank=True)
    subtitle = models.CharField('Подзаголовок', max_length=255, null=True, blank=True)
    img = models.ImageField('Изображение', null=True, blank=True)
    link = models.URLField('Ссылка', null=True, blank=True)
    is_active = models.BooleanField('Активность', default=False)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

class Item(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else 'Unnamed Item'

class AboutUs(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else 'Unnamed About Us'

class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class ClientReview(models.Model):
    author = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.author}" if self.author else "Anonymous Review"
