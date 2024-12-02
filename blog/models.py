from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    file = models.FileField(upload_to='books/', blank=True, null=True)  # FileField for uploading books
    book_name = models.CharField(max_length=255, blank=True, null=True)  # Field to store the book's file name

    def save(self, *args, **kwargs):
        if self.file:
            self.book_name = self.file.name.split('/')[-1] 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
