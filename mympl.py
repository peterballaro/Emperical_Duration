import matplotlib as mpl
import color_constants as cc

def mympl(backround_color='white', font_family="serif"):
    ''' Default rcparams'''



    mpl.rcParams['axes.spines.right'] = False
    mpl.rcParams['axes.spines.left'] = False
    mpl.rcParams['axes.spines.top'] = False
    mpl.rcParams['axes.spines.bottom'] = True
    mpl.rcParams['figure.facecolor'] = backround_color
    mpl.rcParams["axes.facecolor"] = backround_color
    mpl.rcParams["font.family"] = font_family


    #mpl.rcParams['lines.linewidth'] = 2
    #mpl.rcParams['lines.linestyle'] = '--'