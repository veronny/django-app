# Generated by Django 4.1.1 on 2022-09-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("GestanteApp", "0005_gestante_captacion_gestante_meta_captacion_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="gestante",
            old_name="meta_violencia",
            new_name="meta_int_violencia",
        ),
        migrations.AddField(
            model_name="gestante",
            name="int_violencia",
            field=models.IntegerField(
                blank=True, max_length=100, null=True, verbose_name="int_violencia"
            ),
        ),
        migrations.AddField(
            model_name="gestante",
            name="por_int_violencia",
            field=models.IntegerField(
                blank=True, max_length=100, null=True, verbose_name="por_int_violencia"
            ),
        ),
    ]
