from __future__ import annotations

class Fecha:
    def __init__(self, dia: int, mes: int, anio: int):
        '''Validar día, mes y anio. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el anio no es correcto, lo pondrá a 1900.
        Ojo con los anios bisiestos.
        El 1-1-1900 fue lunes.
        '''

        if anio < 1900:
            self.anio = 1900
        elif anio > 2050:
            self.anio = 1900
        else:
            self.anio = anio
        if mes < 1:
            self.mes = 1
        elif mes > 12:
            self.mes = 1
        else:
            self.mes = mes
        max_dias = self.dias_en_mes(self.mes, self.anio)
        if dia < 1:
            self.dia = 1
        elif dia > max_dias:
            self.dia = 1
        else:
            self.dia = dia

    @staticmethod
    def es_anio_bisiesto(anio: int) -> bool:
        return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

    @staticmethod
    def dias_en_mes(mes: int, anio: int) -> int:
        if mes == 2:
            if Fecha.es_anio_bisiesto(anio):
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
            dias += self.dias_en_mes(x, self.anio)
        for y in range(1900, self.anio):
            if self.es_anio_bisiesto(y):
                dias += 366
            else:
                dias += 365
        return dias

    @property
    def dia_semana(self) -> int:
        '''Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).'''
        return (self.obtener_dias_transcurridos() + 1) % 7

    @property
    def es_fin_de_semana(self) -> bool:
        '''True si es fin de semana (sábado o domingo), False en caso contrario.'''
        if self.dia_semana in {6, 0}:
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
        
        return dia_str + "/" + mes_str + "/" + str(self.anio)




    def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
        import datetime
        dias_semana = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]
        dia_semana = dias_semana[self.dia_semana]
        nombres_meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        nombre_mes = nombres_meses[self.mes - 1]
        return f"{dia_semana.upper()} {self.dia} DE {nombre_mes.upper()} DE {self.anio}"

    def __add__(self, dias: int) -> 'Fecha':
        '''Sumar un número de días a la fecha'''
        dia = self.dia + dias
        mes = self.mes
        anio = self.anio
        while dia > self.dias_en_mes(mes, anio):
            dia -= self.dias_en_mes(mes, anio)
            mes += 1
            if mes > 12:
                mes = 1
                anio += 1
        return Fecha(dia, mes, anio)

    def __sub__(self, other) -> Fecha:
        '''Restar una fecha a otra fecha -> Número de días
        Restar un número de días a la fecha -> Nueva fecha'''

        if isinstance(other, Fecha):
            return self.obtener_dias_transcurridos() - other.obtener_dias_transcurridos()

        elif isinstance(other, int):
            dia = self.dia - other
            mes = self.mes
            anio = self.anio
            
            while dia < 1:
                mes -= 1
                if mes < 1:
                    mes = 12
                    anio -= 1
                dia += self.dias_en_mes(mes, anio)
            
            return Fecha(dia, mes, anio)
        

    def __lt__(self, other) -> bool:
        if self.dia < other.dia:
            return True
        if self.mes < other.mes:
            return True
        if self.anio < other.anio:
            return True

    def __gt__(self, other) -> bool:
        if self.dia > other.dia:
            return True
        if self.mes > other.mes:
            return True
        if self.anio > other.anio:
            return True

    def __eq__(self, other) -> bool:
        if self.dia == other.dia:
            return True
        if self.mes == other.mes:
            return True
        if self.anio == other.anio:
            return True
