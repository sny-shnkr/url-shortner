from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import UrlModel
import json
import uuid


def index_view(request):
    if request.method == "POST":
        url = request.POST["link"]
        slug = str(uuid.uuid4())[:8]
        url_obj = UrlModel(url=url, slug=slug)
        url_obj.save()

        shorten_link = f"{str(request.build_absolute_uri())}u/{slug}"

        return render(
            request,
            "shortner/shorten_link.html",
            {"shorten_link": shorten_link, "slug": slug},
        )
    return render(request, "shortner/index.html", {})


def redirect_to_url(request, slug):
    url_obj = UrlModel.objects.get(slug=slug)
    return redirect(url_obj.url)
