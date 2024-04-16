from django.shortcuts import render
from .forms import ImageCompressionForm


def compress_image(request):
    form = ImageCompressionForm()
    context = {
        'form': form
    }
    return render(request, 'image_compression/compress.html', context)
