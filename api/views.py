from django.http import JsonResponse
import string
import random

def index(request):
    return JsonResponse({"string": generate_random_string()})

def generate_random_string(N = 64):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
