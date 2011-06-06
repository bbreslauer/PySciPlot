# Copyright (C) 2010-2011 Ben Breslauer
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Functions for loading from files
import Util

import xml.dom.minidom, os.path, pickle

from PyQt4.QtCore import Qt

from Wave import Wave
from Figure import Figure
from Plot import Plot
from WavePair import *

def loadProjectFromFile(app, fileName):
    """
    Load the project from a file.

    Waves must be imported before anything else. Otherwise, the waves
    might not exist and the other stuff would error out.
    """

    Util.debug(1, "Load", "Loading project from file")
    
    if os.path.isfile(fileName):
        dom = xml.dom.minidom.parse(fileName)
    else:
        return False
    
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

    # Now load tables, figures, and stored settings.
    # It doesn't matter which is loaded first.
    stackingOrder = []
    child = p.firstChild
    while child is not None:
        if child.nodeType is xml.dom.minidom.Node.ELEMENT_NODE:
            if child.nodeName == "tables":
                loadTables(app, child, stackingOrder)
            elif child.nodeName == "figures":
                loadFigures(app, child, stackingOrder)
            elif child.nodeName == "storedSettings":
                loadStoredSettings(app, child)

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
    wavesObj = pickle.loads(str(waves.firstChild.data.strip()))
    try:
        waves = wavesObj.wavesInsertOrder()
    except:
        # This is for older versions (before commit 90f4d06) which don't have
        # an explicit order in the waves object.
        #
        # This can be safely deleted before release, because it only affects
        # saved projects that I have done.
        waves = wavesObj.waves().values()
    for wave in waves:
        app.waves().addWave(wave)

def loadStoredSettings(app, storedSettings):
    """
    Load stored settings into the application.
    """
    Util.debug(1, "Load", "Loading stored settings from file")
    storedSettingsObj = pickle.loads(str(storedSettings.firstChild.data.strip()))
    app.storedSettings().update(storedSettingsObj)

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

        waves = map(app.waves().wave, waveNames)
        
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

        # Get attributes for the figure
        for attrName in figure.attributes.keys():
            figureAttrs[attrName] = int(figure.attributes[attrName].value.strip())

        # Get figure from xml
        pickledFigure = figure.firstChild.data.strip()
        figureObj = pickle.loads(str(pickledFigure))
        figureWindow = app.figures().addFigure(figureObj)._figureSubWindow

        # Reset QT widget values
        figureWindow.setWindowState(Qt.WindowState(figureAttrs["windowState"]))
        figureWindow.resize(figureAttrs["width"], figureAttrs["height"])
        figureWindow.move(figureAttrs["xpos"], figureAttrs["ypos"])

        # Add to stackingOrder
        if figureAttrs["stackingOrder"] >= len(stackingOrder):
            stackingOrder.extend([None] * (figureAttrs["stackingOrder"] - len(stackingOrder) + 1))
        stackingOrder[figureAttrs["stackingOrder"]] = figureWindow

        # Set the figure dialog selected to the first figure
        app._loadedModules['EditFigureDialog'].changeCurrentFigure(0)
        app._loadedModules['EditFigureDialog'].updateFigureSelectorIndex(0)

