def get_population(country_dic):
    
    population_dic={
        '2022': int(country_dic['2022 Population']),
        '2020': int(country_dic['2020 Population']),
        '2015': int(country_dic['2015 Population']),
        '2010': int(country_dic['2010 Population']),
        '2000': int(country_dic['2000 Population']),
        '1990': int(country_dic['1990 Population']),
        '1980': int(country_dic['1980 Population']),
        '1970': (country_dic['1970 Population']),
    }
    lables = population_dic.keys()
    values = population_dic.values()
    return lables, values

def population_by_country(data,country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result
