from django.shortcuts import render
from csitweb import *
# from django.http import HttpResponse

# Create your views here.


def index(request):
    name = request.GET['name']
    if name == 'wansuree':
        status = getData()
        # print(status)
        return render(request, "fontend/index.html", {'info': wansuree[0], 'education': wansuree[1], 'status':status})
    elif name == 'prasart':
        return render(request, "fontend/index.html", {'info': prasart[0], 'education': prasart[1]})
    elif name == 'chakkrit':
        return render(request, "fontend/index.html", {'info': chakkrit[0], 'education': chakkrit[1]})
    elif name == 'ekkasit':
        return render(request, "fontend/index.html", {'info': ekkasit[0], 'education': ekkasit[1]})
    elif name == 'nattavadee':
        return render(request, "fontend/index.html", {'info': nattavadee[0], 'education': nattavadee[1]})
    elif name == 'wuttipong':
        return render(request, "fontend/index.html", {'info': wuttipong[0], 'education': wuttipong[1]})
    elif name == 'janjira':
        return render(request, "fontend/index.html", {'info': janjira[0], 'education': janjira[1]})
    elif name == 'adirek':
        return render(request, "fontend/index.html", {'info': adirek[0], 'education': adirek[1]})
    elif name == 'anongporn':
        return render(request, "fontend/index.html", {'info': anongporn[0], 'education': anongporn[1]})
    elif name == 'tawin':
        return render(request, "fontend/index.html", {'info': tawin[0], 'education': tawin[1]})
    elif name == 'kreangsak':
        return render(request, "fontend/index.html", {'info': kreangsak[0], 'education': kreangsak[1]})
    elif name == 'jaratsri':
        return render(request, "fontend/index.html", {'info': jaratsri[0], 'education': jaratsri[1]})
    elif name == 'winai':
        return render(request, "fontend/index.html", {'info': winai[0], 'education': winai[1]})
    elif name == 'kraisak':
        return render(request, "fontend/index.html", {'info': kraisak[0], 'education': kraisak[1]})
    elif name == 'sanya':
        return render(request, "fontend/index.html", {'info': sanya[0], 'education': sanya[1]})
    elif name == 'sutasinee':
        return render(request, "fontend/index.html", {'info': sutasinee[0], 'education': sutasinee[1]})
    elif name == 'phisetphong':
        return render(request, "fontend/index.html", {'info': phisetphong[0], 'education': phisetphong[1]})
    elif name == 'duangduen':
        return render(request, "fontend/index.html", {'info': duangduen[0], 'education': duangduen[1]})
    elif name == 'thanathorn':
        return render(request, "fontend/index.html", {'info': thanathorn[0], 'education': thanathorn[1]})
    elif name == 'nattapon':
        return render(request, "fontend/index.html", {'info': nattapon[0], 'education': nattapon[1]})
    elif name == 'antony':
        return render(request, "fontend/index.html", {'info': antony[0], 'education': antony[1]})


def show_articles(request):
    scholar_id = request.GET['scholar_id']
    params = {
        "hl": "th",
        "user": str(scholar_id)
    }
    articles = get_articles(params)
    return render(request, 'fontend/articles.html', {'articles': articles, 'size': len(articles)})


def timetable(request):
    email = request.GET['email']
    if email == 'wansureem@nu.ac.th':
        x = get_timetable1(wansuree[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'prasartb@nu.ac.th':
        x = get_timetable1(prasart[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'chakkrits@nu.ac.th':
        x = get_timetable1(chakkrit[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'ekkasitt@nu.ac.th':
        x = get_timetable1(ekkasit[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'nattavadeeho@nu.ac.th':
        x = get_timetable1(nattavadee[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'wuttipongr@nu.ac.th':
        x = get_timetable1(wuttipong[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'janjirap@nu.ac.th':
        x = get_timetable1(janjira[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'adirekr@nu.ac.th':
        x = get_timetable1(adirek[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'anongporns@nu.ac.th':
        x = get_timetable1(anongporn[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'tawint@nu.ac.th':
        x = get_timetable1(tawin[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'kreangsakt@nu.ac.th':
        x = get_timetable1(kreangsak[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'jaratsrir@nu.ac.th':
        x = get_timetable1(jaratsri[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'winaiw@nu.ac.th':
        x = get_timetable1(winai[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'kraisakk@nu.ac.th':
        x = get_timetable1(kraisak[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'sanyak@nu.ac.th':
        x = get_timetable1(sanya[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'sutasineec@nu.ac.th':
        x = get_timetable1(sutasinee[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'phisetphongs@nu.ac.th':
        x = get_timetable1(phisetphong[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'duangduenr@nu.ac.th':
        x = get_timetable1(duangduen[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'thanathornp@nu.ac.th':
        x = get_timetable1(thanathorn[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'nattaponk@nu.ac.th':
        x = get_timetable1(nattapon[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'nattaponk@nu.ac.th':
        x = get_timetable1(nattapon[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'antonyh@nu.ac.th':
        x = get_timetable1(antony[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})