class UnknownWidgetTypeError(Exception):
    """
    Exception raised for unknown widget types.
    
    Attributes:
        widgetType -- the type of widget which is unknown
    """

    def __init__(self, widgetType):
        self.widgetType = widgetType

    def __str__(self):
        return repr(self.widgetType)

