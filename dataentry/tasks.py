from auto_main.celery import app
import time 

@app.task
def celery_test_task():
    print(1)
    time.sleep(1)
    print(10)
  
    return "Task executed successfully from tasks.py!"