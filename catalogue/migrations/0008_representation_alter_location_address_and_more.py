
import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.DateTimeField()),
            ],
            options={
                'db_table': 'representations',
            },
        ),
        migrations.AddConstraint(
            model_name='location',
            constraint=models.UniqueConstraint(fields=('slug', 'website'), name='unique_slug_website'),
        ),
        migrations.AddField(
            model_name='representation',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='representations', to='catalogue.location'),
        ),
        migrations.AddField(
            model_name='representation',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='representations', to='catalogue.show'),
        ),
    ]

