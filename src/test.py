import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
from matplotlib.collections import PatchCollection
import matplotlib.cm as pcm
import numpy as np

numring = 2
pitch = 1
xcoord =[]
ycoord =[]
hcoord = []
vcoord = []
for i in range(1,2*numring):
    if (i <= numring):
        temp = numring + i -1
    else:
        temp = 3*numring - i - 1
    for j in range(1,temp+1):
        xcoord.append(i)
        ycoord.append(j)
for i in range(len(xcoord)):
    hcoord.append(np.abs((xcoord[i]-numring)*2*np.sin(np.radians(60))*pitch*np.cos(np.radians(60))) + (ycoord[i]-1)*2*np.sin(np.radians(60))*pitch)
    vcoord.append((xcoord[i]-numring)*2*np.sin(np.radians(60))*pitch*np.sin(np.radians(60)))

values = [1,2,3,4,5,6,7]

colors = []
colormax = 1
valuesave = sum(values)/len(values)
valuesmax = max(values)
for i in range(len(values)):
    colors.append(((values[i]/valuesmax*colormax)))
    print((values[i]/valuesmax*colormax))

#coord = [[0,0,0],[0,1,-1],[-1,1,0],[-1,0,1],[0,-1,1],[1,-1,0],[1,0,-1]]
# 
labels = [['yes'],['no'],['yes'],['no'],['yes'],['no'],['no']]

# Horizontal cartesian coords
# hcoord = [c[0] for c in coord]

# Vertical cartersian coords
# vcoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) /3. for c in coord]

fig, ax = plt.subplots(1)
ax.set_aspect('equal')
patches = []
# Add some coloured hexagons
for x, y, c, l in zip(hcoord, vcoord, colors, labels):
    color = c  # matplotlib understands lower case words for colours
    # hex = RegularPolygon((x, y), numVertices=6, radius=pitch, 
    #                      orientation=np.radians(0), 
    #                      facecolor=[color,color,color], alpha=0.2, edgecolor='k')
    hex = RegularPolygon((x, y), numVertices=6, radius=pitch,orientation=np.radians(0))
    #ax.add_patch(hex)
    patches.append(hex)
    # Also add a text label
    #ax.text(x, y+0.2, l[0], ha='center', va='center', size=20)
colors = [["Green"],["Blue"],["Green"],["Green"],["Red"],["Green"],["Green"]]
# Also add scatter points in hexagon centres
ax.scatter(hcoord, vcoord, c=[c[0].lower() for c in colors], alpha=0.5)
p = PatchCollection(patches,cmap=pcm.jet,alpha=0.3,edgecolor="k",linewidth=0.5)
p.set_array(np.array(values))
ax.add_collection(p)
plt.colorbar(p,shrink=0.72,extend="neither",extendfrac=0.0,format="$%.2f$")
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# tt = np.linspace(0,1,100)*2*np.pi
# xx = np.sin(tt)
# clrs_rgb = [(255,255,0), (0,1,0),(0,0,1)] 
# clrs_rgba = [(1,0,0,0.2), (0,1,0,0.5),(0,0,1,0.7)] 
# clrs = ['c', 'tab:orange', 'forestgreen']
# # グラフ表示
# fig, ax = plt.subplots(1,3,figsize=(16,4))
# for i in range(len(clrs)):
#     ax[i].plot(tt, xx, label='RGB='+str(clrs_rgb[i]), color=clrs_rgb[i]) # グラフ
#     ax[i].plot(tt, xx*1.5, label='RGBA='+str(clrs_rgba[i]), color=clrs_rgba[i]) # グラフ    ax[i].legend() # 凡例
#     ax[i].legend() # 凡例