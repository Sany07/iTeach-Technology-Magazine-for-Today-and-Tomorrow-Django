# Generated by Django 3.1.4 on 2020-12-10 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_news_instructor'),
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesettings',
            options={'verbose_name': 'Site Setting', 'verbose_name_plural': 'Site Settings'},
        ),
        migrations.CreateModel(
            name='HomePageSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hot_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hot_news', to='news.news')),
                ('post_catalog_five', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_catalog_five', to='news.category')),
                ('post_catalog_four', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_catalog_four', to='news.category')),
                ('post_catalog_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_catalog_one', to='news.category')),
                ('post_catalog_three', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_catalog_three', to='news.category')),
                ('post_catalog_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_catalog_two', to='news.category')),
            ],
            options={
                'verbose_name': 'Home Page Setting',
                'verbose_name_plural': 'Home Page Settings',
                'db_table': 'homepagesettings',
            },
        ),
    ]
