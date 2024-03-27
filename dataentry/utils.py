from django.apps import apps 
from django.core.management.base import CommandError
import csv 
from django.db import DataError


def get_all_custom_models():
    """
        Helper function to get all models from apps
    """
    default_models = ['ContentType','Session','LogEntry','Group','Permission']
    custom_models = []
    for model in apps.get_models():
        if model.__name__ not in default_models:
            custom_models.append(model.__name__)
            # print(model.__name__)
    return custom_models


def check_csv_errors(file_path, model_name):  
        """
            Helper function to check errors in csv with models for both command line and frontend.
            Takes two arguments file_path, model_name   
        """      
        
        model = None 
    # search for the model accros all apps
        # compare csv file header with the model names for errors
        for app_config in apps.get_app_configs():
            # search model in app
            try:
                model = apps.get_model(app_config.label, model_name)
                break # model found 
            except LookupError:
                continue # model not found. search in the next app
        
        if not model:
            raise CommandError(f"{model_name} not found!")
        
        # get the model fileds name
        model_fields = [field.name for field in model._meta.fields if field.name != 'id']
        # model fields also has ID. needs to exclude 
        print(model_fields)
        
        try:             
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)   
                csv_header = reader.fieldnames
                
                if csv_header != model_fields:
                        raise DataError(f"CSV headers must match with {model_name} table fields!")
        except Exception as e:
             raise e

        return model 
