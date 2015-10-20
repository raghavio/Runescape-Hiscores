from django.core.exceptions import FieldError
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_http_methods

from .models import Skills
from utils import skill_names
from forms import SearchForm, CompareForm


@require_http_methods(["GET"])
def show_skill(request, skill):
    skill = str(skill)
    skill_exp = skill + '_exp'
    number_of_skills = len(skill_names)
    context = {}

    try:
        all_results = Skills.objects.order_by('-%s' % skill_exp).values("user_name", skill, skill_exp)
    except FieldError:
        raise Http404("404: Skill could not be found.")
    paginator = Paginator(all_results, number_of_skills)

    rank = request.GET.get('rank', None)
    if rank and rank.isdigit():
        from math import ceil
        rank = float(rank)
        page = ceil(rank / number_of_skills)
        context['highlight_rank'] = rank
    else:
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

    search_form, compare_form = _get_form(request)
    if search_form.is_valid():
        return HttpResponseRedirect(reverse('player', args=(request.GET['search'],)))
    elif compare_form.is_valid():
        return HttpResponseRedirect(reverse('compare', args=(request.GET['player1'], request.GET['player2'])))

    context.update({'results': results_page, 'skill': skill, 'skills': skill_names, 'page_numbers': page_numbers,
                    'search_form': search_form, 'compare_form': compare_form})
    return render(request, 'hiscores/show_skill.html', context)


@require_http_methods(["GET"])
def player(request, user_name):
    player_profile = get_object_or_404(Skills, user_name=user_name)

    search_form, compare_form = _get_form(request)
    if not compare_form.is_bound:  # Check if form is bounded with any data or not.
        # If not bounded, set initial value of compare form to player's user_name.
        compare_form.initial = {'player1': user_name}
    if search_form.is_valid():
        return HttpResponseRedirect(reverse('player', args=(request.GET['search'],)))
    elif compare_form.is_valid():
        return HttpResponseRedirect(reverse('compare', args=(request.GET['player1'], request.GET['player2'])))

    context = {'player': player_profile, 'skills': skill_names, 'search_form': search_form,
               'compare_form': compare_form}
    return render(request, 'hiscores/player.html', context)


def _get_form(request):
    """
    Creates unbounded or bonded search and compare form. Depending on whether request object has data or not.
    :param request: HttpRequest object with data if user has submitted the form.
    :return: forms created
    """
    if 'player1' and 'player2' in request.GET:
        search_form, compare_form = SearchForm(), CompareForm(request.GET)
    elif 'search' in request.GET:
        search_form, compare_form = SearchForm(request.GET), CompareForm()
    else:
        search_form, compare_form = SearchForm(), CompareForm()
    return search_form, compare_form


@require_http_methods(["GET"])
def compare(request, player1, player2):
    player1_profile = Skills.objects.get(user_name=player1)
    player2_profile = Skills.objects.get(user_name=player2)
    player1_skills, player2_skills = player1_profile.compare_skills(player2_profile)
    context = {'player1_username': player1_profile.user_name, 'player2_username': player2_profile.user_name,
               'skills': skill_names,
               'player1_skills': player1_skills,
               'player2_skills': player2_skills}
    return render(request, 'hiscores/compare.html', context)
