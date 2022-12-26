from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Record
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class LockedView(LoginRequiredMixin):
    login_url = "accounts/login"


class RecordListView(LockedView, ListView):
    model = Record
    queryset = Record.objects.all().order_by("-date_created")


class RecordDetailView(LockedView, DetailView):
    model = Record


class RecordCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Record
    fields = ["title", "content", "image", "author"]
    success_url = reverse_lazy("record-list")
    success_message = "Новая запись успешно создана!"


class RecordUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Record
    fields = ["title", "content", "image", "author"]
    success_message = "Запись успешно обновлена!"

    def get_success_url(self):
        return reverse_lazy(
            "record-detail",
            kwargs={"pk": self.object.id}
        )


class RecordDeleteView(LockedView, SuccessMessageMixin, DeleteView):
    model = Record
    success_url = reverse_lazy("record-list")
    success_message = "Запись успешно удалена!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

