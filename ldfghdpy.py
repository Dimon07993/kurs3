import json
import datetime

with open('operations.json', 'r', encoding='utf-8') as f:
    operations = json.load(f)


def format_date(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return date.strftime('%d.%m.%Y')

def format_transaction(transaction):
    if 'from' in transaction:
        from_info, to_info = transaction['from'].split(' '), transaction['to'].split(' ')
        from_format = f'{from_info[1][:4]} {from_info[1][4:6]}** **** {from_info[1][-4:]}'  # 1234 5678 9012 3456
        to_format = f'**{to_info[1][-4:]}'
        return f'{from_info[0]} {from_format} -> {to_info[0]} {to_format}'
    else:
        to_info = transaction['to'].split(' ')
        to_format = f'{to_info[0]} **{to_info[1][-4:]}'
        return to_format


last_operations = sorted(operations[-5:], key=lambda x: x['date'], reverse=True)
for operation in last_operations:
    print(format_date(operation['date']), operation['description'])
    print(format_transaction(operation))
    print(operation['operationAmount']['amount'], operation['operationAmount']['currency']['code'] + '\n')