from abc import ABC, abstractmethod


# Clase base abstracta
class Servicio(ABC):
    """
    Clase abstracta para representar los servicios del sistema.
    """

    def __init__(self, codigo: str, nombre: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass

    def obtener_detalles(self):
        return f"Código: {self.codigo} | Servicio: {self.nombre} | Precio: ${self.precio}"


# Servicio Básico
class ServicioBasico(Servicio):

    def calcular_costo(self):
        return self.precio


# Servicio Premium
class ServicioPremium(Servicio):

    def calcular_costo(self):
        return self.precio * 1.20


# Servicio VIP
class ServicioVIP(Servicio):

    def calcular_costo(self):
        return self.precio * 1.50


# ==========================================
# BLOQUE DE PRUEBA LOCAL (Estudiante 2)
# ==========================================
if __name__ == "__main__":

    servicios = [
        ServicioBasico("S001", "Mantenimiento Básico", 100000),
        ServicioPremium("S002", "Soporte Premium", 150000),
        ServicioVIP("S003", "Atención VIP", 200000)
    ]

    print("=== LISTA DE SERVICIOS ===\n")

    for servicio in servicios:
        print(servicio.obtener_detalles())
        print(f"Costo calculado: ${servicio.calcular_costo():,.0f}")
        print("-" * 40)
