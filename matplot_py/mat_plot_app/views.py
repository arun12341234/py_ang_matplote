from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import matplotlib as pl
pl.use('Agg')
import pandas as pd
import os
import seaborn as sb
 
 
import matplotlib.pyplot as plt
import numpy as np
import django 


import io

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
 
class LinksPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'links.html', context=None)
 
 
class Customers(TemplateView):
    def getCust(request):
        name='liran'
        return HttpResponse('{ "name":"' + name + '", "age":31, "city":"New York" }')
    def getNums(request):
        n = np.array([2, 3, 4])
        name1 = "name-" + str(n[1])
        return HttpResponse('{ "name":"' + name1 + '", "age":31, "city":"New York" }')
 
    def getAvg(request):
        s1=request.GET.get("val","")
        if len(s1)==0:
            return HttpResponse("none")
        l1=s1.split(',')
        ar=np.array(l1,dtype=int)
 
        return HttpResponse(str(np.average(ar)))
 
    def getimage(request):
        fig = Figure() #imp
        fig,ax = plt.subplots() #imp
        # x = np.arange(0, 2 * np.pi, 0.01)
        # s = np.cos(x) ** 2
        
        # plt.plot(x, s)
 
        # plt.xlabel('xlabel(X)')
        # plt.ylabel('ylabel(Y)')
        # plt.title('Simple Graph!')
        # plt.grid(True)

        Country = ['USA','Canada','Germany','UK','France']
        GDP_Per_Capita = [45000,42000,52000,49000,47000]
        # print(Country)
        xAxis = [i + 0.5 for i, _ in enumerate(Country)]

        plt.bar(xAxis, GDP_Per_Capita, color='teal')
        plt.title('Country Vs GDP Per Capita', fontsize=14)
        plt.xlabel('Country', fontsize=14)
        plt.ylabel('GDP Per Capita', fontsize=14)
        plt.xticks([i + 0.5 for i, _ in enumerate(Country)], Country)
        plt.show()



        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        # plt.close(fig)
        canvas = FigureCanvas(fig)
        response = HttpResponse(content_type='image/jpg')
        canvas.print_jpg(response)
        # fig.savefig(response )
        return response
 
    def getData(request):
        samp = np.random.randint(100, 600, size=(4, 5))
        df = pd.DataFrame(samp, index=['avi', 'dani', 'rina', 'dina'],
                          columns=['Jan', 'Feb', 'Mar', 'Apr', 'May'])
        return HttpResponse(df.to_html(classes='table table-bordered'))
 
    def getSBData(request):
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'titanic_train.csv')
        df = pd.read_csv(file_path)
        gr=sb.factorplot(x='Survived', hue='Sex', data=df, col='Pclass', kind='count')
        response = HttpResponse(content_type="image/jpeg")
        gr.savefig(response, format="png")
        return response