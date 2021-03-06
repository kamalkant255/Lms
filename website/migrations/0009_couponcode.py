# Generated by Django 3.2.8 on 2021-11-18 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('discount', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupons', to='website.course')),
            ],
        ),
    ]
