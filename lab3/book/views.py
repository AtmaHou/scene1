from django.http import HttpResponseRedirect
from django.template import Context
from django.shortcuts import render_to_response
from models import Book, Author
import datetime

def current_time(request):
    now = datetime.datetime.now()
    c = Context({'time': now})
    return render_to_response("time.html", c)

def add_book(request):
    if "Title_get" in request.POST:
        try:
            post = request.POST
            au = Author.objects.get(Name=post["AuthorID_get"])
            new_book = Book(
                ISBN=post["ISBN_get"],
                Title=post["Title_get"],
                AuthorID=au,
                Publisher=post["Publisher_get"],
                PublishDate=post["PublishDate_get"],
                Price=post["Price_get"],
            )
            new_book.save()
            author_list = Author.objects.all()
            c = Context({"save": True, "author_list": author_list})
        except:
            author_list = Author.objects.all()
            c = Context({"save": False, "author_list": author_list})
        return render_to_response("add_book.html", c)
    else:
        author_list = Author.objects.all()
        c = Context({"save": False, "author_list": author_list})
        return render_to_response("add_book.html", c)


def add_author(request):
    if "Name_get" in request.POST:
        post = request.POST
        new_author = Author(
            AuthorID=post["AuthorID_get"],
            Name=post["Name_get"],
            Age=post["Age_get"],
            Country=post["Country_get"],
        )
        new_author.save()
        return HttpResponseRedirect('/add_book/')
    else:
        return render_to_response("add_author.html")


def homepage(request):
    if "search" in request.POST:
        author = Author.objects.filter(Name=request.POST["search"])
        book_list = author[0].book_set.all()
        return render_to_response("search_result.html", {"book_list": book_list, "author": author[0]})
    if "search" in request.GET:
        author = Author.objects.filter(Name=request.GET["search"])
        book_list = author[0].book_set.all()
        return render_to_response("search_result.html", {"book_list": book_list, "author": author[0]})
    if 'title' in request.GET:
        t = request.GET["title"]
        book = Book.objects.filter(Title=t)
        c = Context({"a": book[0], "author": book[0].AuthorID})
        return render_to_response("book_detail.html", c)
    if 'delete' in request.GET:
        I = request.GET["delete"]
        book = Book.objects.get(ISBN=I)
        auth = book.AuthorID
        book.delete()
        book_list = auth.book_set.all()
        return render_to_response("search_result.html", {"book_list": book_list, "author": auth})
    return render_to_response("home.html")


def update(request):
    I = request.GET["title"]
    book = Book.objects.filter(ISBN=I)
    b = book[0]
    author_list = Author.objects.all()
    if "Title_get" in request.POST:
        # try:
        post = request.POST
        au = Author.objects.get(Name=post["AuthorID_get"])
        b.Title = post["Title_get"]
        b.AuthorID = au
        b.Publisher = post["Publisher_get"]
        b.PublishDate = post["PublishDate_get"]
        b.Price = post["Price_get"]
        b.save()
        c = Context({"save": True, "author_list": author_list, "a": book[0]})

        # except:
        #     c = Context({"save": False, "author_list": author_list, "a": book[0]})
    else:
        c = Context({"save": False, "author_list": author_list, "a": book[0]})
    return render_to_response("update.html", c)