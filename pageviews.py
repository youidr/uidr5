def getsqls(v1):
    v2 = v1.objects.all().order_by('-id')
    return v2

def getpages(v3,v4):
    showpage = 20
    if v3.count() % showpage == 0:
        v5 = v3.count() // showpage
    else:
        v5 = (v3.count() // showpage) + 1
    if v4 > v5:
        v4 = v5
    v6 = v3[(v4 - 1) * showpage:v4 * showpage]
    return v6,v5,v3.count(),v4
    
            if request.GET.get('p'):
            try:
                p = int(request.GET.get('p'))
            except:
                p = 1
        else:
            p = 1
        saps = getpages(getsqls(Serversum),p)
        sqls = saps[0]
        pages = saps[1]
        pagelist = [pa for pa in range(1,pages + 1)]
        sqlcount = saps[2]
        p = saps[3]
