#Se importan las bibliotecas 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Se le el csv de Indigenas del 2015, que contiene datos de población, salario,
#edad, lengua, alfabetismo, derechohabienda, vivienda, servicios básicos,
#bienes, actividad económica
indigenas = pd.read_csv('Indigenas.csv')
#Se muestran los datos de indigenas
print(indigenas)

#Los datos leídos anteriormente los integramos en un Data Frame
dfin=pd.DataFrame(indigenas)
#Se muestran los datos de dfin
print(dfin)

#Del Data Frame anterior, se seleccionaran las coulumnas  distintas a INEGI,
#ENT, MPO, TIPO2015 ya que no son datos relevantes para este estudio

#Primero se seleccionaran todas las columnas diferentes de INEGI
uno = dfin.loc[:,dfin.columns != 'INEGI']

#Los datos seleccionados anteriormente los integramos en un Data Frame
dfuno=pd.DataFrame(uno)

#Del Data Frame anterior, se seleccionaran todas las columnas diferentes ENT
dos = dfuno.loc[:,dfuno.columns != 'ENT']

#Los datos seleccionados anteriormente los integramos en un Data Frame
dfdos=pd.DataFrame(dos)

#Del Data Frame anterior, se seleccionaran todas las columnas diferentes MPO
tres = dfdos.loc[:,dfdos.columns != 'MPO']

#Los datos seleccionados anteriormente los integramos en un Data Frame
dftres=pd.DataFrame(tres)

#Del Data Frame anterior, se seleccionaran todas las columnas diferentes TIPO2015
cuatro = dftres.loc[:,dftres.columns != 'TIPO2015']

#Los datos seleccionados anteriormente los integramos en un Data Frame
dfindi=pd.DataFrame(cuatro)

#Seleccionamos todas las columnas que nos bridan la información relevante
datos_indi = ["NOMENT","NOMMUN","NOMTIPO","GRADOMARGI 2015","TPOBTOT","IPOB_INDI","Tp0a14h","Ipi0a14h","Tp15a24h","Ipi15a24h","Tp25a64h","Ipi25a64h","Tp65ymah","Ipi65ymah","Tp0a14m","Ipi0a14m","Tp15a24m","Ipi15a24m","Tp25a64m","Ipi25a64m","Tp65ymam","Ipi65ymam","IPHLI5","IP5_BILI","IP5_MONO","IP5_NEBILI","TP15_ALFAB","IP15_ALFA","TP15_ANALF","IP15_ANALFA","TP15NOESP","IP15_NEALFA","TP6A14_ASIS","PI6A14_ASIS","TP6A14_NASIS","PI6A14_NASIS","TP6A14_NEASI","PI6A14_NEASI","TP15_SINSTR","IP15_SINSTR","TP15_CPRIMAINCOM","IP15_CPRIMAINCOM","TP15_CPRIMACOMP","IP15_CPRIMACOMP","TP15_CSECUINCOM","IP15_CSECUINCOM","TP15_CSECUCOMP","IP15_CSECUCOMP","TP15_MSYSUP","IP15_MSYSUP","TP15_NENINST","IP15_NENINST","TPCDERSS","ISITIEDER","TPSDERSS","INOTIEDER","TPNESDERSS","INESPDERE","TPSEGPOP","ISEGPOP","TPIMSS","IIMSS","TPISSSTE","IISSSTE","TPPEMEX","IPEMEX","TPSSINSPRIV","ISSINSPRIV","TPOTASL","IOTASL","TPNACENT","ILNACENT","TPNACOENT","ILNACOTENT","TPNACNOES","ILNACNESP","TPECOACTIV","IPACTIVA","TPOCUPADA","IPOCUPADA","TPDESOCU","IPDESOCUP","TPECOINACT","IPINACTIV","TPECONE","IPNESPACT","TPSINGRESO","IPSINGRESO","TP1SM","IP1SM","TP1A2SM","IP1A2SM","TPMAS2SM","IPMAS2SM","TMLIBRE","IMLIBRE","TMSEPARADA","IMSEPARADA","TMDIVOR","IMDIVOR","TMVIUDA","IMVIUDA","TMCASADA","IMCASADA","TMSOLTERO","IMSOLTERO","TPHIJOSVIVOS","IPHIJOSVIVOS","TVIVPARHAB","INUM_VIV","TVP_AGUENT","IAGUAENTNVI","TVP_SINAGUENT","ISINAGUAENTNVI","TVP_NESAGUENT","INESAGUAENTNVI","TVP_DRENAJ","ICDRENAJENV","TVP_SINDRENAJ","ISINDRENAJENV","TVP_NESDRENAJ","INESDRENAJENV","TVP_ELECTR","ICONELECTNV","TVP_SINELECTR","ISINELECTNV","TVP_NESELECTR","INESELECTNV","TVP_PISTIERR","IPISOTIERNV","TVP_RADIO","ICONRADIONV","TVP_TV","ICONTELEVNV","TVP_REFRI","ICONREFRINV","TVP_TELEF","ICONTELEFNV","TVP_LAVA","ICONLAVNV","TVP_COMPU","ICONCOMPNV","hALFA","mALFA","hANALFA","mANALFA","hALFANESP","mALFANESP","hPEA","mPEA","hPOCUPA","mPOCUPA","hPDESOCU","mPDESOCU","hPEI","mPEI","hPNESPACTI","mPNESPACTI","hTbil","mTbil","hBILI","mBILI","hMONO","mMONO","hMONsp","mMONsp"]
datos_indige = dfindi[datos_indi]

