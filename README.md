# My_First_Machine_Learning_S25086

#Dla regresji liniowej:

R²: 0.5757877060324521
MSE: 0.5558915986952425
Coefficients: [ 4.48674910e-01  9.72425752e-03 -1.23323343e-01  7.83144907e-01
 -2.02962058e-06 -3.52631849e-03 -4.19792487e-01 -4.33708065e-01]

Coefficients (współczynniki) w przypadku regresji liniowej określają o ile zmieni się wartość celu (w tym ćwiczeniu ceny domów) jeśli wartość danej przykładowej cechy wzrośnie o jedną jednostkę, 
zakładając że wszystkie inne cechy pozostają niezmienione. W przypadku datasetu w tym ćwiczeniu, jako że dane są liniowe model określa czy wartość ceny domów wzrasta (dodatni wskaźnik), 
czy spada (ujemny wskaźnik) w porównaniu do innej przykładowej cechy. Im wyższa wartość współczynnika tym cena domów jest bardziej zależna od tej konkretnej badanej cechy.

==============================================================================

#Dla Random Forest:

Accuracy: 1.0
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        10
           1       1.00      1.00      1.00         9
           2       1.00      1.00      1.00        11

    accuracy                           1.00        30
   macro avg       1.00      1.00      1.00        30
weighted avg       1.00      1.00      1.00        30

==============================================================================

#Dla Naiwny klasyfikator Bayesa

Accuracy: 0.9780405405405406
              precision    recall  f1-score   support

           0       0.98      0.96      0.97       195
           1       0.98      0.99      0.99       191
           2       0.97      0.99      0.98       206

    accuracy                           0.98       592
   macro avg       0.98      0.98      0.98       592
weighted avg       0.98      0.98      0.98       592

Text: 'From: LMARSHA@cms.cc.wayne.edu (Laurie Marshall)
Subject: Re: Where's Roger?
Org...'
Real state: rec.sport.hockey | Prediction: rec.sport.hockey
Text: 'From: prb@access.digex.com (Pat)
Subject: Re: Stephen Hawking Tours JPL
Organiza...'
Real state: sci.space | Prediction: sci.space
Text: 'From: dchhabra@stpl.ists.ca (Deepak Chhabra)
Subject: Re: In memoriam: Dan Kelly...'
Real state: rec.sport.hockey | Prediction: rec.sport.hockey
Text: 'From: neideck@nestvx.enet.dec.com (Burkhard Neidecker-Lutz)
Subject: Re: Rumours...'
Real state: comp.graphics | Prediction: comp.graphics
Text: 'From: hammerl@acsu.buffalo.edu (Valerie S. Hammerl)
Subject: Re: Oilers for sale...'
Real state: rec.sport.hockey | Prediction: rec.sport.hockey

==============================================================================

#Wnioski

Najszybszymi modelami był model regresji liniowej i Rajdom Forest, klasyfikator Bayesa trwał ok. 1 sekundę dłużej z uwagi na fakt, 
że dataset ma większą ilość danych od pozostałych.
Największy wskaźnik accuracy ma Random Forest (1.0).
Bez dodatkowego wyszukiwania informacji najłatwiejszym modelem do zrozumienia wydaje się model regresji liniowej 
z uwagi na możliwość wydrukowania współczynników i fakt, że model opiera się na danych liniowych (ciągłych). 
Dane w nim można zinterpretować numerycznie patrząc na wartości, nie trzeba mieć na uwadze rodzaj danych w kolumnie, 
czy ich znaczenie, tak jak przy klasyfikacji.
Najbardziej wymagający był dataset "20newsgroups" z uwagi na najdłużej kompilujący się kod, 
i fakt że kod testowy opierał się na wartościach numerycznych, a nie na tekście i program na początku drukował błąd.
Zależnie od projektu wybrałbym model Regresji liniowej dla zadań regresyjnych jako taki baseline, a dla zadań klasyfikacji
najpewniej model RandomForest z uwagi na możliwość bezpośredniego wglądu do utworzonego drzewa.
