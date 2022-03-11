 #  Получить от пользователя количество секунд. 
total_seconds  =  float(input('Bвeдитe количество секунд:  ')) 

#  Получить количество часов. 
hours  =  (total_seconds  // 3600) % 24
#  Получить количество оставшихся минут. 
minutes  =  (total_seconds  //  60) % 60  
 #  Получить количество оставшихся секунд. 
seconds  =  total_seconds  % 60 
days = ((total_seconds // 3600) // 24) % 365
years = (((total_seconds // 3600) // 24) // 365)
#  Показать результаты. 
print ('Boт время в  годах, днях, часах,  минутах и секундах:')
print ("Годы: ", years)
print ('Дней:', days )
print ('Часы:',  hours) 
print ('Минуты:',  minutes) 
print ('Секунды:',  seconds)
