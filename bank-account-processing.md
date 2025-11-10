# 🏦 Challenge 2: Bank Account Transaction Processor

## 🎯 Objective
Create a COBOL program to update customer account balances based on daily transactions and produce a summary report.

---

## 🧠 Scenario
A bank maintains a **master account file** and receives a **daily transaction file**.  
Your program must apply all deposits and withdrawals, update balances, and generate summary and error reports.

---

## 🧾 Requirements

### Input Files
**Master File (ACCMST.DAT)**  
```
ACC-NO X(10)
ACC-NAME X(25)
BALANCE 9(7)V99
```

**Transaction File (ACCTRN.DAT)**  
```
ACC-NO X(10)
TRN-TYPE X(6) --> DEPOSIT / WITHDRAW
TRN-AMT 9(7)V99
```

### Processing
- Match each transaction with the corresponding account number.  
- Update balance:  
```
IF DEPOSIT ADD TRN-AMT TO BALANCE
IF WITHDRAW SUBTRACT TRN-AMT FROM BALANCE
```
- Flag transactions for unknown accounts or negative balances.  
- Write an updated master file (`ACCNEW.DAT`).

---

## 📊 Output
**Summary Report (ACCSUM.TXT)**  
```
ACC-NO | NAME | TYPE | AMOUNT | NEW-BAL | STATUS
```
Include totals for deposits, withdrawals, and failed transactions.

**Error Log (ACCERR.TXT)**  
List invalid or unmatched transactions with account numbers and reasons.

---

## ✅ Outcome
A working COBOL program demonstrating file handling, record matching, transaction processing, and basic validation.
