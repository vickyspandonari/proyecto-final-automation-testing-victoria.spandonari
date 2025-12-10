# Proyecto-final-automation-testing-victoria.spandonari
Este proyecto corresponde a la entrega final de Automation Testing, e incluye pruebas automatizadas de UI (Selenium WebDriver), API (Requests) y mocks, utilizando Python + Pytest.

### Herramientas utilizadas para la automatización:

| Categoría | Herramienta | 
| :--- | :--- | 
| **Lenguaje** | Python 3.12 | 
| **Framework** | Pytest | 
| **UI Testing** | Selenium WebDriver | 
| **API Testing** | Requests | 
| **Mocks** | `unittest.mock` / `responses` | 
| **Reportes** | `Pytest HTML` | 


# Tecnologías utilizadas
* Python 3.12
* Pytest como framework de pruebas
* Selenium WebDriver para pruebas UI
* WebDriver Manager para manejo automático del driver
* Requests para pruebas API
* Unittest.mock / responses para mocks
* Pytest HTML para reportes

# Instalación
Clonar Repositorio: 
```git clone https://github.com/vickyspandonari/proyecto-final-automation-testing-victoria.spandonari```

Instalar dependencias:
```pip install -r requirements.txt```

# Ejecución de Pruebas

Ejecutar todas las pruebas:
```pytest```

Ejecutar solo pruebas UI:
```pytest tests/test_login.py```

Ejecutar solo pruebas API
```pytest tests/test_api.py```

Generar Reporte HTML:
```pytest --html=reports/report.html --self-contained-html```

# Sitio bajo prueba (UI)
**(https://www.saucedemo.com/)**

Flujos Automatizados:
* Login correcto
* Login incorrecto (escenario negativo)
* Navegación por productos
* Visualización de detalle de producto
* Agregar productos al carrito
* Proceso de checkout completo



