# Generated by Django 4.1.1 on 2022-09-27 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "GestanteApp",
            "0003_gestante_atendido_gestante_control_gestante_examen_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="gestante",
            name="paquete",
            field=models.IntegerField(
                blank=True, max_length=100, null=True, verbose_name="paquete"
            ),
        ),
        migrations.AddField(
            model_name="gestante",
            name="por_atendido",
            field=models.IntegerField(
                blank=True, max_length=100, null=True, verbose_name="por_atendido"
            ),
        ),
        migrations.AddField(
            model_name="gestante",
            name="por_control",
            field=models.IntegerField(
                blank=True, max_length=100, null=True, verbose_name="por_control"
            ),
        ),
        migrations.AddField(
            model_name="gestante",
            name="por_examen",
            field=models.IntegerField(
                blank=True, max_length=100, null=True, verbose_name="por_examen"
            ),
        ),
        migrations.AddField(
            model_name="gestante",
            name="por_paquete",
            field=models.IntegerField(
                blank=True, max_length=100, null=True, verbose_name="por_paquete"
            ),
        ),
        migrations.AddField(
            model_name="gestante",
            name="por_sulfato",
            field=models.IntegerField(
                blank=True, max_length=100, null=True, verbose_name="por_sulfato"
            ),
        ),
        migrations.AddField(
            model_name="gestante",
            name="por_tamizaje",
            field=models.IntegerField(
                blank=True, max_length=100, null=True, verbose_name="por_tamizaje"
            ),
        ),
        migrations.AddField(
            model_name="gestante",
            name="por_violencia",
            field=models.IntegerField(
                blank=True, max_length=100, null=True, verbose_name="por_violencia"
            ),
        ),
    ]
