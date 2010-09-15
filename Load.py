# Functions for loading from files

import xml.dom.minidom

from PyQt4.QtCore import Qt

from Wave import Wave
from Figure import Figure
from Plot import Plot

def loadProjectFromFile(app, fileName):
    """
    Load the project from a file.

    Waves must be imported before anything else. Otherwise, the waves
    might not exist and the other stuff would error out.
    """

    dom = xml.dom.minidom.parse(fileName)
    
    # root project element
    p = dom.documentElement

    child = p.firstChild
    while child is not None:
        if child.nodeType is xml.dom.minidom.Node.ELEMENT_NODE:
            if child.nodeName == "waves":
                loadWaves(app, child)
            elif child.nodeName == "tables":
                loadTables(app, child)
            elif child.nodeName == "figures":
                loadFigures(app, child)

        # Move on to next child
        child = child.nextSibling
    



def loadWaves(app, waves):
    """
    Load given waves into the application.
    """
    
    waveList = waves.getElementsByTagName("wave")
    
    for wave in waveList:
        dataType = str(wave.attributes["dataType"].value.strip())

        # Get wave from xml
        child = wave.firstChild
        while child is not None:
            if child.nodeType is child.ELEMENT_NODE:
                if child.nodeName == "name":
                    name = str(child.firstChild.data.strip())
                elif child.nodeName == "data":
                    data = child.firstChild.data.strip()

            # Move on to next child
            child = child.nextSibling

        if dataType == "Integer":
            dataList = map(int, data.split())
        elif dataType == "Decimal":
            dataList = map(float, data.split())
        elif dataType == "String":
            dataList = map(lambda x: x.decode('base64_codec'), map(str, data.split()))
        
        # Load wave into application
        app.waves().addWave(Wave(name, dataType, dataList))
        





def loadTables(app, tables):
    """
    Load given tables into the application.
    """

    tableList = tables.getElementsByTagName("table")

    for table in tableList:
        tableAttrs = {} # QT attributes
        waveNames = []

        # Get attributes for the table
        for attrName in table.attributes.keys():
            tableAttrs[attrName] = int(table.attributes[attrName].value.strip())

        # Get table from xml
        child = table.firstChild
        while child is not None:
            if child.nodeType is child.ELEMENT_NODE:
                if child.nodeName == "name":
                    name = str(child.firstChild.data.strip())
                elif child.nodeName == "wave":
                    waveNames.append(str(child.firstChild.data.strip()))

            # Move on to next child
            child = child.nextSibling

        waves = map(app.waves().getWaveByName, waveNames)
        
        # Load table into application
        tableWindow = app.createTable(waves, name)

        # Reset QT widget values
        tableWindow.setWindowState(Qt.WindowState(tableAttrs["windowState"]))
        tableWindow.resize(tableAttrs["width"], tableAttrs["height"])
        tableWindow.move(tableAttrs["xpos"], tableAttrs["ypos"])




def loadFigures(app, figures):
    """
    Load given figures into the application.
    """

    figureList = figures.getElementsByTagName("figure")

    for figure in figureList:
        figureAttrs = {} # QT attributes
        figureProps = {} # internal figure properties
        plots = []

        # Get attributes for the figure
        for attrName in figure.attributes.keys():
            figureAttrs[attrName] = int(figure.attributes[attrName].value.strip())

        # Get figure from xml
        child = figure.firstChild
        while child is not None:
            if child.nodeType is child.ELEMENT_NODE:
                if child.nodeName == "plots":
                    plots = loadPlots(child)
                else:
                    figureProps[child.nodeName] = str(child.firstChild.data.strip())

            # Move on to next child
            child = child.nextSibling

        # Load figure into application
        figureObj = Figure(app, "NoName")
        actualFigureProps = figureObj.properties.keys()
        for (key, value) in figureProps.items():
            if key in actualFigureProps:
                figureObj.set_(key, figureObj.properties[key]["type"](value))

        for plot in plots:
            plot.set_("figure", figureObj)
            figureObj.replacePlot(plot.get("plotNum"), plot)

        figureWindow = app.figures().addFigure(figureObj).get("figureSubWindow")

        # Reset QT widget values
        figureWindow.setWindowState(Qt.WindowState(figureAttrs["windowState"]))
        figureWindow.resize(figureAttrs["width"], figureAttrs["height"])
        figureWindow.move(figureAttrs["xpos"], figureAttrs["ypos"])




def loadPlots(plots):
    """
    Load given plots into the application.
    """

    plotList = plots.getElementsByTagName("plot")
    plotsObjList = []

    for plot in plotList:
        plotProps = {} # internal plot properties
        traces = []

        # Get plot from xml
        child = plot.firstChild
        while child is not None:
            if child.nodeType is child.ELEMENT_NODE:
                if child.nodeName == "traces":
                    traces = loadTraces(child)
                else:
                    plotProps[child.nodeName] = str(child.firstChild.data.strip())

            # Move on to next child
            child = child.nextSibling

        # Create plot
        plotObj = Plot(None, plotProps["plotNum"])
        actualPlotProps = plotObj.properties.keys()
        for (key, value) in plotProps.items():
            if key in actualPlotProps:
                plotObj.set_(key, plotObj.properties[key]["type"](value))

        for trace in traces:
            plotObj.addTrace(trace)

        plotsObjList.append(plotObj)

    return plotsObjList



def loadTraces(traces):
    return []








