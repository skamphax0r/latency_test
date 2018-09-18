"""testing prometheus stuff"""
import time
import datetime
import urllib
from timeit import default_timer as timer
from prometheus_client import start_http_server, Summary, Gauge

LATENCY_TIME = Gauge('latency_getting_google', 'latency to google')
LATENCY_LOCAL = Gauge('local_latency', 'hitting localhost')


def get_latency():
    """a function to grab latency to google.com"""
    url = 'http://google.com'
    nf = urllib.request.urlopen(url)
    start = datetime.datetime.now()
    page = nf.read()
    end = datetime.datetime.now()
    nf.close()
    delta = end - start
    print(int(delta.total_seconds() * 1000))
    LATENCY_TIME.set(float(delta.total_seconds() * 1000))


def get_latency_local():
    """a function to grab latency to localhost"""
    url = 'http://localhost:8090'
    nf = urllib.request.urlopen(url)
    start = datetime.datetime.now()
    page = nf.read()
    end = datetime.datetime.now()
    nf.close()
    delta = end - start
    print(int(delta.total_seconds() * 1000))
    LATENCY_LOCAL.set(float(delta.total_seconds() * 1000))


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8090)
    # populate some metrics
    while True:
        get_latency()
        get_latency_local()
        time.sleep(5)
