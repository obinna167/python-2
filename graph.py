import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

pop_ = {'Male':128, 'Female':272}
a = {'borehole':226, 'vendors':131, 'tap':43}
c = {'Borehole':156, 'Well':201, 'Tap':29, 'Vendor':11}
d = {'Borehole':221, 'Tap':43, 'Vendor':107, 'Sachet Water':29}
e = {'Very close':54, 'Close':113, 'Moderate':198, 'Far':35,}
f = {'foot':382, 'vehicle':18}
g = {'Gallon':371, 'Drum':8, 'Tank':21}
h = {'Sachet water':326, 'Indifference':41, 'Others':33}
i = {'High':248, ' Not sure':78, 'Low':73}
j = {'Low':291, 'High':77, 'Not sure':32}
k = {'Low':209, 'Not sure':153, 'High':38}


x_axis = pop_.keys()
y_axis = pop_.values()

# 'blue', 'yellow', 706233, 820300,E36414, 765827, 5F0F40, #5F8670
color = ['#E36414', '#5F0F40']
explode = [0.019, 0.01]
pie_edge = {'edgecolor':'black', 'linewidth': 0.6}

plt.figure(figsize=(8, 8))

plt.pie(y_axis, labeldistance=0.5, startangle=270, colors=color, explode=explode, shadow=False, wedgeprops=pie_edge, autopct='%1.1f%%')

legend_label = x_axis

plt.legend(edgecolor='black', title='GENDER', loc='best', bbox_to_anchor=(0.7, 0.9), labels=legend_label)

path = 'C:/Users/DELL/OneDrive/Desktop/GRAPH/Graph_Output/1a_graph.png'

# plt.savefig(path)
plt.show()