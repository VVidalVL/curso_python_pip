import matplotlib.pyplot as plt 


#def generate_bar_chart(labels, values):
    #labels = ['a', 'b', 'c']
    #values = [100, 200, 300]
    #fig, ax = plt.subplots()
    #ax.bar(labels, values)
    #plt.show()
    #plt.figure(1)

    #plt.figure(2)
    
def generate_pie_chart(labels, values):
    #labels = ['a', 'b', 'c']    
    #values = [10, 500, 200]
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%.2f%%')
    plt.show()


if __name__ == '__main__':
    
    #labels = ['a', 'b', 'c']
    #values = [100, 200, 300]
    generate_pie_chart()
    #generate_bar_chart(labels, values)