from django.db import models
from django.urls import reverse_lazy, reverse
from .image_helpers import Thumbnail
from django.contrib.auth.models import User
from .standard_email import send_email

# Create your models here.
class Image(models.Model):
    caption = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'shop/images')

class Item(models.Model):
    name = models.CharField(max_length = 500)
    price = models.DecimalField(decimal_places = 2, max_digits = 10)
    main_image = models.ImageField(upload_to = 'shop/main_images', null = True)
    thumbnail = models.ImageField(upload_to = 'shop/thumbnails', null = True)
    images = models.ManyToManyField(Image)
    stars = models.IntegerField(default = 5)
    description = models.CharField(max_length = 2000)
    stock = models.IntegerField(default = 1)

    def get_absolute_url(self):
        return reverse('shop:item_detail', kwargs={'pk': self.pk})

    def get_success_url(self):
        return reverse('shop:item_list')

    def create_thumbnail(self):
        self.thumbnail = self.main_image
        self.save()
        image_generator = Thumbnail(source=self.thumbnail)
        modified_image_file = image_generator.generate()
        dest = open(self.thumbnail.path, 'wb')
        dest.write(modified_image_file.read())
        dest.close()

class Customer(models.Model):
    full_name = models.CharField(max_length = 100)
    email = models.EmailField()
    contact_number = models.CharField(max_length = 100)
    message = models.TextField()

    def get_success_url(self):
        return reverse('shop:item_list')

    def get_absolute_url(self):
        return reverse('shop:item_list')

    def send(self):
        contents = f"""
            <html>
            <body>
            <ul>
            <li>{self.full_name} </li>
            <li>{self.email} </li>
            <li>{self.contact_number} </li>
            <li>{self.message} </li>
            </ul>
            </body>
            </html>"""

        send_email(self.full_name, contents)
