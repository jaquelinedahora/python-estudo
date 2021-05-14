import datetime


def data_de_hoje():
    return datetime.datetime.now().strftime("%d/%m/%Y")