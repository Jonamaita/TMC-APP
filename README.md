# TMC APP

Es una aplicación para consultar el valor de la tasa de interés máxima convencional.

Se debe especificar al monto en UF, el plazo en días y la fecha en la que desea saber el TMC.

Desarrollada con Django Framework 2.2.13.



https://tmcs-app.herokuapp.com/



# Tipos de casos

La aplicación solo toma en consideración los siguientes tipos de tasa de interés máximo convencional:



### Operaciones reajustable moneda nacional

**Tipo**= 21 # Menores a 1 año

**Tipo** = 22 # Igual o mayor a 1 año y superior a 2000 Uf

**Tipo** = 24 # Igual o mayor a 1 año e inferior o igual a 2000 Uf



### Operaciones no reajustable moneda nacional

**Tipo** = 25 # Menos de 90 días y superior a 5000 Uf

**Tipo** = 26 # Menos de 90 días e inferior o igual a 5000 Uf

**Tipo** = 34 # 90 días o mas y superior a 5000uf

**Tipo** = 35 # 90 días o mas e inferior o igual a 5000 Uf y superior a 200 Uf

**Tipo** = 44 # 90 días o mas e inferior o igual a 200 Uf y superior a 50 Uf

**Tipo** = 45 # 90 días o mas inferior o igual a 50 Uf



### Operaciones Expresadas en moneda extranjera

**Tipo** = 41 # Operaciones expresadas en moneda extranjera Inferiores o iguales al equivalente de 2.000 unidades de fomento

**Tipo** = 42 # Operaciones expresadas en moneda extranjera Superiores al equivalente de 2.000 unidades de fomento

