from celery import shared_task
import time

# This is a sample task. DELETE it when starting new project!

def mul_ten(number):
    time.sleep(5)
    return number * 10

# This is a sample task. DELETE it when starting new project!

@shared_task
def multiply_by_ten(number):
    num = mul_ten(number)
    return num
