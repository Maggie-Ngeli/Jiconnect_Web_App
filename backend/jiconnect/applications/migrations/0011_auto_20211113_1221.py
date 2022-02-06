# Generated by Django 3.2.8 on 2021-11-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0010_auto_20211112_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='constituency',
            field=models.CharField(choices=[('Changamwe', 'Changamwe'), ('Jomvu', 'Jomvu'), ('Kisauni', 'Kisauni'), ('Nyali', 'Nyali'), ('Likoni', 'Likoni'), ('Mvita', 'Mvita'), ('Msambweni', 'Msambweni'), ('Lunga Lunga', 'Lunga Lunga'), ('Matuga', 'Matuga'), ('Kinango', 'Kinango'), ('Kilifi North', 'Kilifi North'), ('Kilifi South', 'Kilifi South'), ('Kaloleni', 'Kaloleni'), ('Rabai', 'Rabai'), ('Ganze', 'Ganze'), ('Malindi', 'Malindi'), ('Magarini', 'Magarini'), ('Garsen', 'Garsen'), ('Galole', 'Galole'), ('Bura', 'Bura'), ('Lamu East', 'Lamu East'), ('Lamu West', 'Lamu West'), ('Taveta', 'Taveta'), ('Wundanyi', 'Wundanyi'), ('Mwatate', 'Mwatate'), ('Voi', 'Voi')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='county',
            field=models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilifi'), ('Tana River', 'Tana River'), ('Tana River', 'Tana River'), ('Taita Taveta', 'Taita Taveta')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id_document',
            field=models.ImageField(blank=True, default='media/noid.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pin_certificate',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='site_plan',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='title_deed',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='wiring_certificate',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]