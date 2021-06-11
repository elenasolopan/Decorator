from Documents import documents
import datetime


def logger(log_path):
    def log_info(function):
        def function_replaced(*args, **kwargs):
            result = function(*args, **kwargs)
            with open(log_path, 'a+', encoding='utf-8') as f:
                f.write(f"{datetime.datetime.now()} {function.__name__} {args} {kwargs} {result}\n")
            return result
        return function_replaced
    return log_info


@logger(r'C:\Users\zinov\PycharmProjects\PYTHON OOP\Decorator\app.log')
def search_name(number_doc):
    """ функция, которая спросит номер документа из "documents" и выведет имя человека, которому он принадлежит"""
    for document in documents:
        documents_sorted = dict([(document['number'], document['name'])])
        for doc, name in documents_sorted.items():
            if number_doc == doc:
                print(f"Имя пользователя: {name}")
                return name
    print(f"Документ с номером '{number_doc}' отсутствует")
    return f'Error'


if __name__ == '__main__':
    search_name(input("Введите номер документа пользователя: "))
