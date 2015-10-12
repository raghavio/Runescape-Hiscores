from django.core.exceptions import FieldError
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Skills
from utils import skill_names


def show_skill(request, skill):
    skill = str(skill)
    skill_exp = skill + '_exp'
    try:
        all_results = Skills.objects.order_by('-%s' % skill_exp).values("user_name", skill, skill_exp)
    except FieldError:
        raise Http404("404: Skill could not be found.")
    paginator = Paginator(all_results, 26)
    page = request.GET.get('page')

    try:
        results_page = paginator.page(page)
    except PageNotAnInteger:
        # If variable page is not an integer, deliver first page.
        results_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        results_page = paginator.page(paginator.num_pages)

    start_page = max(results_page.number - 4, 1)
    if start_page <= 3:
        start_page = 1
    end_page = results_page.number + 4 + 1
    if end_page >= paginator.num_pages - 1:
        end_page = paginator.num_pages + 1
    page_numbers = [n for n in range(start_page, end_page) if 0 < n <= paginator.num_pages]
    context = {'results': results_page, 'skill': skill, 'skills_name': skill_names, 'page_numbers': page_numbers}
    return render(request, 'hiscores/show_skill.html', context)


def player(request, user_name):
    player_profile = get_object_or_404(Skills, user_name=user_name)
    return render(request, 'hiscores/player.html', {'player': player_profile})
