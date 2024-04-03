import pytest
from date import Fecha


@pytest.fixture
def date1():
    # JUEVES
    return Fecha(dia=1, mes=3, anio=1979)


@pytest.fixture
def date2():
    # DOMINGO
    return Fecha(dia=24, mes=6, anio=1984)


def test_build_date(date1: Fecha, date2: Fecha):
    assert isinstance(date1, Fecha)
    assert date1.dia == 1
    assert date1.mes == 3
    assert date1.anio == 1979

    assert isinstance(date2, Fecha)
    assert date2.dia == 24
    assert date2.mes == 6
    assert date2.anio == 1984


def test_build_date_when_out_of_range():
    date = Fecha(dia=40, mes=1, anio=2000)
    assert date.dia == 1
    assert date.mes == 1
    assert date.anio == 2000

    date = Fecha(dia=1, mes=15, anio=2000)
    assert date.dia == 1
    assert date.mes == 1
    assert date.anio == 2000

    date = Fecha(dia=1, mes=1, anio=1850)
    assert date.dia == 1
    assert date.mes == 1
    assert date.anio == 1900


def test_es_anio_bisiesto():
    assert not Fecha.es_anio_bisiesto(1997)
    assert not Fecha.es_anio_bisiesto(1999)
    assert Fecha.es_anio_bisiesto(2008)
    assert Fecha.es_anio_bisiesto(2016)


def test_dias_en_mes():
    assert Fecha.dias_en_mes(1, 2005) == 31
    assert Fecha.dias_en_mes(2, 2005) == 28
    assert Fecha.dias_en_mes(2, 2004) == 29


def test_obtener_dias_transcurridos(date1: Fecha):
    assert date1.obtener_dias_transcurridos() == 28913


def test_dia_semana(date1: Fecha, date2: Fecha):
    assert date1.dia_semana == 4  # jueves
    assert date2.dia_semana == 0  # domingo


def test_es_fin_de_semana(date1: Fecha, date2: Fecha):
    assert not date1.es_fin_de_semana
    assert date2.es_fin_de_semana


def test_fecha_corta(date1: Fecha, date2: Fecha):
    assert date1.fecha_corta == '01/03/1979'
    assert date2.fecha_corta == '24/06/1984'


def test_date_string(date1: Fecha, date2: Fecha):
    assert str(date1) == 'JUEVES 1 DE MARZO DE 1979'
    assert str(date2) == 'DOMINGO 24 DE JUNIO DE 1984'


def test_add_dates(date1: Fecha):
    date = date1 + 145
    assert date.dia == 24
    assert date.mes == 7
    assert date.anio == 1979


def test_substract_two_dates(date1: Fecha, date2: Fecha):
    assert date2 - date1 == 1942


def test_substract_dias_to_date(date1: Fecha):
    date = date1 - 231
    assert date.dia == 13
    assert date.mes == 7
    assert date.anio == 1978


def test_dates_are_equal(date1: Fecha, date2: Fecha):
    assert date1 == date1
    assert date2 == date2
    assert not date1 == date2
    assert not date2 == date1


def test_date_is_greater_than_other_date(date1: Fecha, date2: Fecha):
    assert date2 > date1


def test_date_is_lower_than_other_date(date1: Fecha, date2: Fecha):
    assert date1 < date2
