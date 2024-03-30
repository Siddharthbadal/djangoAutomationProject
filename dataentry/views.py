from django.shortcuts import render, redirect
from .utils import get_all_custom_models, check_csv_errors
from uploads.models import Upload
from django.conf import settings
from django.core.management import call_command
from django.contrib import messages 
from .tasks import import_data_task, export_data_task


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
            check_csv_errors(file_path, model_name)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('import-data')

        # handle import data task 
        import_data_task.delay(file_path, model_name)

        # show messages 
        messages.success(request, "Upload is in process. You will be notified once completed!")
        

        return redirect('import-data')

    else:
        all_models = get_all_custom_models()
        # print(all_models)
        context = {
            'models':all_models
            }
        
    return render(request, 'dataentry/importdata.html', context)



def exportdata(request):
    if request.method=='POST':
        model_name=request.POST.get('model_name')
        # call the command for export data
        export_data_task.delay(model_name)
        messages.success(request, "Data Export is in Process. Please check your email!")
        return redirect('export_data')
        
    else:
        all_models = get_all_custom_models()
        context ={
              'models':all_models
        }
        
    return render(request, 'dataentry/exportdata.html', context)