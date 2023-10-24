# Entrega_Final_NicholasSprigings_CursoPython

Se desarrolla una web para una empresa de Post Producción.
Se crean diferentes pestañas y las urls son las siguientes:

    path('agrega-portafolio/<cliente>/<agencia>', portafolio),  
    ==> Se usa para agregar al view portafolio los diferentes trabajos realizados junto a la Agencia y el Cliente final
    path('', inicio, name="Inicio"),  
    ==> Es nuestra página de inicio (HomePage), donde en un futuro mostrará novedades y noticias
    path('portafolio/', portafolio, name="Portafolio"),  
    ==> Es nuestra página portafolio que en un futuro mostrará diferentes videos con su descripción
    path('servicios/', servicios, name="Servicios"),  
    ==> Es nuestra página de servicios en donde en un futuro mostrará los diferentes servicios que nuestra empresa brinda
    path('quienes_somos/', quienes_somos, name="Quienes Somos"),  
    ==> Es nuestra página de Quienes Somos (About Us). En donde en un futuro mostrará 
    una imágen de cada una de las personas que integran el equipo y una breve descripción de cada uno
    path('formulariocontactanos /', formulario_contactanos, name="formulario_contactanos"),
    ==> Es nuestra página de Contactanos en donde se pude completar el formulario y la información 
    se guarda en nuestra base de datos
    path('login/', loginView, name="Login"),
    ==> Es nuestra página para Loguearnos con nuestro Usuario y Contraseña
    path('register/', register, name="Registrar"),
    ==> Es nuestra página en donde podemos registrar nuevo usuarios
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    ==> Es nuestra página en la que se realiza el logaout
    path('editarPerfil/', editar_perfil, name="EditarPerfil"),
    ==> Es nuestra página en la que se puede realizar cambios a nuestro perfil.

En este link se podrá encontrar un video con una breve explicación de nuestra web ==> https://youtu.be/Ol770OpMQ-c
