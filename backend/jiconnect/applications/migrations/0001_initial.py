# Generated by Django 3.2.8 on 2021-10-16 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('middlename', models.CharField(blank=True, max_length=200, null=True)),
                ('lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('id_type', models.CharField(blank=True, max_length=200, null=True)),
                ('id_number', models.CharField(blank=True, max_length=200, null=True)),
                ('pin', models.CharField(blank=True, max_length=200, null=True)),
                ('county', models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilifi'), ('Tana River', 'Tana River'), ('Tana River', 'Tana River'), ('Taita Taveta', 'Taita Taveta')], max_length=200, null=True)),
                ('po_box', models.CharField(blank=True, max_length=200, null=True)),
                ('town', models.CharField(blank=True, max_length=200, null=True)),
                ('constituency', models.CharField(choices=[('Changamwe', 'Changamwe'), ('Jomvu', 'Jomvu'), ('Kisauni', 'Kisauni'), ('Nyali', 'Nyali'), ('Likoni', 'Likoni'), ('Mvita', 'Mvita'), ('Msambweni', 'Msambweni'), ('Lunga Lunga', 'Lunga Lunga'), ('Matuga', 'Matuga'), ('Kinango', 'Kinango'), ('Kilifi North', 'Kilifi North'), ('Kilifi South', 'Kilifi South'), ('Kaloleni', 'Kaloleni'), ('Rabai', 'Rabai'), ('Ganze', 'Ganze'), ('Malindi', 'Malindi'), ('Magarini', 'Magarini'), ('Garsen', 'Garsen'), ('Galole', 'Galole'), ('Bura', 'Bura'), ('Lamu East', 'Lamu East'), ('Lamu West', 'Lamu West'), ('Taveta', 'Taveta'), ('Wundanyi', 'Wundanyi'), ('Mwatate', 'Mwatate'), ('Voi', 'Voi')], max_length=200, null=True)),
                ('ward', models.CharField(choices=[('CHAANI', 'CHAANI'), ('MIRITINI', 'MIRITINI'), ('AIRPORT', 'AIRPORT'), ('PORT REITZ', 'PORT REITZ'), ('KIPEVU', 'KIPEVU'), ('JOMVU KUU', 'JOMVU KUU'), ('MAGONGO', 'MAGONGO'), ('MIKINDANI', 'MIKINDANI'), ('SHANZU', 'SHANZU'), ('MWAKIRUNGE', 'MWAKIRUNGE'), ('MJAMBERE', 'MJAMBERE'), ('MAGOGONI', 'MAGOGONI'), ('JUNDA', 'JUNDA'), ('MTOPANGA', 'MTOPANGA'), ('BAMBURI', 'BAMBURI'), ('MKOMANI', 'MKOMANI'), ('KONGOWEA', 'KONGOWEA'), ('KADZANDANI', 'KADZANDANI'), ("ZIWA LA NG'OMBE", "ZIWA LA NG'OMBE"), ('FRERE TOWN', 'FRERE TOWN'), ('MTONGWE', 'MTONGWE'), ('TIMBWANI', 'TIMBWANI'), ('BOFU', 'BOFU'), ('LIKONI', 'LIKONI'), ('SHIKA ADABU', 'SHIKA ADABU'), ('MJI WA KALE/ MAKADARA', 'MJI WA KALE/ MAKADARA'), ('TUDOR', 'TUDOR'), ('TONONOKA', 'TONONOKA'), ('SHIMANZI/ GANJONI', 'SHIMANZI/ GANJONI'), ('MAJENGO', 'MAJENGO'), ('RAMISI', 'RAMISI'), ('GOMBATO BONGWE', 'GOMBATO BONGWE'), ('UKUNDA', 'UKUNDA'), ('KINONDO', 'KINONDO'), ('PONGWE KIDIMU/KIGWEDE', 'PONGWE KIDIMU/KIGWEDE'), ('VANGA', 'VANGA'), ('MWERENI', 'MWERENI'), ('DZOMBO', 'DZOMBO'), ('KUBO SOUTH', 'KUBO SOUTH'), ('MKONGANI', 'MKONGANI'), ('TSIMBA GOLINI', 'TSIMBA GOLINI'), ('TIWI', 'TIWI'), ('WAA', 'WAA'), ('MACKINON ROAD', 'MACKINON ROAD'), ('NDAVAYA', 'NDAVAYA'), ('PUMA', 'PUMA'), ('KINANGO', 'KINANGO'), ('KASEMENI', 'KASEMENI'), ('MWAVUMBO', 'MWAVUMBO'), ('CHENGONI/SAMBURU', 'CHENGONI/SAMBURU'), ('MATSANGONI', 'MATSANGONI'), ('MNARANI', 'MNARANI'), ('SOKONI', 'SOKONI'), ('TEZO', 'TEZO'), ('KIBARANI', 'KIBARANI'), ('WATAMU', 'WATAMU'), ('DABASO', 'DABASO'), ('JUNJU', 'JUNJU'), ('SHIMO LA TEWA', 'SHIMO LA TEWA'), ('MTEPENI', 'MTEPENI'), ('CHASIMBA', 'CHASIMBA'), ('MWARAKAYA', 'MWARAKAYA'), ('KAYAFUNGO', 'KAYAFUNGO'), ('MARIAKANI', 'MARIAKANI'), ('MWANAMWINGA', 'MWANAMWINGA'), ('KALOLENI', 'KALOLENI'), ('JIBANA/KAMBE/RIBE', 'JIBANA/KAMBE/RIBE'), ('MAZERASRABAI/KISURUTINI', 'MAZERASRABAI/KISURUTINI'), ('MWAWESA', 'MWAWESA'), ('RURUMA', 'RURUMA'), ('SOKOKE', 'SOKOKE'), ('BAMBA', 'BAMBA'), ('JARIBUNI', 'JARIBUNI'), ('DUNGICHA/ GANZE', 'DUNGICHA/ GANZE'), ('JILORE', 'JILORE'), ('GANDA', 'GANDA'), ('KAKUYUNI', 'KAKUYUNI'), ('SHELLA', 'SHELLA'), ('MALINDI TOWN', 'MALINDI TOWN'), ('ADU', 'ADU'), ('MARAFA', 'MARAFA'), ('SABAKI', 'SABAKI'), ('MAGARINI', 'MAGARINI'), ('GONGONI', 'GONGONI'), ('GARASHI', 'GARASHI'), ('GARSEN NORTH', 'GARSEN NORTH'), ('GARSEN WEST', 'GARSEN WEST'), ('GARSEN CENTRAL', 'GARSEN CENTRAL'), ('KIPINI EAST', 'KIPINI EAST'), ('GARSEN SOUTH', 'GARSEN SOUTH'), ('KIPINI WEST', 'KIPINI WEST'), ('CHEWANI', 'CHEWANI'), ('KINAKOMBA', 'KINAKOMBA'), ('MAKINDUNI', 'MAKINDUNI'), ('WAYU', 'WAYU'), ('BANGALE', 'BANGALE'), ('CHEWELE', 'CHEWELE'), ('HIRIMAN', 'HIRIMAN'), ('MADOGO', 'MADOGO'), ('SALA', 'SALA'), ('KIUNGA', 'KIUNGA'), ('BASUBA', 'BASUBA'), ('FAZA', 'FAZA'), ('MKOMANI', 'MKOMANI'), ('SHELLA', 'SHELLA'), ('WITU', 'WITU'), ('HINDI', 'HINDI'), ('HONGWE', 'HONGWE'), ('BAHARI', 'BAHARI'), ('MKUNUMBI', 'MKUNUMBI'), ('MATA', 'MATA'), ('MAHOO', 'MAHOO'), ('MBOGHONI', 'MBOGHONI'), ('CHALA', 'CHALA'), ('BOMANI', 'BOMANI'), ('MWANDA/MGANGE', 'MWANDA/MGANGE'), ('KISHUSHE/WUMINGU', 'KISHUSHE/WUMINGU'), ('WERUGHA', 'WERUGHA'), ('WUNDANYI/MBALE', 'WUNDANYI/MBALE'), ('CHAWIA', 'CHAWIA'), ('BURA', 'BURA'), ('WUSI/KISHAMBA', 'WUSI/KISHAMBA'), ('RONGE', 'RONGE'), ('MWATATE', 'MWATATE'), ('NGOLIA', 'NGOLIA'), ('KASIGAU', 'KASIGAU'), ('MARUNGU', 'MARUNGU'), ('SAGALA', 'SAGALA'), ('MBOLOLO', 'MBOLOLO'), ('KALOLENI', 'KALOLENI')], max_length=200, null=True)),
                ('lr_number', models.CharField(blank=True, max_length=200, null=True)),
                ('estate_village', models.CharField(blank=True, max_length=200, null=True)),
                ('area_code', models.CharField(blank=True, max_length=200, null=True)),
                ('ccp', models.CharField(blank=True, max_length=200, null=True)),
                ('voltage', models.CharField(blank=True, max_length=200, null=True)),
                ('connect_type', models.CharField(blank=True, max_length=200, null=True)),
                ('amd', models.CharField(blank=True, max_length=200, null=True)),
                ('id_document', models.FileField(blank=True, null=True, upload_to='')),
                ('pin_certificate', models.FileField(blank=True, null=True, upload_to='')),
                ('title_deed', models.FileField(blank=True, null=True, upload_to='')),
                ('wiring_certificate', models.FileField(blank=True, null=True, upload_to='')),
                ('site_plan', models.FileField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
