import matplotlib as mpl
import color_constants as cc
from cycler import cycler

def mympl(backround_color='white',
          font_family="serif",
          vertical=True,
          horizontal=False):
    ''' Default rcparams'''


    print(mpl.rcParams.keys())
    mpl.rcParams['axes.spines.right'] = False
    mpl.rcParams['axes.spines.left'] = False
    mpl.rcParams['axes.spines.top'] = False
    mpl.rcParams['axes.spines.bottom'] = True
    mpl.rcParams['axes.titlelocation'] = 'left'

    mpl.rcParams['axes.titlelocation'] = 'left'
    mpl.rcParams['axes.titleweight'] = 'bold'
    mpl.rcParams['axes.titlepad'] = 6.0
    mpl.rcParams['axes.titlesize'] = 22

    mpl.rcParams['axes.grid'] = True
    mpl.rcParams['grid.color'] = cc.GRID_COLOR
    mpl.rcParams['grid.alpha'] = .6
    mpl.rcParams['figure.facecolor'] = backround_color
    mpl.rcParams['figure.figsize'] = [10, 8]
    mpl.rcParams["axes.facecolor"] = backround_color
    mpl.rcParams["font.family"] = font_family
    mpl.rcParams['axes.prop_cycle'] = cycler(color=cc.BAR_COLORS)
    mpl.rcParams['lines.linewidth'] = 2.8
    mpl.rcParams['grid.linewidth'] =  1.1


    mpl.rcParams['xtick.labelsize'] = 16
    mpl.rcParams['ytick.labelsize'] = 16

    if vertical:
        mpl.rcParams['axes.grid.axis'] = 'y'
        mpl.rcParams['ytick.major.pad'] = -21

        mpl.rcParams['ytick.alignment'] = 'bottom'
        mpl.rcParams['ytick.labelright'] = True
        mpl.rcParams['ytick.labelleft'] = False
        mpl.rcParams['ytick.left'] =  True




    elif horizontal:
        pass
    else:
        pass



# @mpl.rc_context({'lines.linewidth': 3, 'lines.linestyle': '-'})
# def plotting_function():
#     plt.plot(data)
#
# plotting_function()