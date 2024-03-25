from django.shortcuts import render, redirect
from .utils import get_all_custom_models
from uploads.models import Upload
from django.conf import settings
from django.core.management import call_command
from django.contrib import messages 


def importdata(request):
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')
        model_name = request.POST.get('model_name')

        print("file path: ", file_path)
        print("Model name: ", model_name)

        # store file in upload model
        upload = Upload.objects.create(file=file_path,model_name=model_name)

        # full relative file path
        relative_path = str(upload.file.url)
        print(relative_path)

        # full path
        base_url = str(settings.BASE_DIR)       
        print(base_url)

        file_path = f"{base_url}{relative_path}"
        print(file_path)
        try:
            # call_commands calls the custom comnads in views 
            call_command("importdata", file_path, model_name)
            messages.success(request, f"Data Imported to {model_name} table successfully!")
        except Exception as e:
            messages.error(request, str(e))
        return redirect('import-data')

    else:
        all_models = get_all_custom_models()
        # print(all_models)
        context = {
            'models':all_models
            }
        
    return render(request, 'dataentry/importdata.html', context)

