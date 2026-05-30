class WidgetRegistry:
    """
    Simple widget system for dashboard UI composition
    """

    widgets = {}

    @classmethod
    def register(cls, name):
        def wrapper(widget_class):
            cls.widgets[name] = widget_class()
            return widget_class
        return wrapper

    @classmethod
    def get(cls, name):
        return cls.widgets.get(name)
