# PRUEBA FUNCIONAMIENTO DAO

# PRUEBA OK

# USER: admin
# PASSWORD: admin

from userDao import userDao;

access = userDao()

password = access.select_pass("administrador")
email    = access.select_email("administrador")

#Change attributes
access.update_pass("administrador","admin")
access.update_email("administrador","admin@admin.com")
access.update_username("administrador","admin")

newpassword = access.select_pass("admin")
newemail    = access.select_email("admin")

print(password)
print(email)

print(newpassword)
print(newemail)