from __future__ import annotations
from typing import Union

class Fecha:
    def __init__(self, dia: int, mes: int, año: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        '''

        if año < 1900:
            self.año = 1900
        elif año > 2050:
            self.año = 1900
        else:
            self.año = año
        if mes < 1:
            self.mes = 1
        elif mes > 12:
            self.mes = 12
        else:
            self.mes = mes
        max_dias = self.dias_en_mes(self.mes, self.año)
        if dia < 1:
            self.dia = 1
        elif dia > max_dias:
            self.dia = 1
        else:
            self.dia = dia

    @staticmethod
    def es_año_bisiesto(año: int) -> bool:
        return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

    @staticmethod
    def dias_en_mes(mes: int, año: int) -> int:
        if mes == 2:
            if Fecha.es_año_bisiesto(año):
                return 29
            else:
                return 28
        elif mes in {4, 6, 9, 11}:
            return 30
        else:
            return 31

    def obtener_dias_transcurridos(self) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha'''
        dias = self.dia - 1
        for x in range(1, self.mes):
            dias += self.dias_en_mes(x, self.año)
        for y in range(1900, self.año):
            dias += 366 if self.es_año_bisiesto(y) else 365
        return dias

    @property
    def dia_semana(self) -> int:
        '''Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).'''
        return (self.obtener_dias_transcurridos() + 1) % 7

    @property
    def es_fin_de_semana(self) -> bool:
        '''True si es fin de semana (sábado o domingo), False en caso contrario.'''
        if self.dia_semana in {5, 6}:
            return True
        else:
            return False

    @property
    def fecha_corta(self) -> str:
        '''02/09/2003'''
        if self.dia >= 10:
            dia_str = str(self.dia)
        else:
            dia_str = "0" + str(self.dia)
        
        if self.mes >= 10:
            mes_str = str(self.mes)
        else:
            mes_str = "0" + str(self.mes)
        
        return dia_str + "/" + mes_str + "/" + str(self.año)




    def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
        import datetime
        dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        dia_semana = dias_semana[self.dia_semana]
        nombres_meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        nombre_mes = nombres_meses[self.mes - 1]
        return f"{dia_semana.upper()} {self.dia} DE {nombre_mes.upper()} DE {self.año}"

    def __add__(self, dias: int) -> Fecha:
        '''Sumar un número de días a la fecha'''
        delta = datetime.timedelta(days=dias)
        nueva_fecha = datetime.date(self.año, self.mes, self.dia) + delta
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha'''
        ...

    def __lt__(self, other) -> bool:
        ...

    def __gt__(self, other) -> bool:
        ...

    def __eq__(self, other) -> bool:
        ...




if __name__ == "__main__":
    f1 = Fecha(1, 1, 2000)
    print(f1.dia_semana)
    print(f1.es_fin_de_semana)
    print(f1.fecha_corta)
    print(f1)

    f2 = Fecha(31, 12, 1999)
    print(f1 > f2)
    print(f1 - f2)