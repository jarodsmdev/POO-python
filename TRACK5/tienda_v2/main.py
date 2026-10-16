"""Archivo principal para ejecutar la aplicación de la tienda."""

from TRACK5.tienda_v2.models.application import Application

if __name__ == "__main__":
    app = Application()
    app.main()
