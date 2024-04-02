## Descripción del código

Este código implementa una clase Fecha en Python para representar fechas con día, mes y año. La clase proporciona funcionalidades como la validación de fechas, cálculo de días transcurridos desde una fecha base, determinación del día de la semana, y verificación de si una fecha cae en fin de semana.

## Características principales

Validación de la fecha: Al crear una instancia de la clase Fecha, se valida si la fecha proporcionada es válida (entre el 1-1-1900 y el 31-12-2050). Si alguno de los componentes de la fecha (día, mes o año) no es válido, se ajusta automáticamente.

## Métodos estáticos:

es_año_bisiesto(año: int) -> bool: Determina si un año es bisiesto.
dias_en_mes(mes: int, año: int) -> int: Devuelve el número de días en un mes específico de un año dado.

## Métodos de instancia:

obtener_dias_transcurridos() -> int: Calcula el número de días transcurridos desde el 1-1-1900 hasta la fecha actual.
dia_semana (propiedad): Devuelve el día de la semana de la fecha (0 para domingo, 1 para lunes, etc.).
es_fin_de_semana (propiedad): Indica si la fecha es un fin de semana (sábado o domingo).
fecha_corta (propiedad): Devuelve la fecha en formato corto (DD/MM/YYYY).

## Sobrecarga de operadores:

__add__(self, dias: int) -> Fecha: Permite sumar un número de días a la fecha actual.
