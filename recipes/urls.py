TODOS = [
    {'id': 1, 'title': 'learn python'},
    {'id': 2, 'title': 'get paid'},
]


def get_data(pk):
    for data in TODOS:
        if data['id'] == int(pk):
            return data
        return []


def checking(request):
    print(request)


paths = {
    '/': {'status': 200},
    '/recipes': {'status': 200},
    '/recipes/{}/': {'status': 200},
}
