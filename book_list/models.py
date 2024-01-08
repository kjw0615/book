from django.db import models

# Create your models here.

class BookList(models.Model):
    bcode = models.IntegerField(db_column='BCODE', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=200)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    year_of_publication = models.CharField(db_column='YEAR-OF-PUBLICATION', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    publisher = models.ForeignKey('BookStore', models.DO_NOTHING, db_column='PUBLISHER', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'book_list'


class BookStore(models.Model):
    bscode = models.IntegerField(db_column='BSCODE', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=15, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=50, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'book_store'