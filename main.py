import streamlit as st
import datetime
from decimal import Decimal

header = st.container()
kontonummer1, betrag, gebuehr = st.columns(3)
auswahl = st.container()
r_col1, r_col2, = st.columns(2)
r_col3, r_col4 = st.columns(2)
r_col5, r_col6, r_col7 = st.columns(3)
generatedFile =st.container()

with header:
    st.title('Rückläufer Test')

with kontonummer1:
    ruck_iban1 = st.text_input('IBAN','DE35664900000022805304')
    
with betrag:
    ruck_betrag = st.text_input('Betrag in Euro','100,00')
    
with gebuehr:
    ruck_gebuehr = st.text_input('RLS-Gebühr in Euro','5,00')

summe1 = Decimal(ruck_betrag.replace(',','.'))
summe2 = Decimal(ruck_gebuehr.replace(',','.'))
r_betrag_f = summe1
r_gebuehr_f = summe2
r_summe1 = summe1+summe2
r_summe =str(r_summe1)
r_summe =r_summe.replace(".",",")

    
with auswahl:
    option =st.selectbox(
    'Rückläufergrund?',
    ('901:   Kontonummer fehlerhaft (ungültige IBAN)','902:   Konto aufgelöst','903:   Konto gesperrt','904:   Zahlungsart für diesen Kontotyp nicht zugelassen','905:   Transaktions-Code unzulässig oder falsches Dateiformat','906:   Rückgabe mangels Deckung','907:   Doppeleinreichung','908:   Adresse des Zahlungsempfängers fehlt oder ist unvollständig','909:   Kein gültiges Mandat','910:   InMandate Fehlerhafte oder unvollständige Mandats-information','911:   Absender unbekannt/Falsche Creditor ID','912:   Lastschriftwiderspruch durch den Zahlungspflichtigen','913:   Kontoinhaber verstorben','914:   Sonstige Gründe','915:   Bankidentifikationscode fehlerhaft ungültige BIC)','916:   Cut-Off-Zeit vor Dateiempfang erreicht','917:   Ablehnung auf Grund von aufsichtsrechtlichen Vorschriften','930:   Zahlungpflichtiger ist ein Verbraucher (kein Kommerzkunde)','931:   Falscher Auftragstyp / Falsche Lastschriftart'))
    
    
if option == '901:   Kontonummer fehlerhaft (ungültige IBAN)':
    erstesWort = "901"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]
    
if option == '902:   Konto aufgelöst':
    erstesWort = "902"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]

if option == '903:   Konto gesperrt':
    erstesWort = "903"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]
    
if option == '904:   Zahlungsart für diesen Kontotyp nicht zugelassen':
    erstesWort = "904"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]

if option == '905:   Transaktions-Code unzulässig oder falsches Dateiformat':
    erstesWort = "905"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]
    
if option == '906:   Rückgabe mangels Deckung':
    erstesWort = "906"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]

if option == '907:   Doppeleinreichung':
    erstesWort = "907"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]
    
if option == '908:   Adresse des Zahlungsempfängers fehlt oder ist unvollständig':
    erstesWort = "908"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]
    
if option == '909:   Kein gültiges Mandat':
    erstesWort = "909"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]
    
if option == '910:   InMandate Fehlerhafte oder unvollständige Mandats-information':
    erstesWort = "910"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]

if option == '911:   Absender unbekannt/Falsche Creditor ID':
    erstesWort = "911"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]
    
if option == '912:   Lastschriftwiderspruch durch den Zahlungspflichtigen':
    erstesWort = "912"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]

if option == '913:   Kontoinhaber verstorben':
    erstesWort = "913"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]
    
if option == '914:   Sonstige Gründe':
    erstesWort = "914"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]

if option == '915:   Bankidentifikationscode fehlerhaft ungültige BIC':
    erstesWort = "915"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]
    
if option == '916:   Cut-Off-Zeit vor Dateiempfang erreicht':
    erstesWort = "916"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]
    
if option == '917:   Ablehnung auf Grund von aufsichtsrechtlichen Vorschriften':
    erstesWort = "917"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]

if option == '930:   Zahlungpflichtiger ist ein Verbraucher (kein Kommerzkunde)':
    erstesWort = "930"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]
    
if option == '931:   Falscher Auftragstyp / Falsche Lastschriftart':
    erstesWort = "931"
    zweitesWort1 = option
    zweitesWort =zweitesWort1[7:]
    
    
with r_col1:
    r_today1 = datetime.date.today()
    r_VDatum=st.date_input('Datum Valuta', r_today1)
    r_yearVv = r_VDatum.strftime("%Y")
    r_yearV =r_yearVv[2:]
    r_monthV = r_VDatum.strftime("%m")
    r_dayV =r_VDatum.strftime("%d")


with r_col2:
    r_today = datetime.date.today()
    r_BDatum=st.date_input('Datum Buchung', r_today)
    r_yearBb = r_BDatum.strftime("%Y")
    r_yearB =r_yearBb[2:]
    r_monthB = r_BDatum.strftime("%m")
    r_dayB =r_BDatum.strftime("%d")
    
with r_col3:
    ruck_ref = st.text_input('Interne Referenz','Bsp.: A1.554.602.46596')

with r_col4:
    ruck_mandref =st.text_input('VWZ 1 (22) / Mandatsreferenz','Bankrückläufer')
    
with r_col5:
    r_kontoinhaber = st.text_input('Kontoinhaber', 'John J. Rambo')

with r_col6:
    r_bic = st.text_input('BIC','BELADEBE')

with r_col7:
    r_konto2option = st.text_input('IBAN','DE02100500000054540402')
    
    
with generatedFile:
    st.write(":20:DEUTDEMMXXX")
    st.write(":25:"+ruck_iban1)
    st.write(":28C:00001/1")
    st.write(":60F:C190501EUR0,00")
    st.write(":61F:"+r_yearV+r_monthV+r_dayV+r_monthB+r_dayB+"D"+r_summe+"NRTINONREF/OCMT/EUR"+ruck_betrag+"//CHGS/EUR"+ruck_gebuehr+"/")
    st.write(":86:109?00LS RUECKBELASTUNG?109250?20EREF+"+ruck_ref+"?22MREF+?23CRED+DE98ZZZ09999999999?24COAM+     "+ruck_gebuehr+"?250AMT+     "+ruck_betrag+"?26SVWZ+ RUECKLASTSCHRIFT?27"+zweitesWort+"?28ZINSAUSGLEICH-FREMDENTGELT?29     "+ruck_gebuehr+" EURO?30"+r_bic+"?31"+r_konto2option+"?32"+r_kontoinhaber+"34"+erstesWort+"?60EIGENENTGELT 00000,00 EURO")
    st.write(':62F:C180716EUR0')
    
    
    
    



