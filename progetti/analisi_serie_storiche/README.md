# 📈 Analisi delle Serie Storiche delle Commodities

## 🔍 Obiettivo del Progetto

Questo progetto mira ad analizzare le serie storiche dei prezzi delle commodities fornite dalla World Bank tramite la piattaforma DBNomics. 
I dati vengono estratti attraverso l'API di DBNomics, elaborati e analizzati per identificare trend e relazioni tra le serie.

## 📑 Descrizione del Processo

1. **Estrazione Dati:** Utilizzo dell'API di DBNomics per raccogliere le serie di interesse.
2. **Pulizia e Trasformazione:** Normalizzazione dei dati, estrazione di informazioni chiave e creazione di un dataset strutturato.
3. **Filtro delle Serie:** Selezione delle serie da analizzare tramite input utente.
4. **Analisi Statistica:** Calcolo di media, varianza, covarianza e distribuzione dei quantili.
5. **Visualizzazione Grafica:** Generazione di grafici per evidenziare trend e correlazioni.

## 📂 Struttura del Repository

```
progetto_analisi_serie_storiche/
│── README.md  # Questo file
│── Notebook_agostino_fontana.ipynb  # Jupyter Notebook con l'analisi
│── modulo_agostino_fontana/
│   │── __init__.py  # Per rendere il modulo importabile
│   │── modulo_agostino_fontana.py  # Funzioni personalizzate
│── OUT/  # Cartella per i risultati
│── requirements.txt  # Lista delle librerie necessarie
```

## 🛠 Tecnologie Utilizzate

- **Linguaggi:** Python
- **Librerie:** Pandas, NumPy, Matplotlib, Seaborn
- **API:** DBNomics
- **Ambiente:** Jupyter Notebook

## 📊 Risultati Previsti

- Rappresentazioni grafiche dell’andamento storico delle commodities
- Relazioni tra le serie analizzate
- Insight sui trend di mercato

## 📜 Requisiti

Per eseguire il progetto, installa le dipendenze con:
```bash
pip install -r requirements.txt
```

## 📝 Autore

- **Agostino Fontana**

---
💡 *Se trovi utile questo progetto, lascia una ⭐ su GitHub!*
