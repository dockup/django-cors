from django.http import JsonResponse
import string
import random

def index(request):
    return JsonResponse({"quote": get_random_quote()})

def get_random_quote():
    quotes = [
        ["I have no special talents. I am only passionately curious.", "Albert Einstein"],
        ["Stay Hungry. Stay Foolish.", "Steve Jobs"],
        ["Good Artists Copy, Great Artists Steal.", "Pablo Picasso"],
        ["Argue with idiots, and you become an idiot.", "Paul Graham"],
        ["Be yourself; everyone else is already taken.", "Oscar Wilde"],
        ["Simplicity is the ultimate sophistication.", "Leonardo Da Vinci"]
    ]
    return random.choice(quotes)
