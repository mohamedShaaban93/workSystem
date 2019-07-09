# Generated by Django 2.2 on 2019-07-08 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_workhours'),
    ]

    operations = [
        migrations.CreateModel(
            name='SwapRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SwapRequestOwners', to='administration.Employee')),
                ('shift', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='administration.EmployeeStatus')),
                ('users', models.ManyToManyField(related_name='SwapRequests', to='administration.Employee')),
            ],
        ),
    ]