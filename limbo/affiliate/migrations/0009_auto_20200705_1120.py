# Generated by Django 3.0.6 on 2020-07-05 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0008_auto_20200704_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=600, null=True)),
                ('price', models.IntegerField(max_length=10, null=True)),
                ('categories', models.CharField(default='', max_length=60)),
                ('SubCategories', models.CharField(default='', max_length=60)),
                ('slug', models.CharField(max_length=130)),
                ('date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='image/mobile')),
            ],
        ),
        migrations.DeleteModel(
            name='realme',
        ),
        migrations.DeleteModel(
            name='samsung',
        ),
        migrations.DeleteModel(
            name='xaiomi',
        ),
    ]