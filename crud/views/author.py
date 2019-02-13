from django.shortcuts import render, redirect
from crud.models import Author, AuthorDetail
from django.urls import reverse
from crud.forms.author_forms import AuthorForm


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            age = request.POST.get('age')
            birthday = request.POST.get('birthday')
            telephone = request.POST.get('telephone')
            addr = request.POST.get('addr')

            author_detail_object = AuthorDetail.objects.create(
                birthday=birthday,
                telephone=telephone,
                addr=addr
            )
            Author.objects.create(
                name=name,
                age=age,
                authordetail=author_detail_object
            )

            return redirect(reverse('crud:book'))

        context = {'form': form}

        return render(request, 'author/add_author.html', context=context)

    form = AuthorForm()
    context = {
        'form': form
    }

    return render(request, 'author/add_author.html', context=context)


def edit_author(request, id):
    author = Author.objects.filter(nid=id).first()
    name = author.name
    age = author.age
    birthday = author.authordetail.birthday
    telephone = author.authordetail.telephone
    addr = author.authordetail.addr

    # 保留修改前的信息
    data = {
        'name': name,
        'age': age,
        'birthday': birthday,
        'telephone': telephone,
        'addr': addr
    }
    if request.method == 'POST':
        form = AuthorForm(request.POST, data)
        if form.is_valid():
            name = request.POST.get('name')
            age = request.POST.get('age')
            birthday = request.POST.get('birthday')
            telephone = request.POST.get('telephone')
            addr = request.POST.get('addr')

            AuthorDetail.objects.filter(nid=id).update(
                birthday=birthday,
                telephone=telephone,
                addr=addr
            )
            Author.objects.filter(nid=id).update(
                name=name,
                age=age,
            )
            return redirect(reverse('crud:book'))
        context = {'form': form}
        return render(request, 'author/edit_author.html', context=context)

    form = AuthorForm(data)
    context = {
        'form': form,
    }
    return render(request, 'author/edit_author.html', context=context)


def delete_author(request, id):
    Author.objects.filter(pk=id).delete()
    AuthorDetail.objects.filter(pk=id).delete()

    return redirect(reverse('crud:book'))


def show_author_book(request, id):
    author_obj = Author.objects.filter(nid=id).first()
    book_list = author_obj.book_set.all()
    author_name = author_obj.name

    context = {
        'book_list': book_list,
        'author_name': author_name
    }

    return render(request, 'author/show_author_book.html', context=context)
