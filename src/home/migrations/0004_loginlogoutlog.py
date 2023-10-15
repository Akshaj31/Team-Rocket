# Generated by Django 4.2.6 on 2023-10-15 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_employee_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginLogoutLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=10)),
                ('event_time', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.CharField(max_length=55)),
                ('user_agent', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auditdb.login_logout_log',
            },
        ),
    ]
