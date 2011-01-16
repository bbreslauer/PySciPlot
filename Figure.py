from PyQt4.QtGui import QAction, QColor, QApplication

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure as MPLFigure
from matplotlib.font_manager import FontProperties
from mpl_toolkits.axes_grid.axislines import Axes
from mpl_toolkits.axes_grid1 import Grid

import Util, Property
from FigureObject import *
from Waves import Waves
from Wave import Wave
from Plot import Plot
from gui.SubWindows import FigureSubWindow

class Figure(FigureObject):
    """
    Encapsulates all data for a figure, including all the plots within it.

    plotNum is 0-based.
    """

    def __init__(self, windowTitle=""):
        
        Util.debug(2, "Figure.init", "Creating figure")

        # Properties
        self.properties = {  
                            'windowTitle':        Property.String(''),
                            'title':              Property.String(''),
                            'titleFont':          Property.TextOptions({'size': 20, 'rotation': 'horizontal', 'verticalalignment': 'top'}),
                            'rows':               Property.Integer(1),
                            'columns':            Property.Integer(1),
                            'axesPadding':        Property.Float(0.5),
                            'backgroundColor':    Property.Color(QColor(255,255,255,255)),
                            'linkPlotAxes':       Property.Boolean(False),
                          }

        self._app = QApplication.instance().window

        # Graphical stuff
        self._figure = MPLFigure()
        self._canvas = FigureCanvas(self._figure)
        self._figureSubWindow = FigureSubWindow(self._app.ui.workspace)
        self._figureSubWindow.setWidget(self._canvas)
        self._app.ui.workspace.addSubWindow(self._figureSubWindow)
        self._canvas.setParent(self._figureSubWindow)
        self.showFigure()
        
        FigureObject.__init__(self, self.properties)

        self.set('windowTitle', windowTitle)

        self._plots = []
        self.extendPlots(0)
        
        self.mplHandles = {}
        
        self.refresh()

        Util.debug(1, "Figure.init", "Created figure " + self.get('windowTitle'))

    def __str__(self):
        return "name: %s, rows: %s, columns: %s" % (self.get('windowTitle'), self.get('rows'), self.get('columns'))

    def __reduce__(self):
        return tuple([self.__class__, tuple(), tuple([self.properties, self.plots()])])

    def __setstate__(self, state):
        properties = state[0]
        plots = state[1]

        self.setMultiple(properties)
        self._plots = []
        
        for plot in plots:
            self.addPlot(plot)

    def mplFigure(self):
        return self._figure
    
    def plots(self):
        return self._plots

    def numPlots(self):
        return self.get('rows') * self.get('columns')

    def getPlot(self, plotNum):
        if plotNum < self.numPlots():
            return self.plots()[plotNum]
        return None

    def addPlot(self, plot):
        self.plots().append(plot)
        self.refreshPlots()

    def extendPlots(self, maxPlotNum=-1):
        """
        If maxPlotNum < 0, then it will be equal to numPlots() - 1.
        """
        if maxPlotNum < 0:
            maxPlotNum = self.numPlots() - 1

        Util.debug(2, "Figure.extendPlots", "Extending figure to contain " + str(maxPlotNum + 1) + " plots")
        for i in range(len(self.plots()), maxPlotNum + 1):
            plot = Plot()
            self.plots().append(plot)


    #################################
    # Handlers for when a property is modified
    #################################

    def update_windowTitle(self):
        Util.debug(3, "Figure.update_windowTitle", "")
        self._figureSubWindow.setWindowTitle(self.getMpl('windowTitle'))

    def update_title(self):
        Util.debug(3, "Figure.update_title", "")
        try:
            self.mplFigure().texts.remove(self.mplHandles['title'])
        except:
            pass

        self.mplHandles['title'] = self.mplFigure().suptitle(str(self.getMpl('title')), **(self.getMpl('titleFont')))
        self.redraw()

    def update_titleFont(self):
        Util.debug(3, "Figure.update_titleFont", "")
        self.update_title()

    def update_rows(self):
        Util.debug(3, "Figure.update_rows", "")
        self.refreshPlots()

    def update_columns(self):
        Util.debug(3, "Figure.update_columns", "")
        self.refreshPlots()

    def update_linkPlotAxes(self):
        Util.debug(3, "Figure.update_linkPlotAxes", "")
        self.refreshPlots()
    
    def update_axesPadding(self):
        Util.debug(3, "Figure.update_axesPadding", "")
        if self.getMpl('linkPlotAxes'):
            self.grid.set_axes_pad(self.getMpl('axesPadding'))
        else:
            self.mplFigure().subplots_adjust(wspace=self.getMpl('axesPadding'), hspace=self.getMpl('axesPadding'))

    def update_backgroundColor(self):
        Util.debug(3, "Figure.update_backgroundColor", "")
        self.mplFigure().set_facecolor(self.getMpl('backgroundColor'))
        self.redraw()
        


    def refreshPlots(self):
        Util.debug(3, "Figure.refreshPlots", "")
        # Remove old axes
        for plot in self.plots():
            try:
                self.mplFigure().delaxes(plot.axes())
            except:
                pass

        # Create any new plots that might be necessary
        self.extendPlots()

        # Prepare the figure with a grid for the subplots to go into
        if self.getMpl('linkPlotAxes'):
            self.grid = Grid(self.mplFigure(), 111, nrows_ncols = (self.getMpl('rows'), self.getMpl('columns')), axes_pad=self.getMpl('axesPadding'), share_x=False, share_y=False)
        else:
            self.mplFigure().subplots_adjust(wspace=self.getMpl('axesPadding'), hspace=self.getMpl('axesPadding'))

        # Create the subplots and send the axes to the Plot objects
        for plotNum in range(0, self.numPlots()):
            if self.getMpl('linkPlotAxes'):
                self.getPlot(plotNum).setAxes(self.grid[plotNum])
            else:
                self.getPlot(plotNum).setAxes(self.mplFigure().add_subplot(self.getMpl('rows'), self.getMpl('columns'), plotNum + 1))

        # Finally, redraw the canvas to show all the plots
        self.redraw()

    def redraw(self):
        Util.debug(3, "Figure.redraw", "Drawing canvas")
        self._canvas.draw()


    def refresh(self):
        self.refreshPlots()
        self.update_backgroundColor()
        self.update_title()
        self.update_windowTitle()


    def showFigure(self):
        self._figureSubWindow.show()

    def hideFigure(self):
        self._figureSubWindow.hide()

#    def createRightClickActions(self):
#
#        def createEditPlotDialog():
#            self._app._windows["EditPlotDialog"].show()
#            pass
#
#        editPlotAction = QAction("Edit Plot", self._figureSubWindow)
#        editPlotAction.triggered.connect(createEditPlotDialog)
#        self._figureSubWindow.setContextMenuPolicy(Qt.ActionsContextMenu)
#        self._figureSubWindow.insertAction(QAction(self._figureSubWindow), editPlotAction)



