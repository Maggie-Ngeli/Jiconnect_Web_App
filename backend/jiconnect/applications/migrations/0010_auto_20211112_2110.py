# Generated by Django 3.2.8 on 2021-11-12 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0009_alter_customer_id_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='constituency',
            field=models.CharField(choices=[('Changamwe', 'Changamwe'), ('Jomvu', 'Jomvu'), ('Kisauni', 'Kisauni'), ('Nyali', 'Nyali'), ('Likoni', 'Likoni'), ('Mvita', 'Mvita'), ('Msambweni', 'Msambweni'), ('Lunga Lunga', 'Lunga Lunga'), ('Matuga', 'Matuga'), ('Kinango', 'Kinango'), ('Kilifi North', 'Kilifi North'), ('Kilifi South', 'Kilifi South'), ('Kaloleni', 'Kaloleni'), ('Rabai', 'Rabai'), ('Ganze', 'Ganze'), ('Malindi', 'Malindi'), ('Magarini', 'Magarini'), ('Garsen', 'Garsen'), ('Galole', 'Galole'), ('Bura', 'Bura'), ('Lamu East', 'Lamu East'), ('Lamu West', 'Lamu West'), ('Taveta', 'Taveta'), ('Wundanyi', 'Wundanyi'), ('Mwatate', 'Mwatate'), ('Voi', 'Voi')], default='- - - - - - - - - - - -', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='county',
            field=models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilifi'), ('Tana River', 'Tana River'), ('Tana River', 'Tana River'), ('Taita Taveta', 'Taita Taveta')], default='- - - - - - - - - - - -', max_length=200, null=True),
        ),
    ]
