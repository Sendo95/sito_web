"""
Questo file definisce la base per tutti i modelli SQLAlchemy.
Tutti i modelli dovrebbero ereditare da questa base.
"""

from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    """
    Classe base per tutti i modelli SQLAlchemy.
    """
    id: int
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        """
        Genera automaticamente il nome della tabella in base al nome della classe.
        """
        return cls.__name__.lower()

"""
Descrizione delle componenti:

1. **Base**: Classe base per tutti i modelli SQLAlchemy.
2. **__tablename__**: Genera automaticamente il nome della tabella in base al nome della classe.
"""
