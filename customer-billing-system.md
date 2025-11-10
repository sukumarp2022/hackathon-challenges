# 💰 Challenge 4: Customer Billing System

## 🎯 Objective
Create a COBOL program that generates monthly bills for customers based on their usage details and applicable rates.

---

## 🧠 Scenario
A telecom company maintains customer data and monthly usage records.  
Your task is to read both files, calculate total charges, and produce individual customer bills along with a summary report.

---

## 🧾 Requirements

### Input Files
**Customer Master File (CUSTMST.DAT)**  
```
CUST-ID X(6)
CUST-NAME X(25)
PLAN-CODE X(5)
RATE-PER-UNIT 9(4)V99
```

**Usage File (USAGE.DAT)**  
```
CUST-ID X(6)
UNITS 9(5)
MONTH X(6)
```

### Processing
- Match usage records with corresponding customers by `CUST-ID`.  
- Compute:  
```
BILL-AMOUNT = UNITS * RATE-PER-UNIT
```
- Handle customers with no usage (generate zero bill).  
- Flag usage records with no matching customer.  

---

## 📊 Output
**Customer Bill Report (BILLREP.TXT)**  
```
CUST-ID | NAME | UNITS | RATE | BILL-AMOUNT
```
At the end, show totals for:
```
TOTAL CUSTOMERS BILLED: NNN
TOTAL REVENUE: 999999.99
UNMATCHED USAGE RECORDS: NN
```

---

## ✅ Outcome
A COBOL program that demonstrates file matching, calculations, formatted reporting, and error handling for missing data.
