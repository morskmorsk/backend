# Generated by Django 4.2 on 2023-05-16 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_department_taxable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='device_created_date',
            new_name='deviceCreatedDate',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='device_created_by',
            new_name='deviceCreated_by',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='device_defects',
            new_name='deviceDefects',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='device_model',
            new_name='deviceModel',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='device_updated_date',
            new_name='deviceUpdatedDate',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='device_updated_by',
            new_name='deviceUpdated_by',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='purchase_date',
            new_name='purchaseDate',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='serial_number',
            new_name='serialNumber',
        ),
        migrations.RenameField(
            model_name='devicedefect',
            old_name='defect_description',
            new_name='defectDescription',
        ),
        migrations.RenameField(
            model_name='devicedefect',
            old_name='defect_name',
            new_name='defectName',
        ),
        migrations.RenameField(
            model_name='devicedefect',
            old_name='defect_solution',
            new_name='defectSolution',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='created_at',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_discount',
            new_name='orderDiscount',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_status',
            new_name='orderStatus',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_subtotal',
            new_name='orderSubtotal',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_tax',
            new_name='orderTax',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_total',
            new_name='orderTotal',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_type',
            new_name='orderType',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='updated_at',
            new_name='updatedAt',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='created_at',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='ms_url',
            new_name='msUrl',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='onhand_quantity',
            new_name='onHandQuantity',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_created_by',
            new_name='productCreatedBy',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_updated_by',
            new_name='productUpdatedBy',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sale_end',
            new_name='saleEnd',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sale_start',
            new_name='saleStart',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='updated_at',
            new_name='updatedAt',
        ),
    ]