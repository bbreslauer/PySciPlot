from gui.SubWindows import SubWindow

class ModuleHandler():
    """
    Handle all modules, including importing them into the main program.
    """

    def __init__(self):
        pass

    def addWidgetToWindow(self, widget, subWindow):
        """
        Encapsulate a widget in a SubWindow (basically a QMdiSubWindow) and
        then add it to the QMdiArea.
        """

        subWindow.setWidget(widget)
        widget.setParent(subWindow)
        return subWindow


    def addWidgetToMenu(self, menuName, moduleMenu, window, action):
        """
        Add moduleMenu to the window's menu with the object name menuName.
        """
        menu = getattr(window, menuName)
        menu.addAction(moduleMenu)
        moduleMenu.triggered.connect(action)




