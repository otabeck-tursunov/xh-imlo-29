from django.shortcuts import render
from .models import *


def index_view(reqeust):
    correct = None
    incorrects = None
    message = None

    word = reqeust.GET.get('word')
    if word is not None:

        if 'x' not in word.lower() and 'h' not in word.lower():
            message = "So'z tarkibida Xx yoki Hh mavjud emas!"
        else:
            corrects = Correct.objects.filter(word__contains=word)
            if corrects.exists():
                correct = corrects.first()
                incorrects = correct.incorrect_set.all()
            else:
                incorrects = Incorrect.objects.filter(word__contains=word)
                if incorrects.exists():
                    correct = incorrects.first().correct
                    incorrects = correct.incorrect_set.all()
                else:
                    message = "Bunday so'z mavjud emas!"

    context = {
        'correct': correct,
        'incorrects': incorrects,
        'message': message
    }
    return render(reqeust, 'index.html', context)
