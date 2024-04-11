## Data Automation ToolKit
 
__Automated data import and export__ by using django custom commands, celery and redis. 
User can import and export data from CSV file for a existing database model with email notification, send bulk emails with attachments. 
Also applied Error handling and Messages display with user authentication.

Used celery and redis with django for faster data processing. 


## Goal
To be able to perform various operations faster and without interrpution on user interface and command line.


## Custome Commands For Command Line Interface
Import Data
    - python manage.py importdata file_path model_name

Export Data
    - python manage.py exportdata model_name

Delete Data
    - python manage.py deletedata model_name
    
    
## Tech
    - Django
    - Celery  
    - Redis
    - Docker
    - Bootstrap


    

   ![homePage](https://github.com/Siddharthbadal/djangoAutomationProject/assets/55015090/a0b1950b-6ab3-4c61-b079-79a147af6bc4)

    
   ![dataImportwithCelery](https://github.com/Siddharthbadal/djangoAutomationProject/assets/55015090/7b462e37-6cce-49ca-adff-efad21bba004)
