from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Match, Choice

# Create your views here.


"""def html_bar(first_data, second_data):
    width = 300
    height = 50
    first_ratio = first_data / (first_data + second_data)
    second_ratio = second_data / (first_data + second_data)
    first_rac = [(width*first_ratio-width)/2, width*first_ratio, height] #[x좌표, 너비, 높이]
    second_rac = [(width*second_ratio-width)/2, width*second_ratio, height]
    return [first_rac, second_rac]"""

def index(request):
    latest_match_list = Match.objects.order_by("pub_date")

    context = {
        "latest_match_list": latest_match_list,
        "match_range": range(len(latest_match_list))
    }
    return render(request, "Dobak/index.html", context)

def select(request):
    latest_match_list = Match.objects.order_by("pub_date")[:5]
    context = {
        "latest_match_list": latest_match_list,
    }
    return render(request, "Dobak/select.html", context)

def detail(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    return render(request, "Dobak/detail.html", {"match": match})


def results(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    return render(request, "Dobak/results.html", {"match":match})

def vote(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    try:
        selected_choice = match.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,"Dobak/detail.html",
            {
              "match":match,
              "error_message": "다시 고르시오",
            },
            )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("Dobak:results", args=(match_id,)))
