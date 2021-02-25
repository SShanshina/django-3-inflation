from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'

    with open('inflation_russia.csv', encoding='utf-8') as file:
        data = file.readlines()
        titles = data[0].strip().split(';')

        data_list = list()
        for item in data[1:]:
            item = item.strip().split(';')

            for el_i, element in enumerate(item):
                if el_i == 0 or el_i == 13:
                    continue
                elif len(element) == 0:
                    item[el_i] = '-'
                elif '.' in element:
                    item[el_i] = float(element)
                else:
                    item[el_i] = int(element)

            data_list.append(item)

    return render(request, template_name, context={
        'titles': titles,
        'inflation_data': data_list,
    })
