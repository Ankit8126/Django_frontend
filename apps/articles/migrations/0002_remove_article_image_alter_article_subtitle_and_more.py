# Generated by Django 5.1.3 on 2024-12-18 08:35

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.AlterField(
            model_name='article',
            name='subtitle',
            field=models.TextField(blank=True, default='No subtitle'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.TextField(blank=True, default='No subtitle'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='articles/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('order', models.PositiveIntegerField(default=0, help_text='Order in which the images appear.')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_images', to='articles.article')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='articles_images', to='articles.articleimage'),
        ),
    ]
