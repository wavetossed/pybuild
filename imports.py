# tests that all the following libraries have been successfully installed
# using pip install
from amqplib import client_0_8 as amqp
from binascii import crc32   # zlib version is not cross-platform
from cgi import parse_qs
from collections import namedtuple
from contextlib import contextmanager
from Cookie import SimpleCookie
from cStringIO import StringIO
from datetime import *
from diesel.protocols.wsgi import WSGIApplication
from eventlet import wsgi, listen
from gevent import wsgi as wsgi_fast, pywsgi as wsgi, monkey
from io import BytesIO
from io import TextIOWrapper
from jinja2 import Environment, FunctionLoader
from kombu.connection import BrokerConnection
from kombu.messaging import Exchange, Queue, Consumer, Producer
from lxml import etree
from mako.lookup import TemplateLookup
from mako.template import Template
from paste import httpserver
from paste.translogger import TransLogger
from StringIO import StringIO
from StringIO import StringIO as BytesIO
from subprocess import Popen, PIPE
from tempfile import TemporaryFile
from threading import local
from traceback import format_exc
from twisted.internet import reactor
from twisted.python.threadpool import ThreadPool
from twisted.web import server, wsgi
from urllib import urlencode, quote as urlquote, unquote as urlunquote
from urlparse import urlunsplit, urljoin, SplitResult as UrlSplitResult
from UserDict import DictMixin
from wsgiref.handlers import CGIHandler
from wsgiref.simple_server import make_server, WSGIRequestHandler
from zlib import compress, decompress
import amqplib.client_0_8 as amqp
import ast
import base64
import cgi
import codecs
import ConfigParser
import copy
import cPickle as pickle
import doctest
import email.utils
import fcntl
import flup.server.fcgi
import functools
import gdbm
import hmac
import htmlentitydefs
import httplib
import imp
import inspect # Expensive module. Only import if necessary.
import itertools
import json
import lxml
import lxml.etree
import memcache
import mimetypes
import os
import pickle
import pika
import pymysql
import random
import re
import resource
import sched # use the python standard library sheduler
import shlex
import signal
import signal, errno
import socket
import subprocess
import sys
import sys, os
import sys, time
import telnetlib
import tempfile
import thread
import threading
import time
import time as t
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
import traceback
import warnings
import xml.parsers.expat
import zlib

import tokyo.tyrant
import tokyo.cabinet
import XSLTools
import numpy
import pylint
import coverage
import pycallgraph
import mkcode
import sqlalchemy
import buzhug
import flask
import restez
import pytz
import mcdict
import paramiko
import pexpect
import riak
import ptrace
import html5lib
import curl
import sqlite3
from dateutil.relativedelta import *
import msgpack
import graypy
import haigha
from stormed import Connection, Message

import txamqp
import pylibrabbitmq
import boto
from pyrrd.rrd import DataSource, RRA, RRD
import sqlalchemy
import pyvb
import mkcode
import pydot
import py_interface
from google.protobuf import descriptor
import riak
from pycopia.IO import ConsoleIO
from pycopia import timelib
#from pycopia.CLI import Shell
#from pycopia.db.types import *
#from pycopia.net import dnsupdate

#These ones were tricky to get right
import zmq
import pylibmc
from fapws import base, config
import fapws._evwsgi as evwsgi
from google.protobuf import descriptor
import pysvn
from cherrypy import wsgiserver
import httplib2

import os
import time
print "if you want to check the memory consumption see this PID:"
print os.getpid()
time.sleep(30)
