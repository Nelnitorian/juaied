
--- Main.py
    Inicio de programa
    
--- PageGeneric.py
    Página genérica padre de las que heredan las demás páginas.

--- PageLogin.py
    Ventana de Login.

--- PageUser.py
    Ventana principal de usuario donde puede acceder a todas las opciones.
    
--- PageNewUser.py
    Ventana desde donde se puede agregar un nuevo usuario, para el uso de la red como para su facturación.

--- PageModUser.py
    Ventana desde donde se puede modificar tanto la tarifa, como usuario y contraseña de un usurio.

--- PageNewTax.py
    Ventana desde donde se puede crear una nueva tarifa.

--- PageUserInf.py
    Ventana desde donde se puede ver a tiempo real (cada 3 segundos se actualizan datos) la información relativa a usuario:
    --- Apellidos, Nombre, username, tarifa, dinero, bytes, tiempo ---
    También seleccionado un usuario se puede generar una factura con forme a su tarifa y consumo.

--- UtilitiesFun.py
    Funciones para confirmación de datos introducidos y login.
    
--- DaoAdmin.py (database = credentials)
    Dao de acceso a datos de administrador de la red.
    Tabla = users (username, pass, email)

--- DaoRad.py (database = radius)
    Dao de acceso a datos relacionados con la base de datos Radius.
    Añadir, modificar, eliminar credenciales de usuario.
    Consultar tiempo, octetos.
    --> username                         (tabla = radcheck)
    --> attribute: Cleartext-Password    (tabla = radcheck)
    --> value: password                  (tabla = radcheck)                            
    --> acctinputoctets : octetos enviados por el usuario   (tabla = radacct)
    --> acctoutputoctets: octetos recibidos por el usuario  (tabla = radacct)
    --> acctsessiontime: tiempo de sesion del usuario       (tabla = radacct)

--- DaoTax.py (database = company)
    Dao de accceso a datos relacionados con tarifas.
    Tabla = tarifa_inf (tarifa, control, ratio)

--- DaoUserInf.py (database = company)
    Dao de acceso a datos relacionados con información de usuario.
    Tabla = user_inf
    --> username
    --> pass
    --> nombre
    --> apellidos
    --> tarifa
    --> dinero (euros)
    --> paquetes: numero de octetos enviados y recibidos
    --> tiempo: tiempo de sesion del usuario