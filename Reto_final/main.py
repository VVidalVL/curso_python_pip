import Grafica_poblacion
import read_csv
import charts

def run():
    data = read_csv.read_csv('./Reto_final/data1.csv')
    data = list(filter(lambda ittem: ittem['Continent']== 'South America', data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    porcentages =  list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, porcentages)

if __name__ == '__main__':
    run()