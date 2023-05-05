from django.db import models
from accounts.models import CustomUser as Profile
from datetime import datetime
from decimal import Decimal


class Department(models.Model):
    name = models.CharField(max_length=200)
    taxable = models.CharField(max_length=3, default='yes')

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Department object ({})>'.format(self.id)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Location object ({})>'.format(self.id)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'


class DeviceDefect(models.Model):
    defect_name = models.CharField(max_length=50, unique=True)
    defect_description = models.TextField(
        max_length=500, blank=True, null=True)
    defect_solution = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.defect_name

    def __repr__(self) -> str:
        return self.defect_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Device Defect'
        verbose_name_plural = 'Device Defects'


class Device(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='device_owner')
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='device_department')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    device_model = models.CharField(max_length=200, blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    carrier = models.CharField(max_length=200, blank=True, null=True)
    imei = models.CharField(max_length=20, blank=True, null=True)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    seller = models.ForeignKey(Profile,
                               on_delete=models.CASCADE,
                               related_name='device_seller',
                               blank=True,
                               null=True
                               )
    compatibility = models.CharField(
        max_length=25, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    device_created_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='device_created_by',
        null=True,
        blank=True
    )
    device_updated_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='device_updated_by',
        null=True,
        blank=True
    )
    purchase_date = models.DateField(default=datetime.now)
    device_created_date = models.DateTimeField(auto_now_add=True)
    device_updated_date = models.DateTimeField(auto_now_add=True,)
    info = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    report = models.FileField(
        upload_to='static/reports/store/device_reports/',
        null=True,
        blank=True
    )
    device_defects = models.ManyToManyField(
        DeviceDefect,
        related_name='device_defects',
        help_text='Select all that apply',
        default=None
    )
    photo = models.ImageField(
        upload_to='static/images/store/device_photos/', null=True, blank=True)
    status = models.CharField(
        max_length=25, blank=True, null=True)
    grade = models.CharField(
        max_length=25, blank=True, null=True)

    def __str__(self):
        return self.owner.username + '\'s ' + self.device_model

    def __repr__(self):
        return '<Device object ({})>'.format(self.id)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'


class WorkOrderCart(models.Model):
    customer = models.OneToOneField(Profile, on_delete=models.CASCADE,
                                    related_name='repair_customer')

    def __str__(self):
        return f"{self.customer.username}'s Shopping Cart"

    def get_sales_tax(self):
        tax_rate = 0.09  # 9% sales tax rate
        taxable_items = WorkOrderCartItem.objects.filter(
            cart=self, product__department__taxable=True)
        total_taxable = sum(
            item.price * item.quantity for item in taxable_items)
        return total_taxable * Decimal(tax_rate)


class WorkOrderCartItem(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    cart = models.ForeignKey(WorkOrderCart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.device.name} x {self.quantity}"


class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                 related_name='workorder_customer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Order"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.device.name} x {self.quantity}"
