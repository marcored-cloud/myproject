from django.db import models


class SpedRow(models.Model):
    season = models.TextField(null=True, blank=True)
    agent = models.TextField(null=True, blank=True)
    order_customer = models.TextField(null=True, blank=True)
    customer_description = models.TextField(null=True, blank=True)

    destination_customer = models.TextField(null=True, blank=True)
    destination_id = models.TextField(null=True, blank=True)
    destination_description = models.TextField(null=True, blank=True)

    country = models.TextField(null=True, blank=True)
    country_description = models.TextField(null=True, blank=True)

    selling_type = models.TextField(null=True, blank=True)
    sub_seling_type = models.TextField(null=True, blank=True)
    line = models.TextField(null=True, blank=True)
    order_no = models.TextField(null=True, blank=True)
    po_number = models.TextField(null=True, blank=True)

    family_group = models.TextField(null=True, blank=True)
    family_group_description = models.TextField(null=True, blank=True)

    product_group = models.TextField(null=True, blank=True)
    product_group_description = models.TextField(null=True, blank=True)

    style = models.TextField(null=True, blank=True)
    material = models.TextField(null=True, blank=True)
    material_description = models.TextField(null=True, blank=True)
    measure = models.TextField(null=True, blank=True)
    color = models.TextField(null=True, blank=True)
    size = models.TextField(null=True, blank=True)
    drop_value = models.TextField(null=True, blank=True)

    variant_1 = models.TextField(null=True, blank=True)
    variant_2 = models.TextField(null=True, blank=True)
    label_1 = models.TextField(null=True, blank=True)
    label_2 = models.TextField(null=True, blank=True)
    cites = models.TextField(null=True, blank=True)
    luxury = models.TextField(null=True, blank=True)

    delivery_modality = models.TextField(null=True, blank=True)
    delivery_method = models.TextField(null=True, blank=True)
    delivery_group = models.TextField(null=True, blank=True)
    delivery_from = models.TextField(null=True, blank=True)
    delivery_to = models.TextField(null=True, blank=True)
    customer_priority = models.TextField(null=True, blank=True)
    currency = models.TextField(null=True, blank=True)

    order_qty = models.FloatField(null=True, blank=True)
    order_value = models.FloatField(null=True, blank=True)

    cancelled_qty = models.FloatField(null=True, blank=True)
    cancelled_qty_value = models.FloatField(null=True, blank=True)

    in_work_in_progress_qty = models.FloatField(null=True, blank=True)
    in_work_in_progress_value = models.FloatField(null=True, blank=True)

    stock_in_qty = models.FloatField(null=True, blank=True)
    stock_in_value = models.FloatField(null=True, blank=True)

    ready_qty = models.FloatField(null=True, blank=True)
    ready_value = models.FloatField(null=True, blank=True)

    picking_list_qty = models.FloatField(null=True, blank=True)
    picking_list_value = models.FloatField(null=True, blank=True)

    invoice_qty = models.FloatField(null=True, blank=True)
    invoice_value = models.FloatField(null=True, blank=True)

    ready_to_pick_100_qty = models.FloatField(null=True, blank=True)
    ready_to_pick_100_value = models.FloatField(null=True, blank=True)

    note = models.TextField(null=True, blank=True)