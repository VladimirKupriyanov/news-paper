from django import template

register = template.Library()


@register.filter(name='multiply')  # регестрируем наш фильтр под именем multiply, чтоб django понимал,
# что это именно фильтр, а не простая функция
def multiply(value, arg):  # первый аргумент здесь это то значение, к которому надо применить фильтр,
    # второй аргумент — это аргумент фильтра, т.е. примерно следующее будет в шаблоне value|multiply:arg
    if isinstance(value, str) and isinstance(arg, int):  # проверяем, что value — это точно строка,
        # а arg — точно число, чтобы не возникло курьёзов
        return str(value) * arg  # возвращаемое функцией значение — это то значение, которой подставится к нам в шаблон
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}')  # в случае если кто-то неправильно
        # воспользовался нашим тегом выводим ошибку


@register.filter(name='censor')
def censor(value):
    if isinstance(value, str):
        value = value.lower().replace(',', '').replace('.', '')\
            .replace(':', '').replace(';', '').replace('!', '')\
            .replace('?', '').replace('_', ' ').split()
        censorList = ['bacon', 'spicy', 'hamburger']

        result = []
        for i in value:
            if i in censorList:
                result.append('*' * len(i))
            else:
                result.append(i)
        result = ' '.join(result)
        return result
    else:
        raise ValueError(f'Not str {type(value)}')
