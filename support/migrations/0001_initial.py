# Generated by Django 4.0.1 on 2022-04-19 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('NR', '일반'), ('AC', '계정'), ('Et', '기타')], max_length=2)),
                ('title', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=128, verbose_name='작성자 이메일')),
                ('is_eamil', models.IntegerField(blank=True, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('is_phone', models.IntegerField(blank=True, null=True)),
                ('content', models.TextField()),
                ('created_by_id', models.CharField(max_length=100, verbose_name='질문 작성자')),
                ('updated_by_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='답변 작성자')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
