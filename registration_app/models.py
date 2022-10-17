from django.db import models

# Create your models here.


class LoyalUsers(models.Model):
    user_name = models.CharField(db_column='User_name', max_length=50)  # Field name made lowercase.
    user_surname = models.CharField(max_length=50)
    user_id = models.IntegerField(primary_key=True)
    user_phone = models.IntegerField(unique=True)
    user_email = models.CharField(unique=True, max_length=150)
    user_password = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    class Meta:
        managed = False
        db_table = 'loyal_users'