# uncteams app views.py

from uncteams.models import Team, Athlete, Coach
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    team_list = Team.objects.all()
    paginator = Paginator(team_list, 25)
    page = request.GET.get('page')
    try:
        teams= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        teams = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        teams = paginator.page(paginator.num_pages)
    #return render(request, "uncteams/home.html", context)
    return render(request, 'uncteams/home.html', {"teams": teams})

def team(request, pk):
    team = get_object_or_404(Team, id=pk)
    #is this the right call to activate coaches?..
    coach_list = Coach.objects.all()
    athlete_list = Athlete.objects.all()
    paginator = Paginator(athlete_list, 20)
    page = request.GET.get('page')
    try:
        athletes= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        athletes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        athletes = paginator.page(paginator.num_pages)
    return render(request, "uncteams/team.html", {"athletes": athletes,"team": team, "coaches":coach_list})
    #need to pass something to represent coaches...
   
def athlete(request, pk):
    #athlete = Athlete.objects.order_by('?')[0]
    athlete = get_object_or_404(Athlete, id=pk)
    return render(request, "uncteams/athlete.html", {'athlete': athlete})

def athleteList(request):
    #athlete = Athlete.objects.order_by('?')[0]
    athlete_list = Athlete.objects.all()
    paginator = Paginator(athlete_list, 25)
    page = request.GET.get('page')
    try:
        athletes= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        athletes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        athletes = paginator.page(paginator.num_pages)

    return render(request, 'uncteams/athlete_list.html', {"athletes": athletes})
    
    
    #athlete = get_object_or_404(Athlete)
    #return render(request, "uncteams/athlete_list.html", {'athlete': athlete})

