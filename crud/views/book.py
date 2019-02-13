import json
from django.shortcuts import render, redirect, HttpResponse

from crud.models import Book
from django.urls import reverse
from crud.forms.book_forms import BookForm


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('crud:book'))
        context = {
            'form': form
        }
        return render(request, 'book/add_book.html', context=context)

    form = BookForm()

    context = {
        'form': form,
    }
    return render(request, 'book/add_book.html', context=context)


def edit_book(request, id):
    book_obj = Book.objects.filter(nid=id).first()
    ret = {'status': None, 'message': None}
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book_obj)
        if form.is_valid():
            form.save()
            ret['status'] = 'true'
            return HttpResponse(json.dumps(ret))
        else:
            ret['message'] = form.errors.as_text()
            return HttpResponse(json.dumps(ret))

    form = BookForm(instance=book_obj)

    context = {
        'form': form
    }
    return render(request, 'book/edit_book.html', context=context)


def delete_book(request, id):
    Book.objects.filter(nid=id).delete()

    return redirect(reverse('crud:book'))
