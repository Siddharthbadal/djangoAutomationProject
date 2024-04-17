from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ImageCompressionForm
from PIL import Image 
import io 


def compress_image(request):
    user = request.user
    if request.method == 'POST':
        form = ImageCompressionForm(request.POST, request.FILES)
        if form.is_valid():
            original_image = form.cleaned_data['original_image']
            quality = form.cleaned_data['quality']

            new_compressed_image= form.save(commit=False)
            new_compressed_image.user = user

            # performing compression 
            image = Image.open(original_image)
            output_format= image.format

            # create virtual memory to store binary data of image
            buffer = io.BytesIO()       
            # print("buffer", buffer.getvalue())   
            image.save(buffer, format=output_format, quality=quality)
            # print("buffer", buffer.getvalue())

            # cursor positing back to zero after processing
            buffer.seek(0)
             
            new_compressed_image.compressed_image.save(
                f"compressed_{original_image}", buffer
            )            
            
            #  download the image by converting the image from binary to image

            response = HttpResponse(buffer.getvalue(), content_type=f"image/{output_format.lower()}" )
            response['Content-Disposition'] = f"attachment; filename=compressed_{original_image}"

            
            # messages.success(request, 'Image Compressed Successfully!')
            return response
            # return redirect('compress_image')
         
    else:

        form = ImageCompressionForm()
        context = {
            'form': form
        }
        return render(request, 'image_compression/compress.html', context)
