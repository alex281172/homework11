def add_separators(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print('-' * 70)
        result = f(*args, **kwargs)
        # поведение после вызова
        print('-' * 70)
        return result

    # возвращается функция inner с новым поведением
    return inner


