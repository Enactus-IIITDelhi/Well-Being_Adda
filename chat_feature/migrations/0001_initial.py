# Generated by Django 3.1.6 on 2021-04-18 04:56

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
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study', models.TextField(blank=True)),
                ('no', models.CharField(blank=True, max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chat_feature.contact')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('messages', models.ManyToManyField(blank=True, related_name='message', to='chat_feature.Message')),
                ('participants', models.ManyToManyField(blank=True, related_name='chats', to='chat_feature.Contact')),
            ],
        ),
    ]