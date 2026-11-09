from abc import ABC, abstractmethod
import re

# 1. Clase Abstracta General del Sistema
class EntidadSistema(ABC):
    """
    Clase abstracta que representa entidades generales del sistema Software FJ.
    Establece una estructura base obligatoria para las clases derivadas.
    """
    
    def __init__(self, identificador: str):
        self._identificador = identificador

    @property
    def identificador(self) -> str:
        return self._identificador

    @abstractmethod
    def obtener_detalles(self) -> str:
        """Método abstracto que obliga a las subclases a retornar una descripción detallada."""
        pass


# 2. Excepción Personalizada para el Cliente (Apoyando el manejo robusto de excepciones de la Fase)
class ClienteError(Exception):
    """Excepción personalizada para errores relacionados con los datos del cliente."""
    pass


# 3. Clase Cliente (Hereda de EntidadSistema)
class Cliente(EntidadSistema):
    """
    Clase Cliente con validaciones estrictas y encapsulación de datos personales.
    """
    
    def __init__(self, identificador: str, nombre: str, correo: str, telefono: str):
        super().__init__(identificador)
        self.nombre = nombre       # Usa el setter para validar
        self.correo = correo       # Usa el setter para validar
        self.telefono = telefono   # Usa el setter para validar

    # --- ENCAPSULACIÓN Y VALIDACIONES ESTRICTAS (Getters y Setters) ---

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ClienteError(f"Error: El nombre '{valor}' no es válido. Debe tener al menos 3 caracteres.")
        self._nombre = valor.strip()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str):
        # Expresión regular básica para validar formato de correo electrónico
        patron_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(patron_email, valor):
            raise ClienteError(f"Error: El correo '{valor}' tiene un formato inválido.")
        self._correo = valor

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):
        if not valor.isdigit() or len(valor) < 7:
            raise ClienteError(f"Error: El teléfono '{valor}' no es válido. Debe contener solo números (mínimo 7 dígitos).")
        self._telefono = valor

    # Implementación del método abstracto requerido
    def obtener_detalles(self) -> str:
        return f"Cliente [ID: {self.identificador}] - Nombre: {self.nombre} | Correo: {self.correo} | Teléfono: {self.telefono}"


# ==========================================
# BLOQUE DE PRUEBA LOCAL (Para el Estudiante 1)
# ==========================================
if __name__ == "__main__":
    print("--- Pruebas de la Estructura del Estudiante 1 ---\n")
    
    # Prueba de creación de un cliente válido
    try:
        cliente1 = Cliente(identificador="C001", nombre="Ana Pérez", correo="ana.perez@email.com", telefono="3104567890")
        print("¡Cliente creado con éxito!")
        print(cliente1.obtener_detalles())
    except ClienteError as e:
        print(e)

    print("\n--- Probando validaciones estrictas (Errores controlados) ---\n")
    
    # Prueba con correo inválido
    try:
        cliente_malo = Cliente(identificador="C002", nombre="Carlos Gómez", correo="carlos-correo-malo", telefono="3201234567")
    except ClienteError as e:
        print(f"Excepción atrapada correctamente: {e}")
