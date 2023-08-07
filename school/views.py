from django.shortcuts import render, get_object_or_404, redirect
from .models import about, team
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "home.html")

    # def home(request):
    #         return HttpResponse("<b>home</b>")

class about(View):
    def about(request):
        about_info = about.objects.first()  # Retrieve the first About instance (you can adjust this based on your requirements)
        return render(request, '.html', {'about_info': about_info})

class StaffListView(ListView):
    model = team
    template_name = 'staff/staff_list.html'
    context_object_name = 'staff_list'

class StaffDetailView(DetailView):
    model = team
    template_name = 'staff/staff_detail.html'
    context_object_name = 'staff'

class StaffCreateView(CreateView):
    model = team
    template_name = 'staff/staff_form.html'
    fields = '__all__'

class StaffUpdateView(UpdateView):
    model = team
    template_name = 'staff/staff_form.html'
    fields = '__all__'

class StaffDeleteView(DeleteView):
    model = team
    template_name = 'staff/staff_confirm_delete.html'
    success_url = reverse_lazy('staff_list')
