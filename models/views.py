from django.http import HttpResponse
from django.shortcuts import render
from models.models import Model


# def brand_detail(request, id):
#     if Model.objects.count() < id:
#         return HttpResponse("error. PAGE NOT FOUND")
#
#     data = {
#         "model": Model.objects.get(id=id)
#     }
#     return render(request, 'detail.html', context=data)
#
