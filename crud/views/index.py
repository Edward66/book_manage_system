from django.shortcuts import render
from crud.models import Publish, Author, Book
from django.core.paginator import Paginator, EmptyPage


def index(request):
    book_list = Book.get_all()
    publish_list = Publish.get_all()
    author_list = Author.get_all()

    book_paginator = Paginator(book_list, 5)

    current_page_num = int(request.GET.get('page', 1))

    if book_paginator.num_pages > 11:
        if current_page_num - 5 < 1:
            page_range = range(1, 11)
        elif current_page_num + 5 > book_paginator.num_pages:
            page_range = range(book_paginator.num_pages - 10, book_paginator.num_pages + 1)
        else:
            page_range = range(current_page_num - 5, current_page_num + 5)
    else:
        page_range = book_paginator.page_range

    try:
        current_page = book_paginator.page(current_page_num)
    except EmptyPage as e:
        current_page = book_paginator.page(1)

    context = {
        'book_list': book_list,
        'publish_list': publish_list,
        'author_list': author_list,
        'page_range': page_range,
        'current_page': current_page,
        'current_page_num': current_page_num,
    }
    return render(request, 'index.html', context=context)
