# Generated by Django 2.2 on 2019-05-03 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_code', models.CharField(max_length=255)),
                ('c_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('emp_fname', models.CharField(max_length=255)),
                ('emp_lname', models.CharField(max_length=255)),
                ('emp_phone', models.CharField(max_length=10)),
                ('emp_email', models.EmailField(max_length=255)),
                ('emp_address', models.TextField()),
                ('type', models.CharField(choices=[('01', 'weavers'), ('02', 'supervisors'), ('03', 'engineer')], default='01', max_length=3)),
                ('emp_salary', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('mac_id', models.AutoField(primary_key=True, serialize=False)),
                ('mac_name', models.CharField(max_length=255)),
                ('mac_sum', models.CharField(max_length=255)),
                ('mac_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Machine_Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.IntegerField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Machine', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('state', models.CharField(choices=[('Pending', 'Pending'), ('Inprogress', 'Inprogress'), ('Succeed', 'Succeed')], default='Pending', max_length=50)),
                ('desc', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.Employee')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.Machine')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('part_desc', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
                ('minimum_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='reports.Employee')),
                ('eng_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance_Machine_Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('machine_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Machine_Part')),
                ('maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Maintenance')),
            ],
        ),
        migrations.AddField(
            model_name='machine_part',
            name='maintenance',
            field=models.ManyToManyField(through='reports.Maintenance_Machine_Part', to='reports.Maintenance'),
        ),
        migrations.AddField(
            model_name='machine_part',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Part', unique=True),
        ),
        migrations.CreateModel(
            name='Category_Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Category')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Part')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='machine_part',
            unique_together={('part', 'machine')},
        ),
    ]
