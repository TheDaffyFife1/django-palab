# Generated by Django 4.2.11 on 2024-04-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palabras_admin', '0006_alter_areacodemx_code_alter_countrycode_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='palabracompartida',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='palabracompartida',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='palabracompartida',
            name='total_grupos',
            field=models.IntegerField(),
        ),
    ]
