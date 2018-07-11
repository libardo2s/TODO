from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView

from .forms import FormAdd, FormUpdate

from .models import Todo


class IndexView(ListView):
    template_name = "index.html"
    model = Todo
    context_object_name = "todo_list"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form_add'] = FormAdd()
        context['form_update'] = FormUpdate()
        return context


def add(request):
    if request.method == 'POST':
        data_form = FormAdd(request.POST)
        if data_form.is_valid():
            task = data_form.cleaned_data['task']
            description = data_form.cleaned_data['description']

            Todo.objects.create(task=task, description=description)

    return HttpResponseRedirect('/')


def get(request, id=None):
    if request.method == 'GET':
        if id is not None:
            todo = Todo.objects.get(id=id)
            json_data = {
                'id': todo.id,
                'task': todo.task,
                'description': todo.description
            }
            return JsonResponse(json_data)


def update(request):
    if request.method == 'POST':
        id = request.POST['id']
        task = request.POST['task']
        description = request.POST['description']

        todo = Todo.objects.get(id=id)
        todo.task = task
        todo.description = description
        todo.save()

    return HttpResponseRedirect('/')


def delete(request, id=None):
    if request.method == 'GET':
        if id is not None:
            todo = Todo.objects.get(id=id)
            todo.delete()
    return HttpResponseRedirect('/')