# Generated by Django 5.1.4 on 2024-12-15 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_commentary_post_alter_commentary_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentary',
            name='comments_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentary', to='blog.post'),
        ),
    ]
