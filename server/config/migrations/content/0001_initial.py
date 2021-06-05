# Generated by Django 3.2.4 on 2021-06-05 09:14

import apps.content.models.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('bitrate', models.PositiveIntegerField(verbose_name='Битрейт')),
            ],
            options={
                'verbose_name': 'Аудио',
                'verbose_name_plural': 'Аудио',
            },
        ),
        migrations.CreateModel(
            name='PageTexts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.page')),
            ],
            options={
                'verbose_name': 'Текст на Страницу',
                'verbose_name_plural': 'Тексты на Странице',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='PageVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.page')),
            ],
            options={
                'verbose_name': 'Видео на Страницу',
                'verbose_name_plural': 'Видео на Странице',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('video_file', models.FileField(upload_to=apps.content.models.utils.get_upload_file_path, verbose_name='Ссылка на Видео')),
                ('subtitles_file', models.FileField(upload_to=apps.content.models.utils.get_upload_file_path, verbose_name='Ссылка на файл Субтитров')),
                ('pages', models.ManyToManyField(related_name='videos', through='content.PageVideos', to='page.Page', verbose_name='Страницы')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('pages', models.ManyToManyField(related_name='texts', through='content.PageTexts', to='page.Page', verbose_name='Страницы')),
            ],
            options={
                'verbose_name': 'Текст',
                'verbose_name_plural': 'Тексты',
            },
        ),
        migrations.AddField(
            model_name='pagevideos',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.video'),
        ),
        migrations.AddField(
            model_name='pagetexts',
            name='text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.text'),
        ),
        migrations.CreateModel(
            name='PageAudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.audio')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.page')),
            ],
            options={
                'verbose_name': 'Аудио на Страницу',
                'verbose_name_plural': 'Аудио на Странице',
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='audio',
            name='pages',
            field=models.ManyToManyField(related_name='audios', through='content.PageAudios', to='page.Page', verbose_name='Страницы'),
        ),
    ]
