#GJ from django.shortcuts import render

# Create your views here.

#GJ from django.http import HttpResponse
#GJ def index(request):
#GJ    return HttpResponse("안녕하세요. Django에 오신 것을 환영합니다.")

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .models import Answer

#from .forms import QuestionForm
#from django.http import HttpResponseNotAllowed

from .forms import QuestionForm, AnswerForm

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

from django.contrib import messages
