# 🧪 Lab 1: Task Tracker API — GitHub Copilot Deep Dive

## Overview
You have a **partially built Task Tracker API** (Flask). Your mission is to use GitHub Copilot's full toolkit — Plan Mode, Agent Mode, Testing, Documentation, Customization, Code Review, and MCP — to enhance, test, document, and ship this app.

**Estimated Time:** 60–75 minutes

---

## Prerequisites
- VS Code with GitHub Copilot extension (Chat + Agent)
- Python 3.10+
- This folder open in VS Code

### Setup
```bash
cd lab1-task-tracker-app
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py               # Verify it runs on http://localhost:5000
```

---

## Exercise 1 — Copilot Plan Mode: Writing User Stories & Acceptance Criteria
**⏱ 10 minutes**

### What You'll Learn
- Use Copilot **Plan Mode** in IDE/CLI to plan features before writing code.

### Steps

1. **Open Copilot Chat** (⌘⇧I / Ctrl+Shift+I) and switch to **Plan Mode** (click the plan icon or type `/plan`).

2. **Ask Copilot to plan a new feature:**
   ```
   I want to add a "task statistics dashboard" endpoint to this Flask API.
   It should return:
   - Total number of tasks
   - Breakdown by status (todo, in-progress, done)
   - Breakdown by priority (low, medium, high, critical)
   - Average number of comments per task
   - Most recently created and updated tasks
   
   Plan the implementation with user stories and acceptance criteria.
   ```

3. **Review the plan** — Copilot will generate user stories with acceptance criteria. Examine them critically:
   - Are the acceptance criteria testable?
   - Are edge cases considered (empty database, etc.)?

4. **Refine the plan:**
   ```
   Add acceptance criteria for error handling and for when the database is empty.
   Also add a user story for filtering statistics by date range.
   ```

5. **Save the plan** — Copy the output into a `PLAN.md` file in this folder.

### ✅ Checkpoint
- You have a `PLAN.md` with user stories and acceptance criteria for the statistics feature.

---

## Exercise 2 — Copilot Agent Mode: Implementing Features
**⏱ 15 minutes**

### What You'll Learn
- Use Copilot **Agent Mode** to scaffold, generate boilerplate, and implement logic.

### Steps

1. **Switch to Agent Mode** in Copilot Chat (click the agent icon or select Agent from the mode dropdown).

2. **Implement the statistics endpoint:**
   ```
   Implement the task statistics dashboard endpoint based on the plan in PLAN.md.
   Add a new function in database.py and a new route in app.py at GET /tasks/stats.
   Follow the existing code patterns in this project.
   ```

3. **Watch Copilot Agent work** — It will:
   - Read your existing files
   - Create/edit `database.py` to add statistics functions
   - Create/edit `app.py` to add the new route
   - Run the app to verify

4. **Implement bulk operations:**
   ```
   Implement a POST /tasks/bulk endpoint that accepts a list of task IDs and an 
   action (delete, update_status, add_tag). Use Agent mode to implement this 
   end-to-end including the database functions.
   ```

5. **Fix the bug** — Notice the `# BUG` comment in `app.py` on the `/tasks/<task_id>/transition` endpoint:
   ```
   Fix the task transition endpoint. Add status validation so tasks can only 
   transition: todo → in-progress → done. Reject invalid transitions with 
   a 400 error and a helpful message.
   ```

6. **Test your new endpoints manually:**
   ```bash
   # Create a task
   curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" \
     -d '{"title": "Test task", "description": "Testing", "priority": "high"}'
   
   # Get statistics
   curl http://localhost:5000/tasks/stats
   ```

### ✅ Checkpoint
- `/tasks/stats` returns statistics.
- `/tasks/bulk` handles bulk operations.
- `/tasks/<id>/transition` validates status transitions.

---

## Exercise 3 — Copilot for Testing: Generating Mocks & Edge Cases
**⏱ 10 minutes**