#Los datos seleccionados anteriormente los integramos en un Data Frame
dfindigeneral=pd.DataFrame(datos_indige)
#Muestra los datos del Data Frame integrado anteriormente - dfindigeneral -
print(dfindigeneral)


#                    Población nacional e indígena
#____________________________________________________________________________
#Se seleccionan los datos de NOMENT de todos los estados y se suman de acuerdo
#con la población indígena
print("Población indígena por estados")
acumindi=dfindigeneral.groupby('NOMENT')['IPOB_INDI'].sum()
#Se muestran los datos
print(acumindi)
print("")
#Se seleccionan los datos de NOMENT de todos los estados y se suman de acuerdo
#con la población nacional
print("Población nacional por estados")
acumnal=dfindigeneral.groupby('NOMENT')['TPOBTOT'].sum()
#Se muestran los datos
print(acumnal)
print("")

#                                  Valores
#____________________________________________________________________________

#Se seleccionan los datos donde NOMENT coincida con cada uno de los 4 estados seleccionados,
#Chiapas, Distrito Federal, Nuevo Léon, Oaxaca

es_Chiapas=dfindigeneral["NOMENT"]== "Chiapas"
es_CDMX=dfindigeneral["NOMENT"]== "Distrito Federal"
es_NuevoLeon=dfindigeneral["NOMENT"]== "Nuevo Leon"
es_Oaxaca=dfindigeneral["NOMENT"]== "Oaxaca"

#Con los datos seleccionados anteriormente se incorporaran en una variable
cuatro_estados=dfindigeneral[es_Chiapas | es_CDMX | es_NuevoLeon | es_Oaxaca]

#Con la variable cuatro_estados se hará un Data Frame, él que se utilizará
#durante el programa
df4estados=pd.DataFrame(cuatro_estados)

#Se seleccionan los estados por separado para obtener cuántos municipios se tienen 
#por estado y la población de estos
mun_Chiapas = dfindigeneral[es_Chiapas]
mun_CDMX = dfindigeneral[es_CDMX]
mun_NuevoLeon = dfindigeneral[es_NuevoLeon]
mun_Oaxaca = dfindigeneral[es_Oaxaca]


#                       Estados, municipios y población
#____________________________________________________________________________
#De la seleccion de datos de Chiapas - mun_Chiapas -, se realiza la suma de la población
#de cada uno y se obtiene cuantos hay en el estado.
print("Población de los municipios de Chiapas")
acum1=mun_Chiapas.groupby('NOMMUN')['IPOB_INDI'].sum()
mun_cant_Chiapas = mun_Chiapas["NOMMUN"].count()
#Se muestran los datos de acum1 y mun_cant_Chiapas
print(acum1)
print("Municipios de Chiapas:",mun_cant_Chiapas)
print(" ")

