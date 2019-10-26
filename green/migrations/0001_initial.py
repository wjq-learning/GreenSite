# Generated by Django 2.2.4 on 2019-10-26 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControlData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relay_num', models.CharField(blank=True, max_length=32, null=True)),
                ('relay_name', models.CharField(blank=True, max_length=32, null=True)),
                ('belongto_type', models.IntegerField(blank=True, null=True)),
                ('belongto_id', models.IntegerField(blank=True, null=True)),
                ('relay_type', models.IntegerField(blank=True, null=True)),
                ('relay_value', models.FloatField(blank=True, null=True)),
                ('collect_time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'control_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_num', models.CharField(blank=True, max_length=32, null=True)),
                ('object_id', models.IntegerField(blank=True, null=True)),
                ('object_type', models.IntegerField(blank=True, null=True)),
                ('sensor_type_id', models.CharField(blank=True, max_length=11, null=True)),
                ('sensor_value', models.FloatField(blank=True, null=True)),
                ('collect_time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'data_record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FlowerShelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('room_id', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('created_time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'flower_shelf',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(blank=True, max_length=32, null=True)),
                ('mac', models.CharField(blank=True, max_length=12, null=True)),
                ('ip', models.CharField(blank=True, max_length=16, null=True)),
                ('index', models.IntegerField(blank=True, null=True)),
                ('created_time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'new_device',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OperateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(blank=True, max_length=16, null=True)),
                ('room_id', models.IntegerField(blank=True, null=True)),
                ('device_num', models.CharField(blank=True, max_length=16, null=True)),
                ('operation', models.IntegerField(blank=True, null=True)),
                ('start_time', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=64, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'operate_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuanSheng',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=16, null=True)),
                ('parent', models.IntegerField(blank=True, null=True)),
                ('area_num', models.CharField(blank=True, max_length=8, null=True)),
                ('level', models.CharField(blank=True, max_length=1, null=True)),
                ('level_nam', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'quan_sheng',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuanShi',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=16, null=True)),
                ('parent', models.IntegerField(blank=True, null=True)),
                ('area_num', models.CharField(blank=True, max_length=8, null=True)),
                ('level', models.CharField(blank=True, max_length=1, null=True)),
                ('level_nam', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'quan_shi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuanXian',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=16, null=True)),
                ('parent', models.IntegerField(blank=True, null=True)),
                ('area_num', models.CharField(blank=True, max_length=8, null=True)),
                ('level', models.CharField(blank=True, max_length=1, null=True)),
                ('level_nam', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'quan_xian',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelayInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relay_num', models.CharField(blank=True, max_length=32, null=True)),
                ('relay_name', models.CharField(blank=True, max_length=32, null=True)),
                ('device_mac', models.CharField(blank=True, max_length=32, null=True)),
                ('belongto_type', models.IntegerField(blank=True, null=True)),
                ('belongto_id', models.IntegerField(blank=True, null=True)),
                ('is_online', models.IntegerField(blank=True, null=True)),
                ('status', models.FloatField(blank=True, null=True)),
                ('refresh_time', models.IntegerField(blank=True, null=True)),
                ('created_time', models.IntegerField(blank=True, null=True)),
                ('device_type', models.IntegerField(blank=True, null=True)),
                ('relay_type_id', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'relay_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RoomInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_num', models.CharField(blank=True, max_length=16, null=True)),
                ('room_name', models.CharField(blank=True, max_length=16, null=True)),
                ('city', models.CharField(blank=True, max_length=32, null=True)),
                ('area', models.CharField(blank=True, max_length=32, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('created_time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'room_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('content', models.TextField()),
                ('comment', models.CharField(blank=True, max_length=64, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('created_time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rules',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SensorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_num', models.CharField(blank=True, max_length=32, null=True)),
                ('device_mac', models.CharField(blank=True, max_length=32, null=True)),
                ('device_index', models.IntegerField(blank=True, null=True)),
                ('sensor_type_id', models.IntegerField(blank=True, null=True)),
                ('belongto_type', models.IntegerField(blank=True, null=True)),
                ('belongto_id', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('created_time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sensor_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SensorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_type', models.CharField(blank=True, max_length=16, null=True)),
                ('sensor_type_unit', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 'sensor_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SystemDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(blank=True, null=True)),
                ('key', models.CharField(blank=True, max_length=32, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('created_time', models.IntegerField()),
            ],
            options={
                'db_table': 'system_dict',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('auth_key', models.CharField(max_length=32)),
                ('password_hash', models.CharField(max_length=255)),
                ('password_reset_token', models.CharField(blank=True, max_length=255, null=True)),
                ('access_token', models.CharField(blank=True, max_length=64, null=True)),
                ('email', models.CharField(max_length=255)),
                ('status', models.SmallIntegerField()),
                ('created_at', models.IntegerField()),
                ('updated_at', models.IntegerField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
