from pyquery import PyQuery as pq

try:
    def altulamlar(bu, d = 0):
        if bu.hasClass("parent"): return
        u = ".filterArea .filter.filterCategory:first " + (".filterList " * (d+2)) + " .filterItem"
        ulamlar = pq(bu("a").attr("href"))(u)
        for ulam in ulamlar.items():
            if ulam.hasClass("parent"): continue
            print(("\t"*(d+1)) + ulam("a").text())
            altulamlar(ulam, d+1)

    yerlik = "https://n11.com"
    kaynak_yiv = pq(yerlik)
    ulamlar = kaynak_yiv("nav.catMenu ul li")
    for ulam in ulamlar.items():
        if(ulam.attr("class") == "catMenuItem"):
            print(ulam("a:first").text())
        elif(ulam.attr("class") == "subCatMenuItem"):
            altulamlar(ulam)
except KeyboardInterrupt:
    print("\n\n\t\tDurduruldu")
    pass
