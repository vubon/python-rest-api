import typing
from db.tests.fields import ModelField


class BaseModel(type):
    """Metaclass for all models."""

    _field_class = ModelField

    def __new__(cls, name, bases, attrs, **kwargs):
        super_new = super().__new__

        parents = [b for b in bases if isinstance(b, BaseModel)]
        if not parents:
            return super_new(cls, name, bases, attrs)

        new_class = super_new(cls, name, bases, attrs)
        meta = type('Meta', (), {})
        hints = typing.get_type_hints(new_class)
        attrs = cls._get_class_attributes(new_class, parents)
        assert hints or attrs, '{} model must define class attributes'.format(new_class.__name__)
        meta.fields = cls._get_fields(attrs, hints)
        meta.descriptors = {}

        print(meta.fields)

        # for field_name in meta.fields:
        #     field_type = hints.get(field_name) if hints else None
        #     default_value = getattr(new_class, field_name, Unset)
        #     field = ModelField(
        #         model_class=new_class,
        #         name=field_name,
        #         default_value=default_value,
        #         type=field_type,
        #     )
        #     meta.descriptors[field_name] = field

        new_class._meta = meta


    @classmethod
    def _get_class_attributes(cls, new_class, parents):
        print(new_class)
        print(parents)

    @classmethod
    def _get_fields(cls, attrs, hints):
        fields = set(hints) | attrs
        print('Fields', fields)
        fields.discard('Meta')
        return tuple(fields)


class Model(metaclass=BaseModel):

    def __init__(self, **kwargs):
        self.__post_init__(**kwargs)

    def __post_init__(self, **kwargs):
        pass
