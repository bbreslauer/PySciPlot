

class Module():
    """
    Base class for all modules.  All modules should inherit this class and
    override the following methods:

    getMenuNameToAddTo - determine what menu (objectName) will be the parent of the menu item
    prepareMenuItem - do any customization of the menu item (like name it, set the text, etc)
    """

    def __init__(self, app):
        """Initialize the module.  You should probably create the widget here."""
        self._widget = QWidget()
        self._app = app

    def getWidget(self):
        """Return the widget."""
        return self._widget

    def getMenuNameToAddTo(self):
        """The widget will be activated via a menu.  What menu (specifically, the
        object name of the menu) should it go under?"""
        raise NotImplementedError

    def prepareMenuItem(self, menu):
        """Prepare the menu item that will be added to the application menus."""
        raise NotImplementedError