### What You'll Learn
- Use Copilot to generate comprehensive tests including mocks, fixtures, and edge cases.

### Steps

1. **Ask Copilot to generate tests:**
   ```
   Generate a comprehensive test suite for this Flask Task Tracker API.
   Create a tests/ folder with:
   - test_app.py: API endpoint tests using Flask test client
   - test_database.py: Unit tests for all database functions
   - test_models.py: Unit tests for Task and User models
   
   Include:
   - Fixtures for sample tasks and users
   - Edge cases (empty database, invalid inputs, duplicate operations)
   - Mocks where appropriate
   - Test the status transition validation
   ```

2. **Run the tests:**
   ```bash
   pytest tests/ -v
   ```

3. **Ask Copilot to add more edge cases:**
   ```
   Add edge case tests for:
   - Creating a task with an extremely long title (10000 chars)
   - Searching with special characters
   - Concurrent comment additions
   - Bulk operations with invalid task IDs mixed with valid ones
   ```

4. **Generate a coverage report:**
   ```bash
   pytest tests/ -v --cov=. --cov-report=term-missing
   ```

5. **Ask Copilot to fill coverage gaps:**
   ```
   Based on the coverage report, add tests to cover the uncovered lines.
   ```

### ✅ Checkpoint
- `tests/` folder with passing tests.
- Coverage report showing >80% coverage.

---

## Exercise 4 — Copilot for Documentation: README, Docstrings, Changelogs
**⏱ 10 minutes**

### What You'll Learn
- Use Copilot to generate professional documentation.

### Steps

1. **Generate a README:**
   ```
   Generate a comprehensive README.md for this Task Tracker API project.
   Include:
   - Project overview and architecture
   - Setup instructions
   - API endpoint documentation with examples (curl commands)
   - Environment variables
   - Testing instructions
   - Contributing guidelines
   ```

2. **Add docstrings to all functions:**
   ```
   Add Google-style docstrings to all functions in app.py, database.py, 
   and models.py. Include parameter descriptions, return types, and 
   usage examples.
   ```

3. **Generate a CHANGELOG:**
   ```
   Generate a CHANGELOG.md following the Keep a Changelog format. 
   Document the features we've added: statistics endpoint, bulk operations, 
   status transition validation, and test suite.
   ```

### ✅ Checkpoint
- `README.md` with full API docs.
- All functions have docstrings.
- `CHANGELOG.md` exists.

---

## Exercise 5 — Copilot Customization: Instructions, Prompts, and Custom Agents
**⏱ 15 minutes**

### What You'll Learn
- Create `copilot-instructions.md` to guide Copilot's behavior.
- Create reusable prompt files.
- Understand Custom Agents and Agent Skills.

### Steps

### Part A: copilot-instructions.md

1. **Create `.github/copilot-instructions.md`** — Ask Copilot:
   ```
   Create a .github/copilot-instructions.md file for this project that tells 
   Copilot to:
   - Always use Flask patterns consistent with this codebase
   - Use Google-style docstrings
   - Always include input validation on API endpoints
   - Use the existing database.py pattern for data access
   - Write pytest-style tests with fixtures
   - Follow REST API naming conventions
   ```

2. **Test it** — Ask Copilot to add a new endpoint (e.g., `GET /tasks/<id>/history`) and verify it follows your instructions.

### Part B: Reusable Prompts

3. **Create a `.github/prompts/` directory** with reusable prompt files:
   ```
   Create a .github/prompts/add-endpoint.prompt.md file that contains a 
   reusable prompt template for adding new REST API endpoints to this project.
   It should include steps for: database function, route handler, input 
   validation, error handling, and tests.
   ```

4. **Create another prompt file:**
   ```
   Create a .github/prompts/review-security.prompt.md that checks API 
   endpoints for common security issues: input validation, SQL injection 
   (even though we use in-memory DB), rate limiting considerations, 
   CORS configuration, and error message information leakage.
   ```

### Part C: Custom Agents (Agents.md)

