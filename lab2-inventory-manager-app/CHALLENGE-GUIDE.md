# 🧪 Lab 2: Legacy Inventory Manager — Refactoring & Advanced Copilot

## Overview
You have a **legacy Inventory Management System** that's a mess — monolithic code, no tests, poor performance, bad patterns. Your mission is to use GitHub Copilot's advanced capabilities to **refactor**, **modernize**, and extend this codebase using Coding Agent, Custom Agents, Orchestration, and MCP.

**Estimated Time:** 60–75 minutes

---

## Prerequisites
- VS Code with GitHub Copilot extension (Chat + Agent)
- Python 3.10+
- A GitHub repository (you'll push this code and use Copilot Coding Agent)
- This folder open in VS Code

### Setup
```bash
cd lab2-inventory-manager-app
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python inventory.py          # Try the CLI - explore the mess!
```

### Explore the Codebase First
Before starting, read through `inventory.py` and `utils.py`. Notice:
- ❌ God function pattern — everything in one file
- ❌ No type hints anywhere
- ❌ Repeated `load()`/`save()` calls (data loaded from disk every function call)
- ❌ Manual bubble sort instead of `sorted()`
- ❌ Manual CSV handling instead of `csv` module
- ❌ Magic numbers for discounts
- ❌ Duplicated load/save logic between files
- ❌ No error handling or input validation
- ❌ No tests
- ❌ File handles not using context managers (some places)

---

## Exercise 1 — Copilot Coding Agent: Assigning Refactoring Issues
**⏱ 15 minutes**

### What You'll Learn
- Use **GitHub Copilot Coding Agent** by assigning issues in a GitHub repo.

### Steps

1. **Push this code to a new GitHub repo:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: legacy inventory system"
   # Create a repo on GitHub, then:
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Create GitHub Issues for refactoring tasks.** Use Copilot to help:
   ```
   Help me create 5 GitHub issues for refactoring this legacy inventory system.
   Each issue should have:
   - A clear title
   - Description of the problem
   - Acceptance criteria
   - Labels (refactoring, performance, code-quality)
   
   Issues should cover:
   1. Extract data access layer (eliminate repeated load/save)
   2. Add type hints throughout the codebase
   3. Replace manual sorting/CSV with standard library
   4. Separate concerns (models, services, CLI)
   5. Add comprehensive error handling and input validation
   ```

3. **Assign an issue to Copilot Coding Agent:**
   - Go to one of the issues on GitHub
   - Assign it to **Copilot** (the GitHub Copilot Coding Agent)
   - Watch it create a PR with the refactoring changes!

4. **Review the PR:**
   - Does it follow Python best practices?
   - Did it maintain backward compatibility?
   - Are there any issues the Coding Agent missed?

### ✅ Checkpoint
- GitHub repo with issues created.
- At least one issue assigned to Copilot Coding Agent.
- PR created and reviewed.

---

## Exercise 2 — Copilot Agent Mode: Major Refactoring
**⏱ 15 minutes**

### What You'll Learn
- Use Agent Mode for large-scale refactoring and performance tuning.

### Steps

### Part A: Architecture Refactoring

1. **Ask Agent Mode to restructure the project:**
   ```
   Refactor this legacy inventory system into a proper Python project structure:
   
   lab2-inventory-manager-app/
   ├── models/
   │   ├── __init__.py
   │   ├── product.py
   │   ├── order.py
   │   ├── supplier.py
   │   └── category.py
   ├── services/
   │   ├── __init__.py
   │   ├── inventory_service.py
   │   ├── order_service.py
   │   └── report_service.py
   ├── data/
   │   ├── __init__.py
   │   └── repository.py
   ├── cli.py
   ├── app.py (Flask API)
   └── tests/
   
   - Extract models with type hints and dataclasses
   - Create a Repository class that handles all JSON data access
   - Create service classes for business logic
   - Keep the CLI working
   - Add a Flask REST API (app.py) that exposes all functionality
   ```

2. **Verify the refactoring works:**
   ```bash
   python cli.py    # CLI should still work
   python app.py    # API should start
   ```

### Part B: Performance Tuning

3. **Fix the performance issues:**
   ```
   This codebase has severe performance issues:
   1. Data is loaded from disk on EVERY function call
   2. get_sales_report() uses manual selection sort (O(n²)) instead of sorted()
   3. get_inventory_report() recalculates values multiple times 
   4. generate_full_report() calls other report functions redundantly
   5. utils.py has a bubble sort implementation
   
   Refactor for performance:
   - Implement a caching layer in the repository
   - Use Python built-in sorted() and collections.Counter
   - Compute reports in a single pass where possible
   - Add timing to show before/after performance
   ```

4. **Benchmark the improvement:**
   ```
   Create a benchmark script that:
   1. Generates 10,000 sample products and 5,000 orders
   2. Times the old approach vs. new approach for:
      - get_inventory_report()
      - get_sales_report()
      - generate_full_report()
   3. Prints a comparison table
   ```

### ✅ Checkpoint
- Clean project structure with separation of concerns.
- Performance improvements measured and documented.
- Both CLI and API working.

---

## Exercise 3 — Custom Agents for Modular Development
**⏱ 10 minutes**

### What You'll Learn
- Create Custom Agents specialized for different development tasks.
- Use Copilot-assisted architecture and modular design.

### Steps

1. **Create a refactoring-focused agent:**
   ```
   Create a custom agent at .github/agents/refactoring-expert.md that:
   - Specializes in Python code refactoring
   - Always checks for: type hints, proper error handling, DRY principle
   - Runs existing tests before and after changes
   - Uses dataclasses or Pydantic models
   - Follows the repository pattern for data access
   - Creates a summary of changes made
   ```

2. **Create an API development agent:**
   ```
   Create a custom agent at .github/agents/api-builder.md that:
   - Specializes in building Flask REST APIs
   - Always adds input validation
   - Generates OpenAPI/Swagger documentation
   - Creates API tests alongside endpoints
   - Follows RESTful conventions
   ```

3. **Create a custom agent for testing:**
   ```
   Create a custom agent at .github/agents/test-engineer.md that:
   - Specializes in writing comprehensive Python tests
   - Uses pytest with fixtures and parametrize
   - Generates both unit and integration tests
   - Aims for >90% code coverage
   - Includes performance regression tests
   ```

4. **Test the agents** — Try asking Copilot to use your custom agents:
   ```
   @refactoring-expert Review utils.py and refactor the CSV functions to use 
   the standard library csv module properly.
   ```

### ✅ Checkpoint
- Three custom agents created in `.github/agents/`.
- At least one agent tested and working.

---

## Exercise 4 — Orchestration Patterns with Sub Agents & Handoffs
**⏱ 10 minutes**

### What You'll Learn
- See orchestration in action with multi-step tasks.
- Understand how sub agents handle different parts of a complex task.

### Steps

1. **Give Copilot a complex multi-part task:**
   ```
   I need a complete "Supplier Performance" feature:
   
   1. Add a SupplierPerformance model that tracks:
      - Delivery time (avg days)
      - Quality rating (1-5)
      - Return rate (percentage)
      - On-time delivery rate
   
   2. Create a SupplierService with methods to:
      - Calculate performance metrics from order data
      - Rank suppliers by performance
      - Generate supplier comparison reports
   
   3. Add API endpoints:
      - GET /suppliers/:id/performance
      - GET /suppliers/rankings
      - GET /reports/supplier-comparison
   
   4. Write tests for all of the above
   
   5. Update the README with the new endpoints
   
   Implement everything, run the tests, and confirm it works.
   ```

2. **Observe the orchestration** — Notice how Agent Mode:
   - Breaks the request into sub-tasks
   - Completes them in dependency order
   - Hands off context between steps
   - Verifies the result

3. **Discuss orchestration patterns:**
   ```
   Explain the orchestration pattern you used for this feature.
   How did you decide the order of sub-tasks?
   What are the handoff points between sub agents?
   How does this relate to the Sub Agent and Handoff patterns in Copilot?
   ```

### ✅ Checkpoint
- Supplier Performance feature fully implemented.
- Understanding of orchestration, sub agents, and handoffs.

---

## Exercise 5 — Copilot for Refactoring: Legacy Code & Performance Tuning  
**⏱ 10 minutes**

### What You'll Learn
- Use Copilot specifically for improving legacy code quality.

### Steps

1. **Ask Copilot to identify and fix all code smells:**
   ```
   Analyze the original inventory.py and utils.py (you can find the original 
   code in git history). List every code smell, anti-pattern, and performance 
   issue. Then show me a before/after comparison of the most impactful fixes.
   ```

2. **Modernize the Python patterns:**
   ```
   Update the codebase to use modern Python patterns:
   - Replace any remaining old-style string formatting with f-strings
   - Use pathlib instead of os.path
   - Use dataclasses or Pydantic v2 for models
   - Use contextlib for resource management
   - Use typing module for comprehensive type hints
   - Use enum for status/priority constants
   ```

3. **Add logging and observability:**
   ```
   Add structured logging (using Python logging module) throughout the 
   application. Replace all print() statements. Add:
   - Request/response logging for API endpoints
   - Performance timing for slow operations
   - Error logging with context
   - Configurable log levels
   ```

### ✅ Checkpoint
- Modern Python patterns throughout.
- Structured logging added.
- No print() statements remaining.

---

## Exercise 6 — MCP Configuration and Copilot SDK
**⏱ 5 minutes**

### What You'll Learn
- Configure MCP servers for enhanced Copilot capabilities.
- Understand where Copilot SDK fits.

### Steps

1. **Set up project-level MCP configuration:**
   ```
   Create a .vscode/mcp.json configuration file for this project.
   What MCP servers would be useful for:
   - A Python Flask API project
   - Connecting to our JSON data store
   - Accessing external documentation
   
   Show me the configuration and explain each server's purpose.
   ```

2. **Explore Copilot SDK concepts:**
   ```
   If I wanted to build a custom MCP server that exposes our inventory 
   data to Copilot (so it can query products, check stock levels, and 
   generate reports directly), how would I architect that?
   
   Show me:
   - The MCP server structure
   - Tool definitions for inventory operations
   - How Copilot would invoke these tools
   ```

### ✅ Checkpoint
- MCP configuration created.
- Understanding of custom MCP server architecture.

---

## Exercise 7 — Copilot Code Review Agent
**⏱ 5 minutes**

### What You'll Learn
- Use Code Review Agent to audit the refactored code.

### Steps

1. **Do a full code review of the refactored project:**
   ```
   Perform a thorough code review of this entire project. Check for:
   - Security vulnerabilities (input validation, file path traversal, etc.)
   - Performance issues
   - Error handling gaps
   - API design issues (missing status codes, inconsistent responses)
   - Test coverage gaps
   - Documentation completeness
   - Python best practices violations
   
   Rate each issue as Critical, High, Medium, or Low severity.
   ```

2. **Fix all Critical and High issues** identified in the review.

3. **If you've pushed to GitHub, enable Copilot Code Review on your PR:**
   - Go to your PR settings
   - Enable Copilot as a reviewer
   - Observe the automated review comments

### ✅ Checkpoint
- Code review completed.
- Critical/High issues resolved.

---

## 🏁 Lab 2 Complete!

By now you've used:
- ✅ Copilot Coding Agent (assigning issues on GitHub)
- ✅ Agent Mode for large-scale refactoring
- ✅ Custom Agents for modular development
- ✅ Orchestration Patterns (Sub Agents & Handoffs)
- ✅ Copilot for legacy code refactoring & performance tuning
- ✅ MCP configuration and Copilot SDK concepts
- ✅ Code Review Agent

**Bonus Challenge:** Create a GitHub Actions workflow that runs your tests and uses Copilot Code Review on every PR!
