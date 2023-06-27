from django.http import HttpResponse

def home(request):
    judul   = "<h3> This is home </h3>"
    body    = "<h1> Halloooo Randiii </h1>"

    output = judul + body

    return HttpResponse (output)

def about(request):

    judul2 = "<h2> Halo Mazaya :)) </h2>"
    body2 = "<h1> Mazaya Belum Mandi </h1>"

    output2 = judul2 + body2

    return HttpResponse (output2)