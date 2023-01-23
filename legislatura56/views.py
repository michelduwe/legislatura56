from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from legislatura56.models import Deputado
import requests
from bs4 import BeautifulSoup
import urllib3
import re

urllib3.disable_warnings()

class ImportarDados(TemplateView):
    Deputado.objects.all().delete()

    header = {"accept": "application/json"}
    url = "https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome"
    capturou_dados = False
    while not capturou_dados:
        req = requests.get(url, headers=header, verify=False)
        if req.status_code == 200:
            capturou_dados = True
    print("Dados de deputados capturados")
    dados_deputados = req.json()

    for num, deputado in enumerate(dados_deputados["dados"]):
        url_deputado = "https://www.camara.leg.br/deputados/{}/biografia".format(deputado["id"])
        capturou_deputado = False
        while not capturou_deputado:
            req_deputado = requests.get(url_deputado, verify=False)
            if req_deputado.status_code == 200:
                capturou_deputado = True
        print("Dados do deputado {} capturado com sucesso".format(deputado["nome"]))
        soup = BeautifulSoup(req_deputado.content, "html.parser")
        dp = Deputado()
        dp.nome = deputado["nome"]
        dp.partido = deputado["siglaPartido"]
        dp.estado = deputado["siglaUf"]
        biografia_detalhes = soup.find_all("section", class_="biografia-detalhes-deputado")[0]
        cortes: list = re.split("<strong>\n", biografia_detalhes.prettify())
        for corte in cortes:
            if "Atividades Parlamentares:" in corte:
                selecao = corte.split("</strong>\n")[1]
                bs4_selecao = BeautifulSoup(selecao, "html.parser")
                dp.carreira =  bs4_selecao.text
            if "Atividades Profissionais e Cargos Públicos:" in corte:
                selecao = corte.split("</strong>\n")[1]
                bs4_selecao = BeautifulSoup(selecao, "html.parser")
                dp.curriculo =  bs4_selecao.text
            if "Atividades Partidárias:" in corte:
                selecao = corte.split("</strong>\n")[1]
                bs4_selecao = BeautifulSoup(selecao, "html.parser")
                dp.papel = bs4_selecao.text
            if "Estudos e Cursos Diversos:" in corte:
                selecao = corte.split("</strong>\n")[1]
                bs4_selecao = BeautifulSoup(selecao, "html.parser")
                dp.curriculo += bs4_selecao.text

        dp.cargo = biografia_detalhes.find_all("p")[0].text
        dp.biografia = soup.find_all("ul", class_="informacoes-deputado")[0].text
        dp.save()

            
    template_name = "paginas/importar_dados.html"

class ProcuraDeputado(ListView):

    model = Deputado
    template_name = "paginas/resultados.html"

    def get_queryset(self):
        query = self.request.GET.get('query')
        print(dict(self.request.GET))
        lista = Deputado.objects.filter(nome__icontains=query)
        return lista

class ListaDeputados(ListView):

    model = Deputado
    template_name = "paginas/lista_deputados.html"

    def get_queryset(self):
        if "q_estado" in self.request.GET:
            estado = self.request.GET.get("q_estado")
            lista = Deputado.objects.filter(estado=estado)
        elif "q_id" in self.request.GET:
            self.template_name = "paginas/deputado.html"
            id = int(self.request.GET.get("q_id"))
            print(id)
            lista = Deputado.objects.get(id=id)
        else:
            lista = Deputado.objects.all()
        return lista

class Home(ListView):

    model = Deputado
    template_name = "paginas/index.html"

    def get_queryset(self):
        lista = Deputado.objects.order_by('estado').values('estado').distinct()
        return lista

def display(request):
    dep = Deputado.objects.all()
    
    return render(request, "paginas/display.html", {'dep': dep})
