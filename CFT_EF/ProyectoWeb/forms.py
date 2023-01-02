from django import forms
from django.core import validators

class FormProducto(forms.Form):
    codigo = forms.CharField(
        label = "Código",
        widget = forms.TextInput(
            attrs = {
                'placeholder': ' Ingrese el código',
                'class': 'codigo_form_producto'
            }
        ),
        validators = [
            validators.MaxLengthValidator(4, 'Los código de los productos solo tienen 4 caracteres'),
            validators.RegexValidator('^[A-Za-z0-9\u00C0-\u017FñÑ ]*$', 'El título tiene caracteres inválidos', 'codigo_invalido')
        ]
    )
    nombre = forms.CharField(
        label = "Nombre",
        max_length = 40,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': ' Ingrese el nombre del producto',
                'class': 'nombre_form_producto'
            }
        ),
        validators = [
            validators.MinLengthValidator(4, 'El nombre es muy corto'),
            validators.RegexValidator('^[A-Za-z0-9\u00C0-\u017FñÑ ]*$', 'El nombre tiene caracteres inválidos', 'nombre_invalido')
        ]
    )
    precio_compra = forms.FloatField(
        label = "Precio de compra",
        widget = forms.TextInput(
            attrs = {
                'placeholder': ' Ingrese el precio de compra del producto',
                'class': 'precio-compra_form_producto'
            }
        )
    )
    precio_venta = forms.FloatField(
        label = "Precio de venta",
        widget = forms.TextInput(
            attrs = {
                'placeholder': ' Ingrese el precio de venta del producto',
                'class': 'precio-venta_form_producto'
            }
        )
    )
    fecha_compra = forms.DateField(
        label = "Fecha de compra (Mes/Día/Año)"
    )
    opciones_estado = [
        (1, 'Sí'),
        (0, 'No'),
    ]
    estado = forms.TypedChoiceField(
        label = "¿Vigente?",
        choices = opciones_estado,
    )