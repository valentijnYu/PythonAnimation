#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib as mpl
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
#mpl.rcParams['xtick.minor.bottom'] = 'False'
mpl.rcParams['xtick.top'] = 'True'
#mpl.rcParams['xtick.minor.top'] = 'False'
#mpl.rcParams['ytick.major.right'] = 'True'
mpl.rcParams['ytick.right'] = 'True'
mpl.rcParams['xtick.major.size'] = 12
mpl.rcParams['ytick.major.size'] = 12
mpl.rcParams['xtick.minor.size'] = 6
mpl.rcParams['ytick.minor.size'] = 6

df = pd.read_csv('PS_2022.06.28_02.59.13.csv',index_col=0, comment='#')
df = df[df['default_flag'] == 1].copy()

fps = 120

df['frame'] = (df['disc_year']-1989)*fps
for i in range(0,34): #years interval
    ID = df['frame'] == i*fps
    df.loc[ID,'frame'] = np.random.randint(i*fps, high=i*fps+fps, size=sum(ID))


IDt = df['discoverymethod'] == 'Transit'
IDi = df['discoverymethod'] == 'Imaging'
IDr = df['discoverymethod'] =='Radial Velocity'
IDa = df['discoverymethod'] =='Astrometry'

df['c'] = plt.rcParams['axes.prop_cycle'].by_key()['color'][0]+'ff'
df.loc[IDt,'c'] = plt.rcParams['axes.prop_cycle'].by_key()['color'][1]+'ff'
df.loc[IDi,'c'] = plt.rcParams['axes.prop_cycle'].by_key()['color'][2]+'ff'
df.loc[IDr,'c'] = plt.rcParams['axes.prop_cycle'].by_key()['color'][3]+'ff'
df.loc[IDa,'c'] = plt.rcParams['axes.prop_cycle'].by_key()['color'][4]+'ff'
#df['c'] = df['c'].apply(lambda x: hex)


# df['c'] = (219, 57, 64)
# df.loc[IDt,'c'] = (255, 206, 0)
# df.loc[IDi,'c'] = (9, 111, 153)
# df.loc[IDr,'c'] = (255, 118, 172)

df['ani_size'] = 0
df['alpha_c'] = df['c']
df['sy_dist_ly'] = df['sy_dist']*3.26156

df.sort_values('frame', axis=0, ascending=True, inplace=True)


figsizes = {480: (8.54, 4.8), 720: (8.54, 4.8), 1080: (19.2, 10.8)}
plt.rcParams['figure.dpi'] = 100
plt.rcParams['savefig.dpi'] = 100
# plt.rc('font',**{'family':'serif','size':28})
# plt.rcParams['font.family'] = 'OPPOSans'
plt.rc('font',**{'family':'OPPOSans','size':28,'weight':900})

#plt.rcParams["font.family"]  = 'HeitiSC'
#plt.rc('font',**{'family':'STHeiti Medium','size':28})


fig, ax = plt.subplots(figsize=figsizes[1080])



# plt.scatter(df['pl_orbper'],df['pl_rade'],alpha=0.5,c=df['color'])
#N = 50
#colors = np.random.rand(N)
#c = plt.cm.gist_rainbow(colors)

start_year = 1990
end_year =2022




fmin = df['frame'].min()
fmax = df['frame'].max()

# f = 1019

f = fmin
growth_rate = 10
ax.set_xlabel('轨道周期（天）\n Orbital Period (Days)')
# ylabel = ax.set_ylabel('与地球距离（光年）\n Distance relative to Earth (Lightyears)',labelpad=40)
# ax.set_ylabel('与地球距离（光年）\n Distance relative to Earth (Lightyears)')
plt.text(-0.12, 0.1, '与地球距离（光年）\n Distance relative to Earth (Lightyears)',
         transform=ax.transAxes,rotation=90,ha='center',c='white')

axis_color = 'white'

ax.tick_params(axis='x', colors=axis_color,which="both")
ax.tick_params(axis='y', colors=axis_color,which="both")

ax.tick_params(color=axis_color, labelcolor=axis_color,which="both")
for spine in ax.spines.values():
    spine.set_edgecolor(axis_color)

ax.yaxis.label.set_color(axis_color)
ax.xaxis.label.set_color(axis_color)


ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(0.3,3e5)
ax.set_ylim(7,10000)
ax.set_xticks([1,10,100,1000,10000])
ax.set_yticks([10,100,1000,10000,50000])
ax.get_xaxis().set_major_formatter(ScalarFormatter())
ax.get_yaxis().set_major_formatter(ScalarFormatter())
scat = ax.scatter(df['pl_orbper'],df['sy_dist_ly'],facecolors="None", edgecolors=df['c'],s=df['ani_size'],
          linewidth =2,alpha=0.7)
