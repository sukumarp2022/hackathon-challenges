# 🧩 Challenge 1: Employee Payroll Management System

## 🎯 Objective
Build a complete COBOL program that processes employee payroll data — from reading input records to generating a detailed payslip report — **with GitHub Copilot’s assistance** for code generation, debugging, and documentation.

---

## 🧠 Scenario
Your organization maintains employee details in a sequential file.  
The goal is to compute **gross pay**, **net pay**, and **department-level totals**, and then produce a formatted payroll report.

---

## 🧾 Requirements

### 1. Input File (EMPIN.DAT)
Each record contains the following fields:
```
EMP-ID (PIC X(5))
EMP-NAME (PIC X(20))
DEPT-CODE (PIC X(5))
BASIC-PAY (PIC 9(6)V99)
ALLOWANCE (PIC 9(6)V99)
DEDUCTION (PIC 9(6)V99)
```
### 2. Processing Logic
- Compute:
```
GROSS = BASIC + ALLOWANCE
NET = GROSS - DEDUCTION
```
- Maintain department-level totals for both GROSS and NET.
- Handle invalid or missing numeric fields gracefully (Copilot can assist with validation logic).
- Ensure proper COBOL structure: **IDENTIFICATION**, **DATA**, **PROCEDURE** divisions, and **FILE SECTION** definitions.

### 3. Output Report (PAYREP.TXT)
Generate a formatted report with:
```
EMP-ID | EMP-NAME | DEPT | GROSS | NET
```
At the end of the report, print:
```
DEPARTMENT TOTALS:
DEPT | TOTAL-GROSS | TOTAL-NET
```

### 4. Additional Requirements
- Include inline comments and meaningful section headers.
- Use **COPYBOOKS** for employee record structure.
- Add program-level documentation: author, purpose, and assumptions.

---

## 💡 Tips:

- Ask Copilot to generate the **COBOL skeleton** (IDENTIFICATION, ENVIRONMENT, DATA, PROCEDURE divisions).
- Use inline prompts such as  
  > *“# compute net salary for each employee and write to report”*  
  to get logic suggestions.
- Request Copilot to create **file handling routines** (OPEN, READ, WRITE, CLOSE).
- Use Copilot to **generate sample EMPIN.DAT** input data.
- Ask Copilot to **summarize or explain** the generated COBOL code.
- Use Copilot comments to **improve variable names and add comments automatically**.

---

## ✅ Expected Outcomes
- Developers understand how Copilot can **generate, refactor, and explain** COBOL code.
- Teams gain confidence in using Copilot for **legacy program enhancement** and **modernization initiatives**.
- Participants produce a working payroll system with structured and well-documented COBOL code.

---


