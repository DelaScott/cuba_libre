from django.shortcuts import render
from .models import Guide


def guide_list(request):
    guides = Guide.objects.all()
    return render(request, 'guides/guide_list.html', {'guides': guides})


def guide_detail(request, pk):
    guide = Guide.objects.get(pk=pk)
    return render(request, 'guides/guide_detail.html', {'guide': guide})
