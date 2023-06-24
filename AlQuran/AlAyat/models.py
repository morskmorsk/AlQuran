from django.db import models

# Create your models here.


class Ayah(models.Model):
    surah = models.IntegerField()
    ayah = models.IntegerField()
    text = models.TextField()
    translation = models.TextField()
    transliteration = models.TextField()
    audio = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ayahs"
        ordering = ["surah", "ayah"]

    def __str__(self):
        return f"{self.surah}:{self.ayah}"

    def get_absolute_url(self):
        return f"/{self.surah}/{self.ayah}/"


# class Surah(models.Model):
#     surah = models.IntegerField()
#     name = models.CharField(max_length=255)
#     english_name = models.CharField(max_length=255)
#     english_name_translation = models.CharField(max_length=255)
#     revelation_type = models.CharField(max_length=255)
#     ayahs = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = "surahs"
#         ordering = ["surah"]

#     def __str__(self):
#         return f"{self.surah} - {self.name}"

#     def get_absolute_url(self):
#         return f"/{self.surah}/"


# class Juz(models.Model):
#     juz = models.IntegerField()
#     surah = models.IntegerField()
#     ayah = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = "juzs"
#         ordering = ["juz"]

#     def __str__(self):
#         return f"{self.juz} - {self.surah}:{self.ayah}"

#     def get_absolute_url(self):
#         return f"/juz/{self.juz}/"


# class Page(models.Model):
#     page = models.IntegerField()
#     surah = models.IntegerField()
#     ayah = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = "pages"
#         ordering = ["page"]

#     def __str__(self):
#         return f"{self.page} - {self.surah}:{self.ayah}"

#     def get_absolute_url(self):
#         return f"/page/{self.page}/"


# class HizbQuarter(models.Model):
#     hizb = models.IntegerField()
#     surah = models.IntegerField()
#     ayah = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = "hizb_quarters"
#         ordering = ["hizb"]

#     def __str__(self):
#         return f"{self.hizb} - {self.surah}:{self.ayah}"

#     def get_absolute_url(self):
#         return f"/hizb/{self.hizb}/"
