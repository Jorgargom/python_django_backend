from django.shortcuts import render, HttpResponse


html_base ="""
<h1>Mi web personal</h1>
<ul>

<li><a href="/">Portada</a></li>
<li><a href="/about-me/">Acerca de</a></li>
<li><a href="/portfolio/">Portfolio</a></li>
<li><a href="/contacto/">Contacto</a></li>

</ul>
"""

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def about(request):
    return HttpResponse(html_base + """
    <h2>asiendo cosas</h2>
    """)

def portfolio(request):
    return HttpResponse(html_base + """
    <h2>muchas cosas</h2>
    """)

def contacto(request):
    return HttpResponse(html_base + """
    <h2>contratame</h2>
    """)
