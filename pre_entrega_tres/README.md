# _App_Kiosco_

## Resumen

La app de Kiosco, represente un sitio web de 5 secciones, la seccion de productos y ventas son las unicas que tiene funcionalidad.
Se puede hacer CRUD en:
                    + Productos
                    + Proveedores
                    + Ventas
Tambien tiene un buscador, solo para realizar la busqueda de productos.
Los productos se listan en la misma seccion de productos y en la seccion de ventas se listan las ventas de ese cliente.

## Informacion

Para la Entrega-Final se creo una app estilo e-commerce para kioscos. La funcionalidad que tiene es un CRUD de producto, proveedor y compra solo se consulta, la busqueda es solo para productos que se listan en la misma seccion.
Se puede navegar en el sitio a travez de una barra de navegacion con los vinculos de cada seccion.
Tanto la barra de navegacion como el footer son herencia de HTML que pasan a cada seccion.
Desde el futer se habilito la carga de newsletter en una tabla la cual se utilizaria para enviar las novedades a los correos registrados.

## App

La aplicacion cuenta con un registro para usuarios por formulario, los mismo solo estan habilitados a consultar los productos, hacer la busqueda de un producto y realizar una compra. 
No se creo un carrito de compras, solo se guardan las compras en una tabla y se muestran en la seccion de compras.
Solo los usuarios Administradores tienen habilitado el uso de un CRUD completo sobre productos, proveedores y compras. A diferencia de los usuarios Staff que ellos solon pueden crear y modificar productos, proveedores sin poder borrar los mismos.
Sin iniciar sesion, solo se pueden visitar las secciones de Home, about y contact.

## Usuarios

    < Se crearon 3 usuarios: la contraseña es la misma para los 3: Pa22w0rd >
        + usuario: Este es el tipo que se crear desde la web a travez del registro y solo se puede consultar los productos y las compras del usuario y tambien comprar productos.
        + staff: Este tipo se crea a travez de la seccion admin de django y puede manejarse haciendo todo menos borrar.
        + admin: Este es el tipo superuser que tiene control absoluto.

    Todos los usuarios creados puede modificar sus atributos como su nombre, correo, etc.




