ignore , dia_inicio = input().split()
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(':'))
ignore , dia_final = input().split()
hora_final, minuto_final, segundo_final = map(int, input().split(':'))

total_dias = int(dia_final) - int(dia_inicio)
total_horas = hora_final - hora_inicio
total_minutos = minuto_final - minuto_inicio
total_segundos = segundo_final - segundo_inicio

if total_segundos < 0:
    total_segundos += 60
    total_minutos -= 1
if total_minutos < 0:
    total_minutos += 60
    total_horas -= 1
if total_horas < 0:
    total_horas += 24
    total_dias -= 1
if total_dias < 0:
    total_dias += 30
print(f'{total_dias} dia(s)')
print(f'{total_horas} hora(s)')
print(f'{total_minutos} minuto(s)')
print(f'{total_segundos} segundo(s)')
