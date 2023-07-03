#trying to bypass the use of management command 
from django.core.management import call_command
from django.db import migrations
from django.db.migrations.recorder import MigrationRecorder
def my_migration(apps, schema_editor):
    # Do some schema modifications here
    try:
        MigrationRecorder.get(name__contains = 'apply_data')
    except:
        # Call the management command
        call_command('generate_city')

class Migration(migrations.Migration):
    dependencies = [
        ('iranian_cities', '0005_auto_20221004_0004'),
    ]

    operations = [
        migrations.RunPython(my_migration),
    ]