text1 = plt.text(1. - 0.16, 1. - 0.08, 'Exoplanet系外行星：', transform=ax.transAxes)
text2 = plt.text(0.34, 1.11, 'Year年：', transform=ax.transAxes)
text3 = plt.text(0.35, 1.11,'space')
text4 = plt.text(0.35, 1.11,'space')
text5 = plt.text(0.35, 1.11,'space')
text6 = plt.text(0.35, 1.11,'space')
text7 = plt.text(0.35, 1.11,'space')


def changeAlpha(color,limit,step):
    #bound = hex(limit)
    suffix = np.array([int(str(x).strip()[-2:],16) for x in color])

    ID = (suffix > limit)
#     if hex(int(color[1:],16))[-2:] >= bound:
    final = np.array(['#'+hex(int(value[1:], 16)-step)[2:] for value in color[ID]])
#     else:
#         final = color
    color[ID] = final
    return color

ax.set_xlim(2,10000)
ax.set_ylim(8,4000)

plt.subplots_adjust(left=0.2,right=0.95)

while f <= fmax+200: #end postpond to make sure last circle has enough time to grow

    scat.remove()
    text1.remove()
    text2.remove()
    text3.remove()
    text4.remove()
    text5.remove()
    text6.remove()
    text7.remove()
    scat = ax.scatter(df['pl_orbper'],df['sy_dist_ly'],facecolors="None", edgecolors=df['alpha_c'],s=df['ani_size'],
              linewidth =2)


    ID = df['frame'] <= f
    df.loc[ID,'ani_size'] += growth_rate


    ID_cut = df['ani_size']>df['pl_bmasse']
    df.loc[ID_cut,'ani_size'] = df[ID_cut]['pl_bmasse']

    df.loc[ID,'alpha_c'] = changeAlpha(df.loc[ID,'alpha_c'],120,10)





    exoNumber = (df['frame']<=f).sum()
    year = df[df['frame']<=f].iloc[-1]['disc_year']

    text1 = plt.text(0.35, 1.05, 'Exoplanets系外行星：%i'%exoNumber, transform=ax.transAxes,c='white')
    text2 = plt.text(0.35, 1.11, 'Year年：%i'%year, transform=ax.transAxes,c='white')

    tn = (df[df['frame']<=f]['discoverymethod'] == 'Transit').sum()
    text3 = plt.text(0.75, 0.93, 'Tansit凌日：%i'%tn, transform=ax.transAxes,c=df.loc[IDt,'c'][0],size=18)

    imagn = (df[df['frame']<=f]['discoverymethod'] == 'Imaging').sum()
    text4 = plt.text(0.75, 0.88, 'Imaging直接成像：%i'%imagn, transform=ax.transAxes,c=df.loc[IDi,'c'][0],size=18)

    rn = (df[df['frame']<=f]['discoverymethod'] == 'Radial Velocity').sum()
    text5 = plt.text(0.75, 0.83, 'Radial Velocity径向速度：%i'%rn, transform=ax.transAxes,c=df.loc[IDr,'c'][0],size=18)

    an = (df[df['frame']<=f]['discoverymethod'] == 'Astrometry').sum()
    text6 = plt.text(0.75, 0.78, 'Astrometry天体测量：%i'%an, transform=ax.transAxes,c=df.loc[IDa,'c'][0],size=18)

    on = (df[df['frame']<=f]['c'] == plt.rcParams['axes.prop_cycle'].by_key()['color'][0]+'ff').sum()
    text7 = plt.text(0.75, 0.73, 'Others其他：%i'%on, transform=ax.transAxes,c=plt.rcParams['axes.prop_cycle'].by_key()['color'][0]+'ff',size=18)



    if (f>1760)and(f<1760+3000):
        sub = (f-1760)
        ax.set_xlim(2-sub*0.0013/2,10000+sub*193.3/2)
        ax.set_ylim(8-sub*0.0018/2,4000+sub*30.6/2)

#     if (4000+sub*30.6)>=1e4:
#         ax.set_ylabel('与地球距离（光年）\n Distance relative to Earth (Lightyears)',labelpad=2)

    fig.savefig('seq_zoom/%i_figure.png'%f, transparent=True)

    f += 1


#fig.set_tight_layout(True)
