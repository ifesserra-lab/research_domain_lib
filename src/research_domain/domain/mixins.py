from sqlalchemy import inspect

class SerializableMixin:
    """
    Mixin that adds serialization capabilities to SQLAlchemy models.
    """
    def to_dict(self):
        """
        Returns a dictionary representation of the model, including all columns
        from the current class and any parent classes (if using Joined Table Inheritance).
        """
        result = {}
        processed_keys = set()
        
        # Iterate over the MRO (Method Resolution Order) to find all column attributes
        # This ensures we get columns from parent classes in inheritance scenarios
        for cls in self.__class__.__mro__:
            try:
                mapper = inspect(cls)
                if not mapper.is_mapper:
                    continue
                for column in mapper.column_attrs:
                    key = column.key
                    if key not in processed_keys:
                        result[key] = getattr(self, key)
                        processed_keys.add(key)
            except Exception:
                continue
        
        return result
