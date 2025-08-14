#CLASE PRODUCTO
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor de la clase Producto- supuesto: el ID del producto es único para identificar cada producto, la cantidad se ubicará en números enteros y el precio en entero o decimal"""
        self.id_producto = id_producto      #identificador único del producto
        self.nombre = nombre                #Nombre del producto
        self.cantidad = cantidad            #Cantidad que tengo en mi inventario
        self.precio = precio                #este precio es unitario por producto

    # Getters_Es una encapsulación permite acceder a atributos privados
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters_Encapsulación para modificar atributos de forma controlada
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        """Lo utilizo para imprimir la información del producto y que sea más clara"""
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"
