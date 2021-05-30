from celsiusTofarenheit import CelsiueToFarenheit

celsius = float(input('Insira temperatura em Celsius: '))

c = CelsiueToFarenheit()
fahrenheit = c.convert(celsius)

print('%0.1fºC é igual a %0.1fºF'%(celsius,fahrenheit))