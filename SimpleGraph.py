import matplotlib.pyplot as plt
#绘制点的连线
# x=[1,2,3]
# y=[4,5,6]
# x1=[3,5,2]
# y1=[8,5,6]
# plt.plot(x,y,label='line1')
# plt.plot(x1,y1,label='line2')

#绘制直方图,如果画两个，如果有x点重合，y大的覆盖y小的
# x=[2,3,4,5,8]
# y=[8,5,3,4,1]
# x2=[1,3,4,6,7]
# y2=[4,5,6,7,3]
# plt.bar(x,y,label='bar1',color='crimson')#label是左上角的标识
# plt.bar(x2,y2,label='bar2',color='deepskyblue')#颜色cyan,orange,darkorange,lime,deepskyblue
#                                      #fuchsia,crimson

#绘制histogram,这是描述分布的图
# ages=[23,1,34,54,65,7,6,76,76,4,55,34,23,43,23,22,12,12,34]
# bin=[0,10,20,30,40,50,60,70]#x轴上的一段一段的范围，y是位于[10,20]之间的ages的数量
# plt.hist(ages,bin)

#scatter graph散点图
# x=[2,3,6,4,3,4]
# y=[4,5,6,7,8,3]
# plt.scatter(x,y,marker='*',s=5)#s是点的大小，marker:"o","s"

#stack plots
# days=[1,2,3,4,5]
# work=[3,4,6,7,8]
# eating=[3,4,5,2,3]
# playing=[2,3,4,6,2]
# plt.plot([],[],label='work',color='orange',linewidth=5)
# plt.plot([],[],label='eating',color='lime',linewidth=5)
# plt.plot([],[],label='playing',color='deepskyblue',linewidth=5)
# plt.stackplot(days,work,eating,playing,colors=['orange','lime','deepskyblue'])

#pie charts
# slices=[4,5,6,3]
# activities=['eating','sleeping','working','playing']
# cols=['r','lime','c','deepskyblue']
# plt.pie(slices,labels=activities,colors=cols,
#         startangle=90,shadow=True,explode=(0,0.1,0,0),
#         autopct='%1.1f%%')

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("this is title\nthis is next line")
plt.legend();
plt.show()
