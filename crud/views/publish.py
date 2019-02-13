from django.shortcuts import render, redirect

from crud.models import Publish
from django.urls import reverse
from crud.forms.publish_forms import PublishForm


def add_publish(request):
    if request.method == 'POST':
        form = PublishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('crud:book'))

        context = {
            'form': form
        }
        return render(request, 'publish/add_publish.html', context=context)

    form = PublishForm()

    context = {
        'form': form
    }

    return render(request, 'publish/add_publish.html', context=context)


def edit_publish(request, id):
    publish_obj = Publish.objects.filter(nid=id).first()

    if request.method == 'POST':
        form = PublishForm(request.POST, instance=publish_obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('crud:book'))

        context = {
            'form': form
        }
        return render(request, 'publish/edit_publish.html', context=context)

    form = PublishForm(instance=publish_obj)  # 保留修改前的信息
    context = {
        'publish_obj': publish_obj,
        'form': form
    }
    return render(request, 'publish/edit_publish.html', context=context)


def delete_publish(request, id):
    Publish.objects.filter(nid=id).delete()
    return redirect(reverse('crud:book'))


def show_publish_book(request, id):
    publish_obj = Publish.objects.filter(nid=id).first()
    book_list = publish_obj.book_set.all()
    context = {
        'publish_obj': publish_obj,
        'book_list': book_list,
    }

    return render(request, 'publish/show_publish_book.html', context=context)