5. **Create `.github/agents/api-developer.md`:**
   ```
   Create a custom agent definition at .github/agents/api-developer.md 
   that specializes in building REST API endpoints for this Flask project.
   The agent should:
   - Always read copilot-instructions.md first
   - Follow the add-endpoint prompt pattern
   - Run tests after making changes
   - Update the README with new endpoint documentation
   ```

### Part D: Agent Skills

6. **Understand Agent Skills** — Discuss with Copilot:
   ```
   Explain how Agent Skills work in GitHub Copilot. How would I create a 
   skill for "Flask API development" that includes domain knowledge about 
   REST patterns, Flask best practices, and our project conventions?
   ```

### ✅ Checkpoint
- `.github/copilot-instructions.md` exists and influences Copilot behavior.
- `.github/prompts/` has reusable prompt files.
- `.github/agents/api-developer.md` custom agent exists.
- You understand Agent Skills conceptually.

---

## Exercise 6 — Orchestration Patterns: Sub Agents & Handoffs
**⏱ 5 minutes**

### What You'll Learn
- Understand how Copilot uses sub agents and handoffs internally.

### Steps

1. **Observe orchestration in action:**
   ```
   Add a new feature: task dependencies. A task can depend on other tasks 
   and cannot move to "done" until all dependencies are also "done".
   Implement the model changes, database functions, API endpoints, 
   tests, and update the README.
   ```
   Watch how Agent Mode orchestrates multiple steps — this is the orchestration pattern in action.

2. **Discuss the pattern:**
   ```
   Explain the orchestration pattern you just used. How did you break 
   this task into sub-tasks? How do sub agents and handoffs work in 
   GitHub Copilot's architecture?
   ```

### ✅ Checkpoint
- Task dependency feature implemented.
- Understanding of how orchestration works under the hood.

---

## Exercise 7 — MCP Overview (Model-Context-Prompt)
**⏱ 5 minutes**

### What You'll Learn
- Understand MCP architecture and where to use Copilot SDK.

### Steps

1. **Discuss MCP with Copilot:**
   ```
   Explain the MCP (Model-Context-Prompt) architecture in GitHub Copilot.
   How does it relate to:
   - The model (LLM) selection
   - The context (files, instructions, conversation)
   - The prompt (user input, system prompts, customization)
   
   How would I use the Copilot SDK to build a custom Copilot-powered 
   tool for this task tracker?
   ```

2. **Explore MCP configuration:**
   ```
   Show me how to configure MCP servers in VS Code settings for this project.
   What MCP servers would be useful for a Python Flask API project?
   ```

### ✅ Checkpoint
- Understanding of MCP architecture.
- Awareness of Copilot SDK capabilities.

---

## Exercise 8 — GitHub Copilot Code Review Agent
**⏱ 5 minutes**

### What You'll Learn
- Use Copilot Code Review to find and fix issues.

### Steps

1. **Request a code review:**
   ```
   Review all the code in this project for:
   - Security vulnerabilities
   - Performance issues
   - Code quality problems
   - Missing error handling
   - REST API best practices violations
   ```

2. **Fix the issues** — Let Agent Mode fix the issues identified by the review.

3. **Review the changes** — Use Copilot to review its own fixes:
   ```
   Review the changes you just made. Are there any remaining issues?
   ```

### ✅ Checkpoint
- Code review completed.
- Issues fixed and verified.

---

## 🏁 Lab 1 Complete!

By now you've used:
- ✅ Plan Mode for user stories and acceptance criteria
- ✅ Agent Mode for implementation
- ✅ Copilot for test generation
- ✅ Copilot for documentation
- ✅ copilot-instructions.md, prompts, custom agents, and skills
- ✅ Orchestration patterns (sub agents & handoffs)
- ✅ MCP overview
- ✅ Code Review Agent

**Bonus Challenge:** Try using the Copilot CLI (`gh copilot`) to interact with the API from the terminal!
