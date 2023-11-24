## Identificación y Refactorización del Antipatrón "Spaghetti Code" en Python

### Descripción del Ejercicio

Este ejercicio se centra en la identificación y corrección de un antipatrón de programación conocido como "Spaghetti Code". El código proporcionado muestra un estilo complejo y poco legible que dificulta su seguimiento y mantenimiento.

#### Enunciado

Se provee el siguiente fragmento de código:

```python
def calcular(operacion, num1, num2):
    if operacion == 'suma':
        return num1 + num2
    if operacion == 'resta':
        return num1 - num2
    if operacion == 'multiplicacion':
        return num1 * num2
    if operacion == 'division':
        if num2 != 0:
            return num1 / num2
        else:
            print("No se puede dividir entre cero.")
    else:
        print("Operación no soportada.")
```
El objetivo es identificar las características del antipatrón "Spaghetti Code" presentes en el código y realizar una refactorización para mejorar su legibilidad y mantenibilidad. Se espera eliminar la complejidad de control, modularizar el código y mejorar el manejo de errores.

Evaluación del Ejercicio:

## Identificación de Características de "Spaghetti Code" (20%)

### Función `calcular`

La función `calcular` presenta ciertas características que indican la presencia de "Spaghetti Code":

- **Control basado en cadenas**: El uso de cadenas (`'suma'`, `'resta'`, `'multiplicacion'`, `'division'`) para controlar el flujo del programa puede llevar a una lógica compleja y poco clara.

- **Lógica anidada y falta de modularización**: El manejo de diferentes operaciones se realiza a través de múltiples condicionales anidados (`if-else`), lo que dificulta la lectura y mantenimiento del código.

- **Manejo de errores sin excepciones**: La función maneja un caso de error (división por cero) mediante una impresión directa, lo cual puede no ser adecuado para un manejo robusto de errores. La falta de excepciones podría llevar a un control poco estructurado de casos excepcionales.

Refactorización del Código (60%)

La refactorización debe mejorar la legibilidad y la estructura del código. 
Se espera una modularización adecuada, eliminación del control basado en cadenas y un mejor manejo de errores.

Justificación de Cambios (20%)
Se requiere una explicación detallada de los cambios realizados, cómo estos mejoran el código y cómo evitan las características de "Spaghetti Code".

Observaciones Finales:

Se debe presentar una versión mejorada del código que demuestre una estructura más limpia y un diseño más claro. 
Asegúrate de destacar los beneficios de los cambios realizados y cómo estos mejoran la calidad y mantenibilidad del código.
