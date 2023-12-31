# Generated by Django 4.2.5 on 2023-09-25 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biographie', models.TextField()),
                ('tarif_horaire', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponibilite', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoachDomaine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DemandeCoaching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_soumission', models.DateField(auto_now_add=True)),
                ('date_souhaitee', models.DateField()),
                ('heure_souhaitee', models.TimeField()),
                ('message', models.TextField()),
                ('statut', models.CharField(choices=[('En Attente', 'En Attente'), ('Acceptée', 'Acceptée'), ('Refusée', 'Refusée')], max_length=20)),
                ('date_reponse', models.DateField(blank=True, null=True)),
                ('commentaire_coach', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DomaineExpertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_domaine', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SessionCoaching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_session', models.DateField()),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('statut', models.CharField(choices=[('Planifiée', 'Planifiée'), ('Terminée', 'Terminée'), ('Annulée', 'Annulée')], max_length=20)),
                ('note_utilisateur', models.PositiveIntegerField(blank=True, null=True)),
                ('commentaire_utilisateur', models.TextField(blank=True, null=True)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions_coach', to='coachs.coach')),
            ],
        ),
    ]
