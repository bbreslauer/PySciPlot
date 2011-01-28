# Functions for saving to files

import Util

from PyQt4.QtGui import QMdiArea

import xml.dom.minidom, os.path, pickle


def writeProjectToFile(app, fileName):
    """
    Write the project to a file.

    Need to move this to its own class, and have separate methods for gathering
    each bit of data (waves, a wave, figures, a figure, etc)
    """

    Util.debug(1, "Save", "Writing project to file")

    # Create document
    dom = xml.dom.minidom.Document()

    # Create root project element
    p = dom.createElement("pysciplot")
    dom.appendChild(p)
    p.setAttribute("version", str(app._version))

    appWindowList = app.ui.workspace.subWindowList(QMdiArea.StackingOrder)
    getStoredSettings(app, dom)
    getWaves(app, dom)
    getTables(app, dom, appWindowList)
    getFigures(app, dom, appWindowList)
    
    if os.path.isfile(fileName):
        with open(fileName, "w") as fileHandle:
            dom.writexml(fileHandle, indent='', addindent='  ', newl='\n')

    app.setCurrentProject(fileName)


# Get specific sets of data

def getStoredSettings(app, dom):
    """
    Get the stored settings dict.
    
    app is the pysciplot application.

    dom is the main dom object.
    """

    Util.debug(1, "Save", "Getting waves")

    p = dom.firstChild
    
    storedSettings = dom.createElement("storedSettings")
    storedSettings.appendChild(dom.createTextNode(str(pickle.dumps(app.storedSettings()))))
    p.appendChild(storedSettings)

def getWaves(app, dom, waveNames=[]):
    """
    Get waves and data and put them into the xml document.

    app is the pysciplot application.

    dom is the main dom object.
    
    waveNames is a list of waves to export.  If waveNames is empty, then
    get all the waves.
    """
    
    Util.debug(1, "Save", "Getting waves")

    p = dom.firstChild

    # Create and add waves object
    waves = dom.createElement("waves")
    waves.setAttribute("uniqueNames", str(app.waves().uniqueNames()))
    waves.appendChild(dom.createTextNode(str(pickle.dumps(app.waves()))))
    p.appendChild(waves)

def getTables(app, dom, appWindowList, tablesList=[]):
    """
    Get tables and put them into the xml document.  We only store
    the names of the waves in the table.

    app is the pysciplot application.

    dom is the main dom object.

    appWindowList is a list of the windows in the mdi area, so that we
    can determine the order of the windows.
    
    tablesList is a list of table objects to export.  If tablesList is
    empty, then get all the tables.
    """
    
    Util.debug(1, "Save", "Getting tables")

    p = dom.firstChild

    # Create and add tables object to dom
    tables = dom.createElement("tables")
    p.appendChild(tables)

    if len(tablesList) == 0:
        # Look for tables in all the windows in the app's mdi area
        windows = app.ui.workspace.subWindowList()

        for window in windows:
            if type(window).__name__ == "DataTableSubWindow":
                tablesList.append(window)

    for table in tablesList:
        getTable(app, dom, appWindowList, tables, table)

def getTable(app, dom, appWindowList, tables, tableObj):
    """
    Convert a table object into xml.

    app is the pysciplot application.

    dom is the main dom object.

    tables is the dom object for holding all the tables.

    tableObj is the table object that we are converting.
    """

    Util.debug(1, "Save", "Getting a table")

    table = dom.createElement("table")
    tableName = dom.createElement("name")
    tableName.appendChild(dom.createTextNode(str(tableObj.widget().name())))
    table.appendChild(tableName)

    # Get attributes of the window
    table.setAttribute("stackingOrder", str(appWindowList.index(tableObj)))
    table.setAttribute("windowState", str(int(tableObj.windowState())))
    table.setAttribute("width", str(tableObj.width()))
    table.setAttribute("height", str(tableObj.height()))
    table.setAttribute("xpos", str(tableObj.x()))
    table.setAttribute("ypos", str(tableObj.y()))

    for waveObj in tableObj.widget().model().waves().waves():
        wave = dom.createElement("wave")
        wave.appendChild(dom.createTextNode(str(waveObj.name())))
        table.appendChild(wave)
    tables.appendChild(table)

def getFigures(app, dom, appWindowList, figuresList=[]):
    """
    Get figures and put them into the xml document.

    app is the pysciplot application.

    dom is the main dom object.

    appWindowList is a list of the windows in the mdi area, so that we
    can determine the order of the windows.
    
    figuresList is a list of figure objects to export.  If figuresList is
    empty, then get all the figures in the app.
    """

    Util.debug(1, "Save", "Getting figures")

    p = dom.firstChild

    # Create and add figures object
    figures = dom.createElement("figures")
    p.appendChild(figures)

    # Now gather all the individual figure objects and add them
    if len(figuresList) == 0:
        # Gather all the figures in the app's Figures object
        figuresList = app.figures().figures()

    for figure in figuresList:
        getFigure(app, dom, appWindowList, figures, figure)


def getFigure(app, dom, appWindowList, figures, figureObj):
    Util.debug(1, "Save", "Getting a figure")

    figure = dom.createElement("figure")

    # Get attributes of the window
    figure.setAttribute("stackingOrder", str(appWindowList.index(figureObj._figureSubWindow)))
    figure.setAttribute("windowState", str(int(figureObj._figureSubWindow.windowState())))
    figure.setAttribute("width", str(figureObj._figureSubWindow.width()))
    figure.setAttribute("height", str(figureObj._figureSubWindow.height()))
    figure.setAttribute("xpos", str(figureObj._figureSubWindow.x()))
    figure.setAttribute("ypos", str(figureObj._figureSubWindow.y()))

    figure.appendChild(dom.createTextNode(str(pickle.dumps(figureObj))))

    figures.appendChild(figure)

