#Datos del restaurante: lista de usuarios y ventas del restaurante
usuarios = []
ventas = [
    {
        "idVenta": 1,
        "nombreCliente": "Juan Pérez",
        "numeroMesa": 1,
        "platoPrincipal": "Bandeja Paisa",
        "valorConsumo": 53500,
        "metodoPago": "EFECTIVO",
        "estadoPedido": "ENTREGADO"
    },
    {
        "idVenta": 2,
        "nombreCliente": "Mauricio Gómez",
        "numeroMesa": 2,
        "platoPrincipal": "Ajiaco",
        "valorConsumo": 32000,
        "metodoPago": "TRANSFERENCIA",
        "estadoPedido": "PENDIENTE" 
    },
    {
        "idVenta": 3,
        "nombreCliente": "Carlos Gallego",
        "numeroMesa": 4,
        "platoPrincipal": "Salchipapas Especiales",
        "valorConsumo": 28000,
        "metodoPago": "TARJETA",
        "estadoPedido": "ENTREGADO"
    },
    {
        "idVenta": 4,
        "nombreCliente": "Alejandro Zapata",
        "numeroMesa": 7,
        "platoPrincipal": "Pasta Alfredo",
        "valorConsumo": 35000,
        "metodoPago": "EFECTIVO",
        "estadoPedido": "ENTREGADO"
    },
    {
        "idVenta": 5,
        "nombreCliente": "Sebastián Mejía",
        "numeroMesa": 3,
        "platoPrincipal": "Hamburguesa con Queso",
        "valorConsumo": 25000,
        "metodoPago": "TARJETA",
        "estadoPedido": "ENTREGADO"
    },
    {
        "idVenta": 6,
        "nombreCliente": "Juan Camilo",
        "numeroMesa": 9,
        "platoPrincipal": "Sandwich de Pollo",
        "valorConsumo": 18000,
        "metodoPago": "TRANSFERENCIA",
        "estadoPedido": "PENDIENTE"
    },
    {
        "idVenta": 7,
        "nombreCliente": "Luciana Rodríguez",
        "numeroMesa": 5,
        "platoPrincipal": "Perro Caliente Especial",
        "valorConsumo": 22000,
        "metodoPago": "TARJETA",
        "estadoPedido": "ENTREGADO"
    },
    {
        "idVenta": 8,
        "nombreCliente": "Juliana Martínez",
        "numeroMesa": 8,
        "platoPrincipal": "Ensalada César",
        "valorConsumo": 25000,
        "metodoPago": "EFECTIVO",
        "estadoPedido": "ENTREGADO"
    },
    {
        "idVenta": 9,
        "nombreCliente": "Luis Restrepo",
        "numeroMesa": 6,
        "platoPrincipal": "Bandeja Paisa",
        "valorConsumo": 53500,
        "metodoPago": "EFECTIVO",
        "estadoPedido": "ENTREGADO"
    },
    {
        "idVenta": 10,
        "nombreCliente": "Ana María López",
        "numeroMesa": 10,
        "platoPrincipal": "Sopa de Carne",
        "valorConsumo": 15000,
        "metodoPago": "TRANSFERENCIA",
        "estadoPedido": "PENDIENTE"
    }
]

#Funciones del usuario: registrar usuario e iniciar sesión

#Registro de usuarios
def registro_usuario():
    correo_registro = input("Ingrese su correo electrónico: ")
    contraseña_registro = input("Ingrese su contraseña: ")
    usuario = {
        "correo": correo_registro,
        "contraseña": contraseña_registro
    }
    usuarios.append(usuario)
    print("Usuario registrado exitosamente.")

#Inicio de sesión

def iniciar_sesion():
    intentos = 4                                      
    while intentos > 0:
        correo = input("Digite su correo: ")          
        contraseña = input("Digite su contraseña: ")
        
        for usuario in usuarios:
            if correo == usuario["correo"] and contraseña == usuario["contraseña"]:
                print("Login exitoso.")
                return True
        
        intentos -= 1
        print("Credenciales incorrectas. Intentos restantes:", intentos)
    
    print("Cuenta bloqueada temporalmente.")
    return False

#Funciones de ventas: crear venta, mostrar ventas, ordenar ventas, buscar ventas y eliminar ventas

#Mostrar ventas
def mostrar_ventas():
    for venta in ventas:
        print(f"ID Venta: {venta['idVenta']}) Cliente: {venta['nombreCliente']}, Mesa: {venta['numeroMesa']}, Plato: {venta['platoPrincipal']}, Valor: {venta['valorConsumo']}, Pago: {venta['metodoPago']}, Estado: {venta['estadoPedido']}")

#Ordenar las ventas por valor de consumo
def ordenar_ventas():
    ventas.sort(key=lambda venta: venta["valorConsumo"])
    print("Ventas ordenadas por valor de consumo.")
    mostrar_ventas()

#Buscar una venta por ID
def buscar_ventas():
    id_buscar = int(input("Ingrese el ID de la venta a buscar: "))
    for venta in ventas:
        if venta["idVenta"] == id_buscar:
            print(f"ID venta: {venta['idVenta']}, Cliente: {venta['nombreCliente']}, Mesa: {venta['numeroMesa']}, Plato: {venta['platoPrincipal']}, Valor: {venta['valorConsumo']}, Metodo de Pago: {venta['metodoPago']}, Estado del Pedido: {venta['estadoPedido']}")
            return
    print("Venta no encontrada.")

#Eliminar una venta
def eliminar_venta():
    id_eliminar = int(input("Ingrese el ID de la venta a eliminar: "))
    for venta in ventas:
        if venta["idVenta"] == id_eliminar:
            ventas.remove(venta)
            print("Venta eliminada correctamente.")
            return
    print("Venta no encontrada.")

#Agregar una nueva venta
def agregar_venta():
    id_Venta = int(input("Ingrese el ID de la venta: "))
    nombre_Cliente = input("Ingrese el nombre del cliente: ")
    numero_Mesa = int(input("Ingrese el número de mesa: "))
    plato_Principal = input("Ingrese el nombre del plato principal: ")
    valor_Consumo = int(input("Ingrese el valor del consumo: "))
    metodo_Pago = input("Ingrese el método de pago: ")
    estado_Pedido = input("Ingrese el estado del pedido: ")

    nueva_venta = {
        "idVenta": id_Venta,
        "nombreCliente": nombre_Cliente,
        "numeroMesa": numero_Mesa,
        "platoPrincipal": plato_Principal,
        "valorConsumo": valor_Consumo,
        "metodoPago": metodo_Pago,
        "estadoPedido": estado_Pedido
    }

    ventas.append(nueva_venta)
    print("Venta agregada correctamente.")


# Menu de ventas
def menu_ventas():
    while True:
        print("\n--- Menú de Ventas ---")
        print("1. Mostrar ventas")
        print("2. Ordenar ventas por valor")
        print("3. Buscar venta")
        print("4. Eliminar venta")
        print("5. Agregar nueva venta")
        print("6. Salir del menú de ventas")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_ventas()
        elif opcion == "2":
            ordenar_ventas()
        elif opcion == "3":
            buscar_ventas()
        elif opcion == "4":
            eliminar_venta()
        elif opcion == "5":
            agregar_venta()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

# Flujo principal del programa
registro_usuario()
if iniciar_sesion():
    menu_ventas()
