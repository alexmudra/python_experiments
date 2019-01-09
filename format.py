from datetime import datetime


# Ресурс про форматування https://pyformat.info/
# Інформація про форматування різних елементів та об'єктів за допомогою %(старий підхід) і .format(новий підхід)



#Базове форматування із string
print("Зразок із старим підходом %:", '%s %s'% ('one', 'two'))
'''
Зразок із старим підходом %: one two
'''
print("Зразок з ф-ією .format:", '{} {}'.format('one', 'two'))
'''
Зразок з ф-ією format: one two
'''
#-----------------------------------------------------------------------------
#Базове форматування із малими числами
print("Зразок із старим підходом %:", '%d %d'% (1, 2))
'''
Зразок із старим підходом %: 1 2
'''
print("Зразок з ф-ією .format:", '{} {}'.format(1, 2))
'''
Зразок з ф-ією format: 1 2
'''

#-----------------------------------------------------------------------------
'''
Value conversion
The new-style simple formatter calls by default the __format__() method of an object for its representation. 
If you just want to render the output of str(...) or repr(...) you can use the !s or !r conversion flags.

In %-style you usually use %s for the string representation but there is %r for a repr(...) conversion.

'''

class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'
print("Зразок із старим підходом %:", '%s %r' % (Data(), Data()))
'''
Зразок із старим підходом %: str repr
'''
print("Зразок з ф-ією format:", '{0!s} {0!r}'.format(Data()))
'''
Зразок з ф-ією .format: str repr
'''
#------------------------------------------------------------------------------

'''
In Python 3 there exists an additional conversion flag that uses the output of repr(...) but uses ascii(...) instead
'''
class Data(object):

    def __repr__(self):
        return 'räpr'

print("Зразок із старим підходом %:", '%r %a' % (Data(), Data()))
'''
Зразок із старим підходом %: räpr r\xe4pr
'''
print("Зразок з ф-ією .format:",'{0!r} {0!a}'.format(Data()))
'''
Зразок з ф-ією .format: räpr r\xe4pr
'''
#---------------------------------------------------------------------------

'''
Padding and aligning strings
By default values are formatted to take up only as many characters as needed to represent the content. 
It is however also possible to define that a value should be padded to a specific length.

Unfortunately the default alignment differs between old and new style formatting. 
The old style defaults to right aligned while for new style it's left.
'''
#Align right: Вирівнювання стрінги по правому краю

print("Зразок вирівнювання по правому краю за старим підходом %:",'%10s' % ('test',))
'''
Зразок вирівнювання по правому краю за старим підходом %:       test
'''
print("Зразок вирівнювання по правому краю із ф-ією .format:",'{:>10}'.format('test'))
'''
Зразок вирівнювання по правому краю із ф-ією .format:       test
'''

#Align left: Вирівнювання стрінги по лівому краю
print("Зразок вирівнювання по правому краю за старим підходом %:",'%-10s' % ('test',))
'''
Зразок вирівнювання по правому краю за старим підходом %: test      
'''

print("Зразок вирівнювання по правому краю із ф-ією .format:",'{:10}'.format('test'))
'''
Зразок вирівнювання по правому краю із ф-ією .format: test      
'''
#-------------------------------------------------------------------------------------

#Приклад форматування дати
#The components of a date-time can be set separately:

dt = datetime(2001, 2, 3, 4, 5)
current_date_and_time = datetime(2019, 1, 9, 19, 39)

print("Зразок форматування дати із ф-ією .format (з переменнію dt):",'{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))
'''
Зразок форматування дати із ф-ією .format (з переменнію dt): 2001-02-03 04:05
'''
print("Зразок форматування дати із ф-ією .format (з переменнію current_date_and_time ):",'{:{dfmt} {tfmt}}'.format(current_date_and_time, dfmt='%Y-%m-%d', tfmt='%H:%M'))
'''
Зразок форматування дати із ф-ією .format (з переменнію current_date_and_time ): 2019-01-09 19:39
'''
