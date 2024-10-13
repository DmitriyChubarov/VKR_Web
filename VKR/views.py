from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ImageUploadForm
from django.views.generic import FormView
from .utils import bi_inter
from PIL import Image
import numpy as np
from django.http import HttpResponse
import io

class HomePageView(TemplateView):
    template_name = 'home.html'

class Bi_line(FormView):
    template_name = 'bi_line.html'
    form_class = ImageUploadForm

    def form_valid(self, form):
        size = 3
        image = form.cleaned_data['image']
        image = Image.open(image)
        np_new = bi_inter(image, size)
        img_new = Image.fromarray(np_new)

        byte_io = io.BytesIO()
        img_new.save(byte_io, format='PNG')
        byte_io.seek(0)

        response = HttpResponse(byte_io, content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="image.png"'

        return response
