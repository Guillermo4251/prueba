# Generated by Django 4.0.5 on 2022-07-02 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='compra',
            fields=[
                ('Idcompra', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=30)),
                ('fechaEnvio', models.DateField()),
                ('fechaEstimada', models.DateField()),
                ('fechaEntrega', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('IdProducto', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('NombreProducto', models.CharField(max_length=30)),
                ('Valor', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('descuento', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='sub',
            fields=[
                ('idSub', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='venta',
            fields=[
                ('IdVenta', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('idCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.compra')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]