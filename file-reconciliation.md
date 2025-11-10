# 📊 Challenge 3: File Reconciliation System

## 🎯 Objective
Develop a COBOL program to compare two data files — a master file and a transaction file — and generate a report showing matched, missing, and mismatched records.

---

## 🧠 Scenario
A financial institution receives daily transaction files from multiple sources.  
Your program must compare the **master file** (expected records) with the **incoming file** (actual records) and identify any differences.

---

## 🧾 Requirements

### Input Files
**Master File (MASTFILE.DAT)**  
```
ACC-NO X(10)
ACC-NAME X(25)
AMOUNT 9(7)V99
```

**Transaction File (TRNFILE.DAT)**  
```
ACC-NO X(10)
AMOUNT 9(7)V99
```


### Processing
- Read both files sequentially, assuming they are sorted by `ACC-NO`.  
- Compare records based on `ACC-NO`.  
  - If both exist and `AMOUNT` matches → mark as **MATCHED**.  
  - If both exist but `AMOUNT` differs → mark as **MISMATCHED**.  
  - If a record exists only in one file → mark as **MISSING**.  
- Maintain counters for each category.  

---

## 📊 Output
**Reconciliation Report (RECONREP.TXT)**  
```
ACC-NO | STATUS | MASTER-AMT | TRN-AMT
```

At the end, include totals such as:  
```
MATCHED: 999
MISMATCHED: 25
MISSING: 10
```

---

## ✅ Outcome
A COBOL program that demonstrates file comparison, sequential read logic, conditional processing, and report generation.
