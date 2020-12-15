# coding: utf-8
import os
import gevent
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from gevent import monkey; monkey.patch_all()
from lib.utils.util import load_env_config
from lib.scanner.scan import Scan
from lib.secureheaders.site import Site

class Headers():

    def __init__(self):
        load_env_config()
        self.headers_filter = os.getenv('HEADERS').lower().split(',')
        self.scanner = Scan()
        self.data = []

    #Método que inicia el escaneo, filtra los encabezados obtenidos y organiza toda la información obtenida
    def work_headers(self, direction):
        try:
            site = Site({'id': direction[0], 'domain': direction[1]})
            response = self.scanner.connect(site['domain'])
            if response or (response['status_code' == 200]):
                site.update({'url': response['url']})
                site.update({'status_code': response['status_code']})
                for header in response['headers'].keys():
                    if header in self.headers_filter:
                        site['headers'].update({header: response['headers'][header]})
            self.data.append(site)
        except TypeError:
            print("[!] site <{}> will be excluded from the analysis".format(direction))

    #Este método es el que se encarga de extraer las diferentes direcciones del sitio web a escanear
    def get_links(self, url):
        scheme = 'http'
        uri = "{}://{}".format(scheme, url)
        req = Request(uri, headers={'User-Agent': 'Mozilla/5.0'})
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        list=[]
        firstUrl = []
        firstUrl.append(0)
        firstUrl.append(url)
        list.append(firstUrl)
        id = 1
        for link in soup.findAll('a'):
            href = link.get('href')
            direction = []
            if href:
                if href and "#" not in href and href.startswith('/'):
                    direction.append(id)
                    direction.append(url+href)
                    list.append(direction)
                    id += 1
        return list

    #Método principal que inicia el escaneo en todas las url utilizando un pool de threads
    def run(self, url, num_threads):
        print("Iniciando la extracción de direcciones presentes en la página de inicio...")
        dictsites = self.get_links(url)
        start = 0
        thread = 1
        while (start < len(dictsites)):
            print("Iniciando el escaneo de cada dirección..." )
            print('Thread pool {} ({} - {})'.format(thread, start, start + num_threads))
            thread += 1
            threads = [gevent.spawn(self.work_headers, item) for item in dictsites[start:start+num_threads]]
            gevent.joinall(threads)
            start += num_threads
        print("Resultados:")
        if not (self.data == []):
            orderedData = sorted(self.data,key=lambda site : site['id'])
            for site in orderedData:
                print("")
                print("La dirección "+site['url'] + " cuenta con los siquientes encabezados:")
                for header in site['headers']:
                    print("Encabezado: " +header)
                    print("Valor: "+ site['headers'][header])
                    print("------------------------------------")
        self.scanner.get_summary(self.data)