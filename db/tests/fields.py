Unset = type('Unset', (), {})


class ModelField:
    def __init__(self, model_class, name, default_value=Unset, type=None):
        self.model_class = model_class
        self.name = name
        self._default_value = default_value
        self.type = type
        self.is_property = isinstance(getattr(model_class, name, None), property)

        try:
            self._validate = getattr(model_class, 'validate_{}'.format(name))
        except AttributeError:
            self._validate = None
