# Necesidades para el cliente de billing pueda funcionar
_Aquí se describen las funciones escritas en RSC.py que necesitan una funcionalidad adicional_

### fetchUsernames
_Función que se encarga de devolver una lista con los usuarios cuya información se haya modificado en el último intervalo_

```
RSC.py#fetchUsernames()
fetchUsernames{
    #algo
    return usernames
}
```

### fetchUserData
_Función que se encarga de devolver los datos del usuario especificado_

```
Este aún tengo que pensarlo porque el DAO está ahí, pero no me gustaría cambiar el path del script para importarlo. Tengo que darle una pensada aún.
```

### updateStatus
_Función que actualiza el estado de un usuario para desconectarlo de la sesión y evitar que en futuros intentos de sesión se le conceda acceso_

```
RSC.py#updateStatus(username,status)
updateStatus{
    #algo
    pass
}
