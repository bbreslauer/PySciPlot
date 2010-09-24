# Functions for loading from files

import Util

import xml.dom.minidom

from PyQt4.QtCore import Qt

from Wave import Wave
from Figure import Figure
from Plot import Plot
from Trace import Trace

def loadProjectFromFile(app, fileName):
    """
    Load the project from a file.

    Waves must be imported before anything else. Otherwise, the waves
    might not exist and the other stuff would error out.
    """

    Util.debug(1, "Load", "Loading project from file")

    dom = xml.dom.minidom.parse(fileName)
    
    # root project element
    p = dom.documentElement

    # Load waves first
    child = p.firstChild
    while child is not None:
        if child.nodeType is xml.dom.minidom.Node.ELEMENT_NODE:
            if child.nodeName == "waves":
                loadWaves(app, child)

        # Move on to next child
        child = child.nextSibling

    # Now load tables and figures.  It doesn't matter which
    # is loaded first.
    stackingOrder = []
    child = p.firstChild
    while child is not None:
        if child.nodeType is xml.dom.minidom.Node.ELEMENT_NODE:
            if child.nodeName == "tables":
                loadTables(app, child, stackingOrder)
            elif child.nodeName == "figures":
                loadFigures(app, child, stackingOrder)

        # Move on to next child
        child = child.nextSibling
    
    # Order windows according to stackingOrder
    topWindow = None
    while stackingOrder:
        window = stackingOrder.pop(0)
        if window is not None:
            window.raise_()
            topWindow = window

    # Focus the top window
    if topWindow is not None:
        topWindow.setFocus(Qt.OtherFocusReason)

    app.setCurrentProject(fileName)

def loadWaves(app, waves):
    """
    Load given waves into the application.
    """
    
    Util.debug(1, "Load", "Loading waves from file")

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

def loadTables(app, tables, stackingOrder):
    """
    Load given tables into the application.
    """

    Util.debug(1, "Load", "Loading tables from file")

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

        # Add to stackingOrder
        if tableAttrs["stackingOrder"] >= len(stackingOrder):
            stackingOrder.extend([None] * (tableAttrs["stackingOrder"] - len(stackingOrder) + 1))
        stackingOrder[tableAttrs["stackingOrder"]] = tableWindow

def loadFigures(app, figures, stackingOrder):
    """
    Load given figures into the application.
    """
    
    Util.debug(1, "Load", "Loading figures from file")

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
                Util.debug(3, "Load.loadFigures", "Loading " + str(child.nodeName))
                if child.nodeName == "plots":
                    plots = loadPlots(app, child)
                else:
                    figureProps[child.nodeName] = str(child.firstChild.data.strip())

            # Move on to next child
            child = child.nextSibling

        # Load figure into application
        figureObj = Figure(app, "NoName")
        actualFigureProps = figureObj.properties.keys()
        for (key, value) in figureProps.items():
            if key in actualFigureProps:
                figureObj.set_(key, value)

        for plot in plots:
            plot.set_("figure", figureObj)
            figureObj.replacePlot(plot.get("plotNum"), plot)

        figureWindow = app.figures().addFigure(figureObj).get("figureSubWindow")

        # Reset QT widget values
        figureWindow.setWindowState(Qt.WindowState(figureAttrs["windowState"]))
        figureWindow.resize(figureAttrs["width"], figureAttrs["height"])
        figureWindow.move(figureAttrs["xpos"], figureAttrs["ypos"])

        # Add to stackingOrder
        if figureAttrs["stackingOrder"] >= len(stackingOrder):
            stackingOrder.extend([None] * (figureAttrs["stackingOrder"] - len(stackingOrder) + 1))
        stackingOrder[figureAttrs["stackingOrder"]] = figureWindow

        # Refresh figure
        #figureObj.refresh()

def loadPlots(app, plots):
    """
    Convert plots in xml to plot objects.
    """

    Util.debug(1, "Load", "Loading plots from file")

    plotList = plots.getElementsByTagName("plot")
    plotsObjList = []

    for plot in plotList:
        plotProps = {} # internal plot properties
        traces = []

        # Get plot from xml
        child = plot.firstChild
        while child is not None:
            if child.nodeType is child.ELEMENT_NODE:
                Util.debug(3, "Load.loadPlots", "Loading " + str(child.nodeName) + "=" + str(child.firstChild.data.strip()))
                if child.nodeName == "traces":
                    traces = loadTraces(app, child)
                else:
                    plotProps[child.nodeName] = str(child.firstChild.data.strip())

            # Move on to next child
            child = child.nextSibling

        # Create plot
        plotObj = Plot(None, plotProps["plotNum"])
        actualPlotProps = plotObj.properties.keys()
        for (key, value) in plotProps.items():
            if key in actualPlotProps:
                plotObj.set_(key, value)

        for trace in traces:
            plotObj.addTrace(trace)

        plotsObjList.append(plotObj)

    return plotsObjList

def loadTraces(app, traces):
    """
    Convert traces in xml to trace objects.
    """

    Util.debug(1, "Load", "Loading traces from file")

    traceList = traces.getElementsByTagName("trace")
    tracesObjList = []

    for trace in traceList:
        traceProps = {} # internal trace properties
        xWave = ""
        yWave = ""

        # Get trace from xml
        child = trace.firstChild
        while child is not None:
            if child.nodeType is child.ELEMENT_NODE:
                Util.debug(3, "Load.loadTraces", "Loading " + str(child.nodeName))
                if child.nodeName == "xWave":
                    xWave = app.waves().getWaveByName(str(child.firstChild.data.strip()))
                elif child.nodeName == "yWave":
                    yWave = app.waves().getWaveByName(str(child.firstChild.data.strip()))
                else:
                    traceProps[child.nodeName] = str(child.firstChild.data.strip())

            # Move on to next child
            child = child.nextSibling

        # Create trace
        traceObj = Trace(xWave, yWave)
        actualtraceProps = traceObj.properties.keys()
        for (key, value) in traceProps.items():
            if key in actualtraceProps:
                traceObj.set_(key, value)

        tracesObjList.append(traceObj)

    return tracesObjList








