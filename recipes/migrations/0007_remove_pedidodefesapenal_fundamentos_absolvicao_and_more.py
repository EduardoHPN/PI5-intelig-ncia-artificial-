# Generated by Django 5.1.4 on 2025-04-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_fundamentoabsolvicao_pedidodefesapenal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidodefesapenal',
            name='fundamentos_absolvicao',
        ),
        migrations.AddField(
            model_name='pedidodefesapenal',
            name='fundamentos_absolvicao',
            field=models.CharField(blank=True, choices=[('inexistencia_fato', 'Inexistência do fato'), ('fato_atipico', 'Fato atípico'), ('excludente_ilicitude', 'Excludente de ilicitude'), ('excludente_culpabilidade', 'Excludente de culpabilidade'), ('ausencia_autoria', 'Ausência de indícios suficientes de autoria'), ('outro', 'Outro (especificar)')], max_length=255, null=True),
        ),
    ]

