from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('catalogue', '0002_usermeta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=60)),
            ],
            options={'db_table': 'types'},
        ),
    ]
