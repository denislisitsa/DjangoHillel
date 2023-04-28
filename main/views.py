from django.http import HttpResponse
from .models import Teacher

def teachers_list(request):
    teachers = Teacher.objects.all()
    teachers_str = '\n'.join([str(teacher) for teacher in teachers])
    return HttpResponse(teachers_str)