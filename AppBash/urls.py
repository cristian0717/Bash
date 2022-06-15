from django.urls import path
from AppBash.views import login, vendedor, ventas, mediosDePago, articulo, cliente
from AppBash.views import plantilla1

urlpatterns = [
    path("login/", login, name="Login"),
    path("vendedor/", vendedor, name="Vendedor"),
    path("ventas/", ventas, name="Ventas"),
    path("mediosdepago/", mediosDePago, name="Medios de pago"),
    path("articulo/", articulo, name="Articulo"),
    path("cliente/", cliente, name="Cliente"),
    path("", plantilla1)
]