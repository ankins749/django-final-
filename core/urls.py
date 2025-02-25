from django.urls import path
from .views import (
	index, nosotros, obtener_boletas, obtener_boletas_user, panel_admin, 
	agregar_productos, agregar_user, api, 
	carrito_compras, historial_compras, 
	mantenedor_bodega, mis_datos, navegacion, 
	nosotros, registro, ventas, login,
	footer, logout, importar_productos, eliminar_producto,
	obtener_productos, actualizar_cuenta, actualizar_producto,
    crear_boleta, verificar_boletas, actualizar_estado_boleta,
    eliminar_cuenta, error404, actualizar_cuenta_admin
)

urlpatterns = [
	path("", index, name="index"),
	path("navegacion", navegacion, name="navegacion"),
	path("footer", footer, name="footer"),
	path("registro/", registro, name="registro"),
	path("login/", login, name="login"),
	path("logout/", logout, name="logout"),
	path("nosotros/", nosotros, name="nosotros"),
	path("panel_admin/", panel_admin, name="panel_admin"),
	path("agregar_productos/", agregar_productos, name="agregar_productos"),
	path("agregar_user/", agregar_user, name="agregar_user"),
	path("api/", api, name="api"),
	path("api/productos/", obtener_productos, name="obtener_productos"),
	path("carrito_compras/", carrito_compras, name="carrito_compras"),
	path("historial_compras/", historial_compras, name="historial_compras"),
	path("mantenedor_bodega/", mantenedor_bodega, name="mantenedor_bodega"),
	path("mis_datos/", mis_datos, name="mis_datos"),
    path("actualizar_cuenta", actualizar_cuenta, name="actualizar_cuenta"),
	path("nosotros/", nosotros, name="nosotros"),
	path("ventas/", ventas, name="ventas"),
	path("eliminar_producto/<int:id>/", eliminar_producto, name="eliminar_producto"),
	path("editar_producto/<int:id>/", lambda request, id: agregar_productos(request, id), name="editar_producto"),
	path("importar_productos/", importar_productos, name="importar_productos"),
    path("actualizar_producto", actualizar_producto, name="actualizar_producto"),
    path("crear_boleta/", crear_boleta, name="crear_boleta"),
    path("verificar_boletas/", verificar_boletas, name="verificar_boletas"),
    path("obtener_boletas_user/", obtener_boletas_user, name="obtener_boletas_user"),
    path("obtener_boletas/", obtener_boletas, name="obtener_boletas"),
    path("actualizar_estado_boleta/<int:boletaID>/<str:nuevo_estado>/", actualizar_estado_boleta, name="actualizar_estado_boleta"),
    path("eliminar_cuenta/<str:cuentaID>/", eliminar_cuenta, name="eliminar_cuenta"),
    path("error404", error404, name="error404"),
    path("actualizar_cuenta_admin", actualizar_cuenta_admin, name="actualizar_cuenta_admin")

]