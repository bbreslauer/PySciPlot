class Module():
    """
    Base class for all modules.  All modules should inherit this class and
    override the following methods:

    load - Do everything necessary to load the module
    unload - Do everything necessary to unload the module
    """

    def __init__(self, app):
        """Initialize the module."""
        self._app = app

    def load(self):
        """
        Perform all actions required in order to load the module.
        This will normally include creating the necessary window(s) and adding
        menu entries.

        Add a window with the following:

        self.windowName = DialogSubWindow(self._app.ui.workspace)
        self.windowName.setWidget(self._widget)
        self._widget.setParent(self.windowName)

        Create a menu action and add to a menu with name (not text) "menuName" with the following:

        self.menuEntry = QAction(self._app)
        self.menuEntry.setObjectName("menuActionName")
        self.menuEntry.setShortcut("Ctrl+X")
        self.menuEntry.setText("Menu Entry Text")
        self.menuEntry.triggered.connect(self.windowName.show)
        menu = getattr(self._app.ui, menuName)
        menu.addAction(self.menuEntry)
        """
        raise NotImplementedError

    def unload(self):
        """
        Perform all actions required in order to unload the module.
        This will normally include deleting the necessary window(s) and removing
        menu entries.
        """
        raise NotImplementedError

