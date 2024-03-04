from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, Http404
from .models import Snippet
import secrets
import string


class Card:
    def __init__(self, title, hr, id, dop):
        self.title = title
        self.hr = hr
        self.id = id
        self.dop = dop

    def get_dict(self):
        return {
            'title': self.title,
            'hr': self.hr,
            'id': self.id,
            'dop': self.dop
        }


def get_random_name():
    letters = string.ascii_letters
    digits = string.digits
    alphabet = letters + digits
    pwd_length = 12
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    return pwd


def get_pc_specs():
    specs = {
        'mypc': [
            Card('CPU', True, 'cpu_name', False),
            Card('GPU', True, 'gpu_name', False),
            Card('MB', True, 'mb_name', False),
            Card('RAM', True, 'ram_name', False),
            Card('COOLING', True, 'cooling_name', False),
            Card('PSU', True, 'psu_name', False),
            Card('STORAGE', True, 'storage_name', False),
            Card('CASE', False, 'case_name', [
                {'title': 'TOP', 'id': 'top_name'},
                {'title': 'BOTTOM', 'id': 'bottom_name'},
                {'title': 'FRONT', 'id': 'front_name'},
                {'title': 'EXHAUST', 'id': 'exhaust_name'},
            ])

        ],

        'monitors': [
            Card('MONITORS', False, 'monitor_name', False)
        ],

        'accessories': [
            Card('MOUSE', True, 'mouse_name', False),
            Card('MOUSEPAD', True, 'mousepad_name', False),
            Card('KEYBOARD', True, 'keyboard_name', [
                {'title': 'BASE', 'id': 'base_name'},
                {'title': 'SWITCHES', 'id': 'switches_name'},
                {'title': 'STABS', 'id': 'stab_name'},
                {'title': 'LUBE', 'id': 'lube_name'},
                {'title': 'KEYCAPS', 'id': 'keycaps_name'},
            ]),
            Card('SPEAKERS', True, 'speakers_name', False),
            Card('HEADPHONES', True, 'headphones_name', [
                {'title': 'AMP', 'id': 'amp_name'},
            ]),
            Card('AUDIO_IFACE', True, 'audio_int_name', False),
            Card('MIC', False, 'mic_name', False),
        ]
    }
    return specs


def nr_to_br(s):
    s = s.replace(",", 'repl')
    return s


def index_page(request: WSGIRequest):
    context = get_pc_specs()

    if request.method == "POST":
        snippet = Snippet()
        data = {
            'mypc': [],
            'monitors': [],
            'accessories': []
        }

        for item in context['mypc']:
            same = None
            for obj in context['mypc']:
                if obj.id == item.id:
                    same = obj
                    break

            d = same.get_dict()
            new_d = []
            if d['dop']:
                for tip in d['dop']:
                    new_d.append([tip['title'], request.POST[tip['id']]])

            d['dop'] = new_d
            d['data'] = nr_to_br(request.POST[item.id])  # Replacing commas to breaks
            data['mypc'].append(d)

        for item in context['monitors']:
            same = None
            for obj in context['monitors']:
                if obj.id == item.id:
                    same = obj
                    break

            d = same.get_dict()
            new_d = []
            if d['dop']:
                for i in d['dop']:
                    new_d.append([i['title'], request.POST[i['id']]])

            d['dop'] = new_d
            d['data'] = nr_to_br(request.POST[item.id])  # Replacing commas to breaks
            data['monitors'].append(d)

        for item in context['accessories']:
            same = None
            for obj in context['accessories']:
                if obj.id == item.id:
                    same = obj
                    break

            d = same.get_dict()
            new_d = []
            if d['dop']:
                for i in d['dop']:
                    new_d.append([i['title'], request.POST[i['id']]])

            d['dop'] = new_d
            d['data'] = nr_to_br(request.POST[item.id])  # Replacing commas to breaks
            data['accessories'].append(d)

        # print(data)

        snippet.data, snippet.name = data, get_random_name()
        snippet.save()

        return redirect(f'/{snippet.name}')

    return render(request, 'pages/index.html', context)


def paste_page(request: WSGIRequest, snippet):
    al = Snippet.objects.all()
    flag = False
    for obj in al:  # Checking the existence of a snippet
        if obj.name == snippet:
            flag = True

    if flag:
        obj = Snippet.objects.get(name=snippet)
        context = {
            'mypc': eval(obj.data)['mypc'],
            'monitors': eval(obj.data)['monitors'],
            'accessories': eval(obj.data)['accessories'],
        }

        return render(request, 'pages/final.html', context)

    else:
        return render(request, 'pages/error.html', {'ex': snippet})


def error_page(request: WSGIRequest):
    context = {

    }
    return render(request, 'pages/error.html', context)
