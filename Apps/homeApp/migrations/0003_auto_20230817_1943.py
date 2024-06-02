
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0002_auto_20230817_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafileupload',
            name='x_test_data',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datafileupload',
            name='y_test_data',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datafileupload',
            name='trained_model_data',
            field=models.BinaryField(),
        ),
    ]
