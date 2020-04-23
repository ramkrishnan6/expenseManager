# Generated by Django 3.0.5 on 2020-04-22 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200422_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('Automobile', 'Automobile'), ('Bank Transfer', 'Bank Transfer'), ('Cash Withdrawal', 'Cash Withdrawal'), ('Education', 'Education'), ('Entertainment', 'Entertainment'), ('Fine', 'Fine'), ('Food', 'Food'), ('Health Care', 'Health Care'), ('Paytm', 'PayTM'), ('Recharge', 'Recharge'), ('Shopping', 'Shopping'), ('Travel', 'Travel'), ('Unknown', 'Unknown'), ('UPI', 'UPI')], default='Unknown', max_length=30),
        ),
    ]