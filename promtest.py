from timeit import default_timer as timer
from prometheus_client import start_http_server, Summary, Gauge
import time
import datetime 
import random
import urllib

# Create a metric to track time spent and requests made.
LATENCY_TIME = Gauge('latency_getting_google', 'latency to google')
LATENCY_LOCAL = Gauge('local_latency', 'hitting localhost')
def get_latency():
    """a function to grab latency to google.com"""
    url='http://google.com'
    nf = urllib.request.urlopen(url)
    start = datetime.datetime.now()
    page = nf.read()
    end = datetime.datetime.now()
    nf.close()
    delta = end - start
    print(int(delta.total_seconds() * 1000))
    LATENCY_TIME.set(float(delta.total_seconds() * 1000))
    # end - start gives you the page load time


def get_latency_local():
    """a function to grab latency to localhost"""
    url='http://localhost:8090'
    nf = urllib.request.urlopen(url)
    start = datetime.datetime.now()
    page = nf.read()
    end = datetime.datetime.now()
    nf.close()
    delta = end - start
    print(int(delta.total_seconds() * 1000))
    LATENCY_LOCAL.set(float(delta.total_seconds() * 1000))
    # end - start gives you the page load time

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8090)
    # Generate some requests.
    while True:
        get_latency()
        get_latency_local()
        time.sleep(5)
