from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import SpedRow
import csv
from io import StringIO


def to_float(value):
    if value is None:
        return None

    value = str(value).strip()

    if value == "":
        return None

    value = value.replace(",", ".")

    try:
        return float(value)
    except ValueError:
        return None


@login_required
def upload_csv(request):
    if request.method == 'POST':
        file = request.FILES.get('csv_file')

        if file:
            content = file.read().decode('utf-8')

            csv_file = StringIO(content)
            reader = csv.reader(csv_file, delimiter=';')

            righe = list(reader)

            # cancella dati precedenti
            SpedRow.objects.all().delete()

            for riga in righe[1:]:
                SpedRow.objects.create(
                    season=riga[0],
                    agent=riga[1],
                    order_customer=riga[2],
                    customer_description=riga[3],

                    destination_customer=riga[4],
                    destination_id=riga[5],
                    destination_description=riga[6],

                    country=riga[7],
                    country_description=riga[8],

                    selling_type=riga[9],
                    sub_seling_type=riga[10],
                    line=riga[11],
                    order_no=riga[12],
                    po_number=riga[13],

                    family_group=riga[14],
                    family_group_description=riga[15],

                    product_group=riga[16],
                    product_group_description=riga[17],

                    style=riga[18],
                    material=riga[19],
                    material_description=riga[20],
                    measure=riga[21],
                    color=riga[22],
                    size=riga[23],
                    drop_value=riga[24],

                    variant_1=riga[25],
                    variant_2=riga[26],
                    label_1=riga[27],
                    label_2=riga[28],
                    cites=riga[29],
                    luxury=riga[30],

                    delivery_modality=riga[31],
                    delivery_method=riga[32],
                    delivery_group=riga[33],
                    delivery_from=riga[34],
                    delivery_to=riga[35],
                    customer_priority=riga[36],
                    currency=riga[37],

                    order_qty=to_float(riga[38]),
                    order_value=to_float(riga[39]),

                    cancelled_qty=to_float(riga[40]),
                    cancelled_qty_value=to_float(riga[41]),

                    in_work_in_progress_qty=to_float(riga[42]),
                    in_work_in_progress_value=to_float(riga[43]),

                    stock_in_qty=to_float(riga[44]),
                    stock_in_value=to_float(riga[45]),

                    ready_qty=to_float(riga[46]),
                    ready_value=to_float(riga[47]),

                    picking_list_qty=to_float(riga[48]),
                    picking_list_value=to_float(riga[49]),

                    invoice_qty=to_float(riga[50]),
                    invoice_value=to_float(riga[51]),

                    ready_to_pick_100_qty=to_float(riga[52]),
                    ready_to_pick_100_value=to_float(riga[53]),

                    note=riga[54] if len(riga) > 54 else None
                )

            return HttpResponse("TUTTE LE COLONNE SALVATE")

    rows = SpedRow.objects.all().order_by('-id')[:50]

    return render(request, 'importer/upload_csv.html', {
        'rows': rows
    })