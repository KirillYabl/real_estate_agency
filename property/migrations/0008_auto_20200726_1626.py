# Generated by Django 2.2.4 on 2020-07-26 13:26

from django.db import migrations
import phonenumbers


def normalize_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(phonenumber):
            normalized_phonenumber = phonenumbers.format_number(phonenumber, phonenumbers.PhoneNumberFormat.E164)
            flat.owner_phone_pure = normalized_phonenumber
            flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_phone_pure = None
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0007_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumbers, move_backward),
    ]
