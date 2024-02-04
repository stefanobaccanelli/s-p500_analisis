#Importo las librerías as utilizar.
import yfinance as yf
import pandas as pd

#Guardo el link en una variable.
sp_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

#Extraigo los datos de la tabla del URL.
sp_df_list = pd.read_html(sp_url)

#Depuro solo la lista que me interesa ya que en la página hay 2 tablas.
sp_df = sp_df_list[0]

#Guardo los tickers en una lista con la que voy a iterar y obtener los valores de interés de cada acción.
sp_tickers_list = list(sp_df['Symbol'].values)

#Creo una lista vacía donde voy a guardar la información.
df = []

#Hago un For loop para obtener la información financiera asociada a cada acción.
#La búsqueda me devuelve muchos datos de los cuales voy a seleccionar algunos de interés. Estos se ven reflejados
#en las variables definidas dentro de la iteración.
# la iteración está acotada desde la posición 0 hasta el valor de la longitud de la lista de acciones.

for x in range(len(sp_tickers_list)):

#Asigno a la variable 'Ticker' el ticker que está en la posición 'x' de la lista.
    Ticker = yf.Ticker(sp_tickers_list[x])

#obtengo la información de la acción.

    info = Ticker.info

#Selecciono algunas caetgorías de interés para mi posterior análisis. Para esto realicé una corrida del codigo,
#obteniendo así la totalidad de la información. Esa información la analicé para ver cómo venía estucturada, y en base a
#eso depurar acorde.

    Ticket = info.get('symbol')
    Nombre = info.get('longName')
    Precio=info.get('currentPrice')
    Estado = info.get('state')
    Pais = info.get('country')
    Sector = info.get('sector')
    Industria = info.get('industry')
    Capitalización = info.get('marketCap')
    Riesgo = info.get('overallRisk')
    Beta = info.get('beta')
    Ultimo_Div = info.get ('lastDividendValue')
    Ratio_Pago = info.get('payoutRatio')
    Raio = info.get('dividendRate')
    Ult_año = info.get('52WeekChange')
    Ganancia_tot = info.get('totalRevenue')
    Acciones_tot = info.get('floatShares')

#Para obtener el nombre de los CEO de las empresas, tengo que acceder a un diccionario adentro del principal
#que contiene datos sobre los meimbros de los altos rangos.
#Hay 2 acciones para las cuales no se pudo descargar información, por lo que utilizo el siguiente 'IF'
#para poder seguir la iteración en caso de que el resultado al método 'Get' me devuelva el valor nulo ('NONE').

    off = info.get('companyOfficers',None)


    if off is not None:
        off = off[0]
        CEO = off.get('name')
    else:
        CEO='None'

#Asigno los valores de la variable al siguiente diccionario.

    info_dic = {'Ticker': Ticket,
                'Nombre':Nombre,
                'Precio': Precio,
                'Estado': Estado,
                'País': Pais,
                'Sector': Sector,
                'Industria': Industria,
                'Captialización': Capitalización,
                'Riesgo Total': Riesgo,
                'Beta': Beta,
                'Ult. Precio Div.': Ultimo_Div,
                'Payout Ratio': Ratio_Pago,
                'Ratio Dividendos': Raio,
                'Anual': Ult_año,
                'Revenue': Ganancia_tot,
                'Cantidad Acciones': Acciones_tot,
                'CEO': CEO

            }
#Con la función append, agrego los valores al final.

    df.append(info_dic)

#Transformo el diccionario en un Data Frame usando Pandas.

df = pd.DataFrame(df)

#Luego exporto ese DF a una carpeta en mis docuemntos como CSV. Los '*****' representan la ruta dónde se quiera
#guardar el documento CSV.

df.to_csv(r"********", index=False)





