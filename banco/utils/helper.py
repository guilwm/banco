from datetime import date, datetime


def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_para_date(data):
    return datetime.strptime(data, '%d/%m/%Y')


def format_float_str_moeda(valor):
    return f'R$ {valor:,.2f}'



