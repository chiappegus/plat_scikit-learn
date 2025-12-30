
"""
cd ~/Desktop/Ora/BALANCES_GUS_PY
source env/Scripts/activate
cd /d/proyectos/plat_scikit-learn
"""



# cd ~/Desktop/Ora/BALANCES_GUS_PY

# source env/Scripts/activate

#en mi caso vuelvo : cd \d\ORA_proyectos\Seguimiento_PP_T_operativo

# python
import pyodbc
print(pyodbc.drivers())  # List all available ODBC drivers


# ['SQL Server', 'PostgreSQL ANSI(x64)', 'PostgreSQL Unicode(x64)', 'PostgreSQL ANSI', 'PostgreSQL Unicode', 'ODBC Driver 18 for SQL Server']

# AHORA SI => 'ODBC Driver 18 for SQL Server'

# $ py Inicio_check.py 
# ['SQL Server', 'PostgreSQL ANSI(x64)', 'PostgreSQL Unicode(x64)', 'PostgreSQL ANSI', 'PostgreSQL Unicode', 'ODBC Driver 18 for SQL Server',
#  'Microsoft Access Driver (*.mdb, *.accdb)', 'Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)', 'Microsoft Access Text Driver (*.txt, *.csv)', 
#  'Microsoft Access dBASE Driver (*.dbf, *.ndx, *.mdx)']

# SELECT TOP 100000 * 
# FROM DatoDiario 
# WHERE CDate(Fecha) > CDate('10/01/2025') 
# ORDER BY Fecha DESC
##Dar un año!!
# Excel connexion a base de datos :) 
# SELECT  * 
# FROM DatoDiario 
# WHERE CDate(Fecha) > CDate('10/01/2024') 
# ORDER BY Fecha DESC