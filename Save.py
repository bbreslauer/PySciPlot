# Functions for saving to files

import xml.dom.minidom


def writeProjectToFile(app, fileName):
    """
    Write the project to a file.

    Need to move this to its own class, and have separate methods for gathering
    each bit of data (waves, a wave, figures, a figure, etc)
    """

    # Create document
    dom = xml.dom.minidom.Document()

    # Create root project element
    p = dom.createElement("pysciplot")
    dom.appendChild(p)
    p.setAttribute("version", str(app._version))

    getWaves(app, dom)
    getTables(app, dom)
    getFigures(app, dom)

    fileHandle = open(fileName, "w")
    dom.writexml(fileHandle, indent='', addindent='  ', newl='\n')


# Get specific sets of data

def getWaves(app, dom, waveNames=[]):
    """
    Get waves and data and put them into the xml document.

    app is the pysciplot application.

    dom is the main dom object.
    
    waveNames is a list of waves to export.  If waveNames is empty, then
    get all the waves.
    """
    
    p = dom.firstChild

    # Create and add waves object
    waves = dom.createElement("waves")
    waves.setAttribute("uniqueNames", str(app.waves().uniqueNames()))
    p.appendChild(waves)

    # Now gather all the individual wave objects and add them to the waves object
    wavesList = []
    if len(waveNames) == 0:
        wavesList = app.waves().waves()
    else:
        for waveName in waveNames:
            wave = app.waves().getWaveByName(waveName)
            if wave:
                wavesList.append(wave)

    for wave in wavesList:
        getWave(app, dom, waves, wave)

def getWave(app, dom, waves, waveObj):
    """
    Convert a wave object into xml.

    app is the pysciplot application.

    dom is the main dom object.

    waves is the dom object for holding all the waves.

    waveObj is the wave object that we are converting.
    """

    wave = dom.createElement("wave")
    dataType = waveObj.dataType()
    wave.setAttribute("dataType", dataType)
    waves.appendChild(wave)

    name = dom.createElement("name")
    name.appendChild(dom.createTextNode(str(waveObj.name())))
    wave.appendChild(name)
    
    data = dom.createElement("data")
    wave.appendChild(data)

    dataList = waveObj.data()
    dataString = ""
    for element in dataList:
        if dataType == "String":
            dataString += "\'" + str(element) + "\'"
        else:
            dataString += str(element)
        dataString += " "

    data.appendChild(dom.createTextNode(str(dataString)))

def getTables(app, dom, tablesList=[]):
    """
    Get tables and put them into the xml document.  We only store
    the names of the waves in the table.

    app is the pysciplot application.

    dom is the main dom object.
    
    tablesList is a list of table objects to export.  If tablesList is
    empty, then get all the tables.
    """
    
    p = dom.firstChild

    # Create and add tables object to dom
    tables = dom.createElement("tables")
    p.appendChild(tables)

    if len(tablesList) == 0:
        # Look for tables in all the windows in the app's mdi area
        windows = app.ui.workspace.subWindowList()

        for window in windows:
            if type(window.widget()).__name__ == "DataTableView":
                tablesList.append(window.widget())

    for table in tablesList:
        getTable(app, dom, tables, table)

def getTable(app, dom, tables, tableObj):
    """
    Convert a table object into xml.

    app is the pysciplot application.

    dom is the main dom object.

    tables is the dom object for holding all the tables.

    tableObj is the table object that we are converting.
    """

    table = dom.createElement("table")
    tableName = dom.createElement("name")
    tableName.appendChild(dom.createTextNode(str(tableObj.name())))
    table.appendChild(tableName)

    for waveObj in tableObj.model().waves().waves():
        wave = dom.createElement("wave")
        wave.appendChild(dom.createTextNode(str(waveObj.name())))
        table.appendChild(wave)
    tables.appendChild(table)

def getFigures(app, dom, figuresList=[]):
    """
    Get figures and put them into the xml document.

    app is the pysciplot application.

    dom is the main dom object.

    figuresList is a list of figure objects to export.  If figuresList is
    empty, then get all the figures in the app.
    """

    p = dom.firstChild

    # Create and add figures object
    figures = dom.createElement("figures")
    p.appendChild(figures)

    # Now gather all the individual figure objects and add them
    if len(figuresList) == 0:
        # Gather all the figures in the app's Figures object
        figuresList = app.figures().figures()

    for figure in figuresList:
        getFigure(app, dom, figures, figure)

def getFigure(app, dom, figures, figureObj):
    """
    Convert a figure object into xml.

    app is the pysciplot application.

    dom is the main dom object.

    figures is the dom object for holding all the figures.

    figureObj is the figure object that we are converting.
    """

    figure = dom.createElement("figure")
    
    # Get all the figure properties
    for propName in figureObj.properties.keys():
        propValue = figureObj.get(propName)
        prop = dom.createElement(str(propName))
        prop.appendChild(dom.createTextNode(str(propValue)))
        figure.appendChild(prop)

    # Get the plots
    plots = dom.createElement("plots")
    figure.appendChild(plots)

    for plotObj in figureObj.plots():
        plot = dom.createElement("plot")
        plots.appendChild(plot)
        
        for propName in plotObj.properties.keys():
            propValue = plotObj.get(propName)
            prop = dom.createElement(str(propName))
            prop.appendChild(dom.createTextNode(str(propValue)))
            plot.appendChild(prop)

        # Get the traces
        traces = dom.createElement("traces")
        plot.appendChild(traces)

        for traceObj in plotObj.traces():
            trace = dom.createElement("trace")
            traces.appendChild(trace)

            xWave = dom.createElement("xWave")
            xWave.appendChild(dom.createTextNode(str(traceObj.getXName())))
            trace.appendChild(xWave)

            yWave = dom.createElement("yWave")
            yWave.appendChild(dom.createTextNode(str(traceObj.getYName())))
            trace.appendChild(yWave)

            for propName in traceObj.properties.keys():
                propValue = traceObj.get(propName)
                prop = dom.createElement(str(propName))
                prop.appendChild(dom.createTextNode(str(propValue)))
                trace.appendChild(prop)

    figures.appendChild(figure)



