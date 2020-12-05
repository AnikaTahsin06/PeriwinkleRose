from django.db import models

class Slider(models.Model):
    sliderImage = models.ImageField(upload_to='slider/')

    @staticmethod
    def get_all_sliders():
        return Slider.objects.all()