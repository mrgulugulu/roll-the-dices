from die import Die
import pygal

#创建2个D6
die_1 = Die()
die_2 = Die()

#掷几个骰子，将结果存在列表中
results = []
for i in range(10000):
    result = die_1.roll() + die_2.roll()#将两次的点数加起来
    results.append(result)

#分析结果
frequencies = []

max_result = die_1.num_sides + die_2.num_sides

for i in range(2, max_result+1):
    frequency = results.count(i)#计算每个点数出现的次数,count()方法用来计数
    frequencies.append(frequency)

#对结果可视化
hist = pygal.Bar()

hist.title = 'Result of rolling two D6 10000 times'#主标题
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']#X轴的标签
hist.x_title = 'Result'#X轴标题
hist.y_title = 'Frequency of Result'#Y轴标题

hist.add('D6 + D6', frequencies)#前者为数值的标签，后者为要传入的值
hist.render_to_file('dice_visual.svg')
