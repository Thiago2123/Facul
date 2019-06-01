segundos_entrada = input("Digite os segundos para converter: ")
total_segundos = int(segundos_entrada)



horas = total_segundos // 3600
segundos_rest = total_segundos % 3600

minutos = segundos_rest //60
seg_rest_final= segundos_rest %60

dia = horas // 24
horas_rest = horas % 24
print(dia, "dias, ", horas_rest, "horas, ", minutos, "minutos e", seg_rest_final, "segundos.")



