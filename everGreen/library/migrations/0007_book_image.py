# Generated by Django 4.2.1 on 2023-05-24 21:21

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_librarycard_user_id_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/ndongchrist/Desktop/Akashicodes/Open-Source/LibraryApp/everGreen/media'), upload_to='images/', verbose_name=''),
        ),
    ]