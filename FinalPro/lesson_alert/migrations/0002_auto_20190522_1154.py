# Generated by Django 2.1.7 on 2019-05-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_alert', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Time',
        ),
        migrations.AddField(
            model_name='category',
            name='Lesson',
            field=models.CharField(choices=[('第一節', '8:10-9:00'), ('第二節', '9:10-10:00'), ('第三節', '10:10-11:00'), ('第四節', '11:10-12:00'), ('第五節', '13:10-14:00'), ('第六節', '14:10-15:00'), ('第七節', '15:10-16:00'), ('第八節', '16:10-17:00'), ('第九節', '17:10-18:00'), ('第十節', '18:10-19:00'), ('第十一節', '19:10-20:00'), ('第十二節', '20:10-21:00')], default='', max_length=20, verbose_name='第幾節'),
        ),
        migrations.AddField(
            model_name='category',
            name='Week',
            field=models.CharField(choices=[('星期一', '星期一'), ('星期二', '星期二'), ('星期三', '星期三'), ('星期四', '星期四'), ('星期五', '星期五'), ('星期六', '星期六'), ('星期日', '星期日')], default='', max_length=20, verbose_name='星期幾'),
        ),
        migrations.AlterField(
            model_name='category',
            name='Name',
            field=models.CharField(default='', max_length=255, verbose_name='課程名稱'),
        ),
    ]
