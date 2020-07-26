# Generated by Django 3.0.7 on 2020-07-26 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bangladesh_geocode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VictimApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No name', max_length=50)),
                ('incident_type', models.CharField(choices=[('rape', 'Rape'), ('physical_torture', 'Attacking Physically'), ('metal_torture', 'Mental Torture')], default='metal_torture', max_length=20)),
                ('incident_date', models.DateField()),
                ('place', models.CharField(max_length=50)),
                ('address_5', models.CharField(default='Bangladesh', max_length=20)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('unspecified', 'Unspecified')], default='female', max_length=15)),
                ('age_victim', models.PositiveSmallIntegerField(null=True)),
                ('age_criminal', models.PositiveSmallIntegerField(null=True)),
                ('relation_with_criminal', models.CharField(choices=[('friend', 'Friend(s)'), ('unknown', 'Unknown'), ('relative', 'Relative(s)'), ('in-laws', 'In laws')], default='unknown', max_length=20)),
                ('witness', models.BooleanField(default=False)),
                ('witness_name', models.CharField(default='No name', max_length=20)),
                ('informed_authority', models.BooleanField(default=False)),
                ('authority_name', models.CharField(choices=[('police', 'Police'), ('UNO', 'UNO'), ('chairman', 'Chairman'), ('member', 'Member')], default='None', max_length=20)),
                ('description', models.CharField(default='', max_length=300)),
                ('current_status_of_victim', models.CharField(default='', max_length=30)),
                ('address_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangladesh_geocode.Unions')),
                ('address_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangladesh_geocode.Upzilas')),
                ('address_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangladesh_geocode.Districts')),
                ('address_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangladesh_geocode.Divisions')),
            ],
        ),
    ]
