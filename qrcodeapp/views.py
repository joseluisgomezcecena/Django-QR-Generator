from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time
from .models import QrCode, DjangoPartNumbers


# Create your views here.


def qr_generator(request):
    if request.method == 'POST':
        part = request.POST['part_number']
        order = request.POST['work_order']
        qty = request.POST['quantity']
        data = part + ',' + order + ',' + qty
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        media_root = str(settings.MEDIA_ROOT)
        img.save(media_root + '/' + img_name)

        # save data to database
        qr = QrCode(part_number=part, work_order=order, quantity=qty, img_url=img_name)
        qr.save()

        return render(request, 'index.html', {'img_name': img_name, 'parts': DjangoPartNumbers.objects.all()})

    return render(request, 'index.html', {'parts': DjangoPartNumbers.objects.all()})


def track(request, order):
    # search for the part number in the database
    # if found, return the image
    # if not found, return a message
    try:
        qr = QrCode.objects.get(work_order=order)
        return render(
            request,
            'track.html',
            {
                'img_name': qr.img_url,
                'parts': DjangoPartNumbers.objects.all(),
                'data': qr
            }
        )
    except QrCode.DoesNotExist:
        return render(
            request,
            'error.html',
            {
                'parts': DjangoPartNumbers.objects.all(),
                'message': 'No data was found.'
            }
        )

