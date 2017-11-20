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

def test(p,c):
    if p <= 3:
        if c > 5:
            a = [d for d in range(1,6)]
        else:
            a = [d for d in range(1,c+1)]
    elif c - p <= 3:
        a = [d for d in range(c-4,c+1)]
    else:
        a = [d for d in range(p-2,p+3)]
    return a
    
       if request.GET.get('p'):
            try:
                p = int(request.GET.get('p'))
                if p < 1:
                    p = 1
            except:
                p = 1
        else:
            p = 1
        saps = getpages(getsqls(Serverslog),p)
        sqls = saps[0]
        pages = saps[1]
        sqlcount = saps[2]
        p = saps[3]
        pagelist = test(p,pages)
        if 1 < pagelist[0]:
            previous_page = True
            p_5 = p - 5
            p_1 = p - 1
        if pagelist[-1] < pages:
            next_page = True
            pa5 = p + 5
            pa1 = p + 1
            
            
                                    {% if previous_page %}
                        <a href="?p={{ p_5 }}"><<</a> <a href="?p={{ p_1 }}"><</a>
                        {% endif %}
                        {% for pa in pagelist %}
                            <a href="?p={{ pa }}">{{ pa }}</a>
                        {% endfor %}
                        {% if next_page %}
                         <a href="?p={{ pa1 }}">></a> <a href="?p={{ pa5 }}">>></a>
                        {% endif %}
                        </td>
                        <td>{{ p }}/{{ pages }}</td>
