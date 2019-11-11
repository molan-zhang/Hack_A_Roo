from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import patches
import matplotlib
import numpy as np
import seaborn as sns
import os
sns.set_style("whitegrid")
num = '1'
map_dict={'1':[[0, 0], [0, 2], [0, 4], [0, 6], [0, 8], [0, 10],
               [0, 12], [0, 14], [0, 16], [0, 18], [0, 20], [2, 20],
               [4, 20], [6, 20], [8, 20], [10, 20], [12, 20], [14, 20],
               [16, 20], [18, 20], [20, 20], [22, 20], [24, 20], [26, 20],
               [28, 20], [30, 20], [32, 20], [34, 20], [36, 20], [38, 20],
               [40, 20], [42, 20], [44, 20], [46, 20], [48, 20], [50, 20],
               [52, 20], [54, 20], [56, 20], [58, 20], [60, 20]],
          '2':[[0, 0], [0, 2], [0, 4], [0, 6], [0, 8], [0, 10],
               [0, 12], [0, 14], [0, 16], [0, 18], [0, 20], [0, 22], [0, 24],
               [0, 26], [0, 28], [0, 30], [0, 32], [0, 34], [0, 36], [0, 38],
               [0, 40], [2, 40], [4, 40], [6, 40], [8, 40], [10, 40], [12, 40],
               [14, 40], [16, 40], [18, 40], [20, 40], [22, 40], [24, 40],
               [26, 40], [28, 40], [30, 40], [32, 40], [34, 40], [36, 40],
               [38, 40], [40, 40], [42, 40], [44, 40], [46, 40], [48, 40],
               [50, 40], [52, 40], [54, 40], [56, 40], [58, 40], [60, 40]],
          '3':[[0, 0], [0, 2], [0, 4], [0, 6], [0, 8], [0, 10], [0, 12],
               [0, 14], [0, 16], [0, 18], [0, 20], [0, 22], [0, 24], [0, 26],
               [0, 28], [0, 30], [0, 32], [0, 34], [0, 36], [0, 38], [0, 40],
               [0, 42], [0, 44], [0, 46], [0, 48], [0, 50], [0, 52], [0, 54],
               [0, 56], [0, 58], [0, 60], [2, 60], [4, 60], [6, 60], [8, 60],
               [10, 60], [12, 60], [14, 60], [16, 60], [18, 60], [20, 60],
               [22, 60], [24, 60], [26, 60], [28, 60], [30, 60], [32, 60],
               [34, 60], [36, 60], [38, 60], [40, 60], [42, 60], [44, 60],
               [46, 60], [48, 60], [50, 60], [52, 60], [54, 60], [56, 60],
               [58, 60], [60, 60]]
          }

obstacles = [[50,60],[50,40],[46,20],[54,22],[54,24],[54,26],[54,28],[54,30],[54,32],[34, 88],
             [8, 46], [30, 40], [50, 28], [36, 30], [28, 86], [20, 74],
             [12, 10], [40, 62], [44, 58], [34, 76], [50, 28], [8, 52],
             [24, 16], [40, 6], [24, 60], [10, 80], [18, 24], [30, 30],
             [54, 46]]
y = 0



# 创建画布，包含2个子图
fig = plt.figure()
ax = fig.add_subplot(111)


# 先绘制初始图形，每个子图包含1个正弦波和三个点的散点图

rx1 = 0
ry1 = 0
sca2 = ax.scatter(rx1,ry1,c='red',marker ='h',label = 'robot')
rect1 = patches.Rectangle((60,60), 10, 10, linewidth=0.3, edgecolor='g', facecolor='g',label = 'target_1')
ax.add_patch(rect1)
rect2 = patches.Rectangle((60,40), 10, 10, linewidth=0.3, edgecolor='m', facecolor='m',label = 'target_2')
ax.add_patch(rect2)
rect3 = patches.Rectangle((60,20), 10, 10, linewidth=0.3, edgecolor='y', facecolor='y',label = 'target_3')
ax.add_patch(rect3)
ax.scatter(obstacles[0][0],obstacles[0][1],c='black',label ='obstacles')
for i in range(1,len(obstacles)):
    ax.scatter(obstacles[i][0],obstacles[i][1],c='black')
plt.legend(loc=2,ncol=3)






def init():
    # 构造开始帧函数init

    # 改变散点图数据
    rx1 = 0
    ry1 = 0
    rdata = [rx1,ry1]
    sca2.set_offsets(rdata)
    label = 'timestep {0}'.format(0)
    ax.set_xlabel(label)
    return sca2,ax  # 注意返回值，我们要更新的就是这些数据

def animate(i):
    # 接着，构造自定义动画函数animate，用来更新每一帧上各个x对应的y坐标值，参数表示第i帧
    # plt.cla() 这个函数很有用，先记着它
    global y
    global map_dict
    rdata = [0,0]
    if i < len(map_dict[num]):
        rdata = map_dict[num][i]
        if rdata in obstacles :
            y = y + 2
            new_route = map_dict[num][i-1]
            map_dict[num].insert(i,new_route)
            rdata = new_route
            for j in range(i,len(map_dict[num])):
                map_dict[num][j][1] += 2
        sca2.set_offsets(rdata)
        print(map_dict[num][i])
    if y > 5 and i >= len(map_dict[num]):
        rdata = map_dict[num][len(map_dict[num])-1]
        y = y - 2
        new_route = [0,0]
        new_route[0] = map_dict[num][len(map_dict[num])-1][0]
        new_route[1] = map_dict[num][len(map_dict[num])-1][1] - 2
        map_dict[num].insert(i,new_route)
        sca2.set_offsets(rdata)
    label = 'timestep {0}'.format(i)
    ax.set_xlabel(label)
    return sca2,ax


# 接下来，我们调用FuncAnimation函数生成动画。参数说明：
# fig 进行动画绘制的figure
# func 自定义动画函数，即传入刚定义的函数animate
# frames 动画长度，一次循环包含的帧数
# init_func 自定义开始帧，即传入刚定义的函数init
# interval 更新频率，以ms计
# blit 选择更新所有点，还是仅更新产生变化的点。应选择True，但mac用户请选择False，否则无法显示动画
ani = animation.FuncAnimation(fig=fig,
                              func=animate,
                              frames=100,
                              init_func=init,
                              interval=1000,
                              blit=True)
plt.show()

