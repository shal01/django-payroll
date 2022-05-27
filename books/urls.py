from django.urls import path
from books import views

urlpatterns=[
    path("add",views.BookCreateView.as_view(),name="book-add"),
    path("all",views.BookListView.as_view(),name="book-all"),
    path("edit/<int:id>",views.BookEditView.as_view(),name="book-edit"),
    path("details/<int:id>",views.BookDetailView.as_view(),name="detail"),
    path("remove/<int:id>",views.bookdelete,name="delete")

]