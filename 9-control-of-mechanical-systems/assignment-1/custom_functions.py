import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton

notes = []

def plot(*args, scalex=True, scaley=True, data=None, **kwargs):
    """Wrapper for the standard Matplotlib 'plot' command. 
    
    This is done to allow for the addition of data tips. By
    LEFT clicking in the plot window, a data tip is placed to
    the north east of the point. If you right click, the data
    tip will be placed to the south west. Points can be erased
    by double clicking.
    """
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    line = ax.plot(
        *args, scalex=scalex, scaley=scaley,
        **({"data": data} if data is not None else {}), **kwargs)
    
    def mouse_click(event):
        try:
            if event.dblclick:
                for note in notes:
                    try:
                        note.remove()
                    except:
                        pass
            elif event.button is MouseButton.RIGHT:
                offset = 20
                xdisplay, ydisplay = ax.transData.transform((event.xdata, event.ydata))
                bbox = dict(boxstyle="round", fc="0.8")
                arrowprops = dict(
                    arrowstyle="->",
                    connectionstyle="angle,angleA=0,angleB=45,rad=10")
                notes.append(ax.annotate(f'({event.xdata:.2f}, {event.ydata:.2f})',
                            (xdisplay, ydisplay), xytext=(0.5*offset, offset),
                            xycoords='figure pixels',
                            textcoords='offset points',
                            bbox=bbox, arrowprops=arrowprops))
            # elif event.button is MouseButton.RIGHT:
            #     offset = 25
            #     xdisplay, ydisplay = ax.transData.transform((event.xdata, event.ydata))
            #     bbox = dict(boxstyle="round", fc="0.8")
            #     arrowprops = dict(
            #         arrowstyle="->",
            #         connectionstyle="angle,angleA=0,angleB=45,rad=10")
            #     notes.append(ax.annotate(f'({event.xdata:.2f}, {event.ydata:.2f})',
            #                 (xdisplay, ydisplay), xytext=(-2*offset, -offset),
            #                 xycoords='figure pixels',
            #                 textcoords='offset points',
            #                 bbox=bbox, arrowprops=arrowprops))
        except:
            pass
    fig.canvas.mpl_connect('button_press_event', mouse_click)
    return line

def scalar_times_list(scalar=1, data_list=[]) -> list:
    """Multiplies each value in list by the scalar
    
    args:
        scalar: number, value to multiply list by
        data_list: list[number], list of int or floats
    
    returns:
        list[nubmer]: original list scaled by the scalar factor
    """
    return [scalar * x for x in data_list]
