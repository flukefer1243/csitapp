from django.shortcuts import render
from csitweb import scholar, data, urls
# from django.http import HttpResponse

# Create your views here.


def index(request):
    name = request.GET['name']
    if name == 'wansuree':
        status = scholar.getData()
        print(status)
        return render(request, "fontend/index.html", {'info': data.wansuree[0], 'education': data.wansuree[1], 'status':status})
    elif name == 'prasart':
        return render(request, "fontend/index.html", {'info': data.prasart[0], 'education': data.prasart[1]})
    elif name == 'chakkrit':
        return render(request, "fontend/index.html", {'info': data.chakkrit[0], 'education': data.chakkrit[1]})
    elif name == 'ekkasit':
        return render(request, "fontend/index.html", {'info': data.ekkasit[0], 'education': data.ekkasit[1]})
    elif name == 'nattavadee':
        return render(request, "fontend/index.html", {'info': data.nattavadee[0], 'education': data.nattavadee[1]})
    elif name == 'wuttipong':
        return render(request, "fontend/index.html", {'info': data.wuttipong[0], 'education': data.wuttipong[1]})
    elif name == 'janjira':
        return render(request, "fontend/index.html", {'info': data.janjira[0], 'education': data.janjira[1]})
    elif name == 'adirek':
        return render(request, "fontend/index.html", {'info': data.adirek[0], 'education': data.adirek[1]})
    elif name == 'anongporn':
        return render(request, "fontend/index.html", {'info': data.anongporn[0], 'education': data.anongporn[1]})
    elif name == 'tawin':
        return render(request, "fontend/index.html", {'info': data.tawin[0], 'education': data.tawin[1]})
    elif name == 'kreangsak':
        return render(request, "fontend/index.html", {'info': data.kreangsak[0], 'education': data.kreangsak[1]})
    elif name == 'jaratsri':
        return render(request, "fontend/index.html", {'info': data.jaratsri[0], 'education': data.jaratsri[1]})
    elif name == 'winai':
        return render(request, "fontend/index.html", {'info': data.winai[0], 'education': data.winai[1]})
    elif name == 'kraisak':
        return render(request, "fontend/index.html", {'info': data.kraisak[0], 'education': data.kraisak[1]})
    elif name == 'sanya':
        return render(request, "fontend/index.html", {'info': data.sanya[0], 'education': data.sanya[1]})
    elif name == 'sutasinee':
        return render(request, "fontend/index.html", {'info': data.sutasinee[0], 'education': data.sutasinee[1]})
    elif name == 'phisetphong':
        return render(request, "fontend/index.html", {'info': data.phisetphong[0], 'education': data.phisetphong[1]})
    elif name == 'duangduen':
        return render(request, "fontend/index.html", {'info': data.duangduen[0], 'education': data.duangduen[1]})
    elif name == 'thanathorn':
        return render(request, "fontend/index.html", {'info': data.thanathorn[0], 'education': data.thanathorn[1]})
    elif name == 'nattapon':
        return render(request, "fontend/index.html", {'info': data.nattapon[0], 'education': data.nattapon[1]})
    elif name == 'antony':
        return render(request, "fontend/index.html", {'info': data.antony[0], 'education': data.antony[1]})


def show_articles(request):
    scholar_id = request.GET['scholar_id']
    params = {
        "hl": "th",
        "user": str(scholar_id)
    }
    articles = scholar.get_articles(params)
    return render(request, 'fontend/articles.html', {'articles': articles, 'size': len(articles)})


def timetable(request):
    email = request.GET['email']
    if email == 'wansureem@nu.ac.th':
        x = scholar.get_timetable1(data.wansuree[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'prasartb@nu.ac.th':
        x = scholar.get_timetable1(data.prasart[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'chakkrits@nu.ac.th':
        x = scholar.get_timetable1(data.chakkrit[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'ekkasitt@nu.ac.th':
        x = scholar.get_timetable1(data.ekkasit[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'nattavadeeho@nu.ac.th':
        x = scholar.get_timetable1(data.nattavadee[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'wuttipongr@nu.ac.th':
        x = scholar.get_timetable1(data.wuttipong[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'janjirap@nu.ac.th':
        x = scholar.get_timetable1(data.janjira[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'adirekr@nu.ac.th':
        x = scholar.get_timetable1(data.adirek[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'anongporns@nu.ac.th':
        x = scholar.get_timetable1(data.anongporn[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'tawint@nu.ac.th':
        x = scholar.get_timetable1(data.tawin[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'kreangsakt@nu.ac.th':
        x = scholar.get_timetable1(data.kreangsak[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'jaratsrir@nu.ac.th':
        x = scholar.get_timetable1(data.jaratsri[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'winaiw@nu.ac.th':
        x = scholar.get_timetable1(data.winai[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'kraisakk@nu.ac.th':
        x = scholar.get_timetable1(data.kraisak[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'sanyak@nu.ac.th':
        x = scholar.get_timetable1(data.sanya[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'sutasineec@nu.ac.th':
        x = scholar.get_timetable1(data.sutasinee[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'phisetphongs@nu.ac.th':
        x = scholar.get_timetable1(data.phisetphong[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'duangduenr@nu.ac.th':
        x = scholar.get_timetable1(data.duangduen[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'thanathornp@nu.ac.th':
        x = scholar.get_timetable1(data.thanathorn[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'nattaponk@nu.ac.th':
        x = scholar.get_timetable1(data.nattapon[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'nattaponk@nu.ac.th':
        x = scholar.get_timetable1(data.nattapon[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})
    elif email == 'antonyh@nu.ac.th':
        x = scholar.get_timetable1(data.antony[0]['timetable'])
        return render(request, 'fontend/timetable.html', {'table': x})