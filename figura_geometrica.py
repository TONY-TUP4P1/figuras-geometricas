"""
Este módulo define una jerarquía de figuras geométricas, con métodos
para calcular áreas según cada tipo de figura.
"""

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para calcular áreas y otros métodos comunes."""

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""

    def __str__(self):
        """Método para representar la figura geométrica de manera general."""
        return f"Figura geométrica de área {self.calcular_area()}"


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo y calcula su área."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura

    def __str__(self):
        return f"Rectángulo de base {self.base} y altura {self.altura}"

    def get_details(self):
        """Obtiene los detalles del rectángulo."""
        return {"base": self.base, "altura": self.altura}

    def is_large_area(self, threshold):
        """Verifica si el área del rectángulo es mayor al umbral dado."""
        return self.calcular_area() > threshold


class Triangulo(FiguraGeometrica):
    """Clase que representa un triángulo y calcula su área."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2

    def __str__(self):
        return f"Triángulo de base {self.base} y altura {self.altura}"

    def get_details(self):
        """Obtiene los detalles del triángulo."""
        return {"base": self.base, "altura": self.altura}

    def is_large_area(self, threshold):
        """Verifica si el área del triángulo es mayor al umbral dado."""
        return self.calcular_area() > threshold


class Circulo(FiguraGeometrica):
    """Clase que representa un círculo y calcula su área."""

    def __init__(self, radio):
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return self.pi * (self.radio ** 2)

    def __str__(self):
        return f"Círculo de radio {self.radio}"

    def get_details(self):
        """Obtiene los detalles del círculo."""
        return {"radio": self.radio}

    def is_large_area(self, threshold):
        """Verifica si el área del círculo es mayor al umbral dado."""
        return self.calcular_area() > threshold


# Variables globales
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3

# Ejecución principal
if __name__ == "__main__":
    # Crear instancias de las figuras
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    # Calcular áreas
    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")
