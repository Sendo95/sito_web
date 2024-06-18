
from pydantic import AnyHttpUrl, validator
from typing import List, Optional, Union

class Settings():
    """
    La classe Settings utilizza Pydantic per definire e validare le variabili d'ambiente necessarie per l'applicazione.
    """

    # Variabili d'ambiente generali
    API_V1_STR: str = "/api/v1"  # Prefisso per tutte le rotte API
    SECRET_KEY: str  # Chiave segreta utilizzata per la sicurezza, come la firma dei token JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # Tempo di scadenza per i token di accesso (in minuti)

    # CORS (Cross-Origin Resource Sharing)
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []  # Lista degli URL permessi per CORS

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        """
        Validatore personalizzato per gestire le origini CORS. Converte una stringa separata da virgole in una lista.
        """
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, list):
            return v
        raise ValueError(v)

    # Configurazione del database
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: dict) -> str:
        """
        Validatore personalizzato per costruire la stringa di connessione al database.
        """
        if isinstance(v, str):
            return v
        return f"postgresql://{values.get('POSTGRES_USER')}:{values.get('POSTGRES_PASSWORD')}@{values.get('POSTGRES_SERVER')}/{values.get('POSTGRES_DB')}"

    # Variabili d'ambiente per il database
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    class Config:
        """
        Configurazione per Pydantic. Specifica che le variabili d'ambiente devono essere lette dal file .env.
        """
        env_file = ".env"
        case_sensitive = True

# Creazione di un'istanza di Settings
settings = Settings()
