import datetime
import pytz

year = 2023
month = 6
day = 5

#craindo a variável do tipo datetime
d = datetime.date(year, month, day)

print(d)

#função que retorna o ano, mes e dia atual
today = datetime.date.today()
print(f"today[{today}]")

#retona o dia da semana baseado no data atual como [0-6]
week = today.weekday()
print(f"week:{week}")

#retona o dia da semana baseado no data atual como [1-7]
week = today.isoweekday()
print(f"iso week:{week}")

# a função timedelta represena uma duração de tempo
new_date = today + datetime.timedelta(days=4)
print(f"new date [{new_date}]")

#cálculo de quandias dias faltam par aniversário no ano corrente
bith_day = datetime.date(2020,7,3)
till_bith_day = bith_day - today

print(till_bith_day)

#data e hora atual pelo tz padrão
dt_utcnow = datetime.datetime.now(tz = pytz.UTC)

#data e hora atual para US/Mountein
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))

print(f"Day now here [{dt_utcnow}]\nDay now in US/Mountain [{dt_mtn}]")

#converter data para string
dt_str = dt_mtn.strftime('%B %d, %y')
print(dt_str)

#converter data em string para formato datetime
dt = datetime.datetime.strptime(dt_str,'%B %d, %y')
print(dt)


