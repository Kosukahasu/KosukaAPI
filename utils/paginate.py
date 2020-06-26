def paginate(page, limit, maxLimit):
    p = int(page)
    l = int(limit)

    if p < 1:
        p = 1

    if l < 1:
        l = 50

    if l > maxLimit:
        l = maxLimit

    start = int(p-1) * int(l)
    return "LIMIT %d,%d"%(start,l)

def rankPaginate(index, limit, page):
    if page == 1:
        return "%d"%(index+1)

    start = int(page-1) * int(limit)
    return "%d"%(index+1+start)