#De la seleccion de datos de CDMX - mun_CDMX -, se realiza la suma de la población
#de cada uno y se obtiene cuantos hay en el estado.
print("Población de los municipios de CDMX")
acum2=mun_CDMX.groupby('NOMMUN')['IPOB_INDI'].sum()
mun_cant_CDMX = mun_CDMX["NOMMUN"].count()
#Se muestran los datos de acum2 y mun_cant_CDMX
print(acum2)
print("Municipios de CDMX:",mun_cant_CDMX)
print(" ")

#De la seleccion de datos de Nuevo León - mun_NuevoLeon -, se realiza la suma de la población
#de cada uno y se obtiene cuantos hay en el estado.
print("Población de los municipios de NuevoLeon")
acum3=mun_NuevoLeon.groupby('NOMMUN')['IPOB_INDI'].sum()
mun_cant_NuevoLeon = mun_NuevoLeon["NOMMUN"].count()
#Se muestran los datos de acum3 y mun_cant_NuevoLeon
print(acum3)
print("Municipios de Chiapas:",mun_cant_Chiapas)
print(" ")

#De la seleccion de datos de Oaxaca - mun_Oaxaca -, se realiza la suma de la población
#de cada uno y se obtiene cuantos hay en el estado.
print("Población de los municipios de Oaxaca")
acum4=mun_Oaxaca.groupby('NOMMUN')['IPOB_INDI'].sum()
mun_cant_Oaxaca = mun_Oaxaca["NOMMUN"].count()
#Se muestran los datos de acum4 y mun_cant_Oaxaca
print(acum4)
print("Municipios de Oaxaca:",mun_cant_Oaxaca)
print(" ")

#De la seleccion de datos de los estados de: Chiapas, CDMX, Nuevo León y Oaxaca en
#- df4estados - se realiza la suma de la población de cada uno 
print(" Población Total de Chiapas, CDMX, Nuevo León y Oaxaca")
acum=df4estados.groupby('NOMENT')['IPOB_INDI'].sum()
#Se muestran los datos de acum
print(acum)
print(" ")

#                Lengua indígena y condición de habla española
#____________________________________________________________________________
#De la seleccion de datos de los estados de: Chiapas, CDMX, Nuevo León y Oaxaca en
#- df4estados - se realiza la suma de la población de 5 años y más que habla alguna lengua
#indígena de cada estado

print("Lengua indígena y condición de habla española")
print("población de 5 años y más que habla alguna lengua indígena")
acumlen=df4estados.groupby('NOMENT')['IPHLI5'].sum()
#Se muestran los datos de acumlen
print(acumlen)


#                     Características de la vivienda
#____________________________________________________________________________
#De la seleccion de datos de los estados de: Chiapas, CDMX, Nuevo León y Oaxaca en
#- df4estados - se realiza la suma de la población de 5 años y más que habla alguna lengua
#indígena de cada estado

print("Características de la vivienda")
print("Total de viviendas particulares")
acumviv=df4estados.groupby('NOMENT')['INUM_VIV'].sum()
#Se muestran los datos de acumviv
print(acumviv)

#                                  Gráficas
#____________________________________________________________________________

#Se selecciona los datos en que NOMENT corresponda con el estado deseado
dfindiestado = dfindigeneral.loc[(dfindigeneral['NOMENT']== 'Aguascalientes')]
#print(dfindiestado)
print(" ")
#Se cuenta cuantos municipios se tienen con: población indígena dispersa, con presencia indígena
#indígena y sin población indígena
tipomun = dfindiestado.groupby(['NOMTIPO']).size().reset_index(name='Cantidad')
#print(tipomun)

#Se grafica mediante la función sns
f = sns.catplot(x='NOMTIPO',y='Cantidad',data=tipomun,kind='bar',palette='Paired')

#Se muestra la gráfica
#plt.show()

#Se guarda la gráfica como imagen con formato png, pero si se desea guardar
#se debe comentar plot.show()
#plt.savefig('Aguascalientes.png')
