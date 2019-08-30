import pymorphy2
import num2words

var_date = '11.06.1973'
day_tens = var_date [0]
day_ones = var_date [1]
month = var_date [3:5]
year = var_date [6:10]
dict_month = {"01": "январь", "02": "февраль", "03": "март", "04": "апрель", "05": "май", "06": "июнь",
       "07": "июль", "08": "август", "09": "сентябрь", "10": "октябрь", "11": "ноябрь", "12": "декабрь"
       }
dict_date_tens = {"2":"двадцать", "3":"тридцать"}
day_tens_str = ''
if int(day_tens) is 1:
    day_ones = day_ones + day_tens
elif int(day_tens) is 2:
    day_tens_str = dict_date_tens['2']
elif int(day_tens) is 3:
    day_tens_str = dict_date_tens['3']
morph = pymorphy2.MorphAnalyzer()
month_str = morph.parse(dict_month[str(month)])[0]
day_ones_str = num2words.num2words(day_ones, lang = 'ru', ordinal = True)
temp = morph.parse(day_ones_str)[0]
print('{0} {1} {2} {3} года'.format(day_tens_str, temp.inflect({'neut', 'sing'}).word, month_str.inflect({'sing', 'gent'}).word, year))