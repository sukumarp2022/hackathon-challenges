# 🏭 Challenge 5: Inventory Management System

## 🎯 Objective
Build a COBOL program to manage inventory by processing stock transactions (purchases and sales) and generating a final stock report.

---

## 🧠 Scenario
A retail company maintains an **inventory master file** with item details.  
Each day, it processes a **transaction file** containing purchase and sale records.  
Your program must update stock quantities and produce a detailed summary.

---

## 🧾 Requirements

### Input Files
**Inventory Master File (INVMST.DAT)**  
```
ITEM-CODE X(10)
ITEM-NAME X(25)
STOCK-QTY 9(5)
UNIT-PRICE 9(5)V99
```

**Transaction File (INVTRN.DAT)**  
```
ITEM-CODE X(10)
TRN-TYPE X(5) --> BUY / SELL
TRN-QTY 9(5)
```

### Processing
- Match transactions with master records using `ITEM-CODE`.  
- Update stock:  
```
IF BUY ADD TRN-QTY TO STOCK-QTY
IF SELL SUBTRACT TRN-QTY FROM STOCK-QTY
```
- Flag items that go below zero stock.  
- Write an updated master file (`INVNEW.DAT`).  

---

## 📊 Output
**Inventory Report (INVREP.TXT)**  
```
ITEM-CODE | ITEM-NAME | STOCK-QTY | UNIT-PRICE | VALUE
```
At the end, include totals:  
```
TOTAL STOCK VALUE: 9999999.99
ITEMS BELOW REORDER LEVEL: NN
```

---

## ✅ Outcome
A COBOL program demonstrating file handling, arithmetic operations, conditional logic, and report generation for inventory control.
