from ammapp.models import Group
from ammapp.models import Student
from django.http import HttpResponse
from django.template import Context, loader

#Методы выдачи данных
#В зависимости от id происходит выборка данных
def index(request):
    records = Group.objects.order_by("level", "course")
    template = loader.get_template('ammapp/index.html')
    context = Context({'records': records})
    return HttpResponse(template.render(context))

def group_detail(request, id):
    record = Group.objects.get(pk=id)
    st_list = record.student.order_by("name")
    template = loader.get_template('ammapp/group_detail.html')
    context = Context({'record': record, 'students': st_list})
    return HttpResponse(template.render(context))

def profile(request, id):
    record = Student.objects.get(pk=id)
    template = loader.get_template('ammapp/profile.html')
    context = Context({'record': record})
    return HttpResponse(template.render(context))
