# Generated by Django 4.2.5 on 2023-09-25 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coachs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessioncoaching',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions_utilisateur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='demandecoaching',
            name='coach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coachs.coach'),
        ),
        migrations.AddField(
            model_name='demandecoaching',
            name='domaine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coachs.domaineexpertise'),
        ),
        migrations.AddField(
            model_name='demandecoaching',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coachdomaine',
            name='coach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coachs.coach'),
        ),
        migrations.AddField(
            model_name='coachdomaine',
            name='domaine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coachs.domaineexpertise'),
        ),
        migrations.AddField(
            model_name='coach',
            name='utilisateur',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
