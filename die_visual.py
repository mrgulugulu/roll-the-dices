from die import Die
import pygal

#创建一个D6
die = Die()

#掷几个骰子，将结果存在列表中
results = []
for i in range(1000):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []

for i in range(1, die.num_sides+1):
    frequency = results.count(i)#计算每个点数出现的次数,count()方法用来计数
    frequencies.append(frequency)

#对结果可视化
hist = pygal.Bar()

hist.title = 'Result of rolling one D6 1000 times'#主标题
hist.x_labels = ['1', '2', '3', '4', '5', '6']#X轴的标签
hist.x_title = 'Result'#X轴标题
hist.y_title = 'Frequency of Result'#Y轴标题

hist.add('D6', frequencies)#前者为数值的标签，后者为要传入的值
hist.render_to_file('die_visual.svg')
