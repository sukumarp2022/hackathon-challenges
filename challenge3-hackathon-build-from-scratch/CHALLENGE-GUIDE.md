# 🏆 Challenge 3: Build a Smart Meeting Scheduler — Hackathon Challenge

## The Challenge
Build a **Smart Meeting Scheduler** from scratch using **only GitHub Copilot** as your pair programmer. No starter code. No templates. Just you, Copilot, and the techniques from Labs 1 & 2.

**Estimated Time:** 60–90 minutes  
**Team Size:** 1–3 people

---

## What You're Building

A Python application that helps teams schedule meetings intelligently:
- Manages participants and their availability
- Finds optimal meeting times across multiple participants
- Handles time zones
- Tracks meeting rooms and resources
- Sends meeting summaries
- Provides a REST API and a simple CLI

---

## Requirements

### Core Features
1. **Participant Management** — Add/edit/remove participants with their weekly availability (e.g., "Monday 9am-5pm", "Tuesday 10am-3pm")
2. **Meeting Scheduling** — Find the first available slot where all required participants are free
3. **Room Booking** — Manage meeting rooms with capacity limits and equipment (projector, whiteboard, video conferencing)
4. **Conflict Detection** — Detect and report scheduling conflicts
5. **Meeting CRUD** — Create, read, update, cancel meetings

### Stretch Goals
6. **Time Zone Support** — Participants in different time zones
7. **Recurring Meetings** — Weekly/bi-weekly/monthly recurrence
8. **Priority Scheduling** — VIP participants get priority; suggest bumping lower-priority meetings
9. **Analytics Dashboard** — Meeting frequency, most-booked rooms, busiest participants
10. **Calendar Export** — Export to .ics format

---

## How to Build It — Step by Step Using Copilot

### Phase 1: Plan with Copilot Plan Mode (10 min)

Start in **Plan Mode** and use these prompts:

```
I'm building a Smart Meeting Scheduler in Python. Plan the full project:

1. Generate user stories with acceptance criteria for:
   - Participant management
   - Meeting scheduling algorithm
   - Room booking
   - Conflict detection

2. Design the data models (Participant, Meeting, Room, TimeSlot)

3. Propose the project structure with separation of concerns

4. Identify edge cases and error scenarios
```

Save the plan to `PLAN.md`.

---

### Phase 2: Set Up Customization First (5 min)

Before writing any code, set up your Copilot customization:

```
Create the following customization files for a new Python project 
called "Smart Meeting Scheduler":

1. .github/copilot-instructions.md — Project-specific rules:
   - Use Python 3.11+ features
   - Use Pydantic v2 for models
   - Use Flask for the API
   - Use pytest for testing
   - Google-style docstrings
   - Type hints everywhere

2. .github/prompts/new-feature.prompt.md — Template for adding features

3. .github/agents/scheduler-dev.md — Custom agent for this project
```

---

### Phase 3: Build with Agent Mode (30 min)

Now use **Agent Mode** for the heavy lifting. Use these prompts in sequence:

**Prompt 1: Project scaffolding**
```
Create the project structure for the Smart Meeting Scheduler based on PLAN.md.
Set up:
- models/ with Pydantic models for Participant, Meeting, Room, TimeSlot
- services/ with SchedulerService, RoomService, ParticipantService
- api/ with Flask routes
- cli.py for command-line interface
- requirements.txt
- A basic README.md
```

**Prompt 2: Scheduling algorithm**
```
Implement the core scheduling algorithm in services/scheduler_service.py:
- Given a list of participant IDs, a duration, and a date range
- Find all available time slots where ALL participants are free
- Rank slots by preference (morning preferred over afternoon)
- Handle the case where no slot exists — suggest the time with fewest conflicts
```

**Prompt 3: REST API**
```
Build the complete Flask REST API:
- POST /participants — Create participant with availability
- GET /participants/:id/availability — Get free slots for a date range
- POST /meetings/find-slot — Find optimal meeting time
- POST /meetings — Book a meeting
- GET /meetings/:id — Get meeting details
- DELETE /meetings/:id — Cancel a meeting
- POST /rooms — Add a room
- GET /rooms/available — Find available rooms for a time slot
- GET /analytics/dashboard — Meeting statistics
```

**Prompt 4: Tests**
```
Create comprehensive tests:
- Unit tests for the scheduling algorithm (including edge cases)
- API integration tests
- Test fixtures with sample data
- Test scenarios: overlapping meetings, all-day availability, 
  no availability, single participant, 20 participants
```

---

### Phase 4: Enhance with Advanced Features (15 min)

**Prompt 5: Orchestration challenge**
```
Add time zone support to the entire application:
1. Update Participant model with timezone field
2. Modify the scheduling algorithm to normalize times to UTC
3. Update API responses to return times in each participant's local timezone
4. Add timezone conversion utilities
5. Update all tests
6. Update the README

Do this as a single coordinated change across all files.
```

**Prompt 6: Custom Agent in action**
```
@scheduler-dev Add recurring meeting support:
- Weekly, bi-weekly, monthly recurrence patterns
- Ability to skip specific dates (holidays)
- Cancel a single occurrence vs. entire series
- Conflict detection across the recurrence series
```

---

### Phase 5: Quality & Documentation (10 min)

**Prompt 7: Code Review**
```
Perform a complete code review of this Smart Meeting Scheduler.
Check for security issues, performance problems, edge cases, and 
Python best practices. Fix all issues found.
```

**Prompt 8: Documentation**
```
Generate:
1. A comprehensive README.md with:
   - Architecture diagram (Mermaid)
   - API documentation with curl examples
   - Setup instructions
   - Testing guide
2. Docstrings on all public functions
3. A CHANGELOG.md
```

**Prompt 9: MCP exploration**
```
Design an MCP server configuration that would let Copilot directly 
interact with the meeting scheduler — checking availability, booking 
meetings, and querying analytics — right from the chat interface.
Create a .vscode/mcp.json configuration.
```

---

### Phase 6: Ship It (5 min)

**Prompt 10: GitHub Coding Agent**
```
Help me:
1. Initialize a git repo
2. Create a proper .gitignore
3. Write GitHub Issues for remaining stretch goals
4. Create a GitHub Actions workflow for CI (tests + linting)
5. Push to GitHub
```

Then assign one of the stretch goal issues to **Copilot Coding Agent** and watch it work!

---

## Judging Criteria

| Criteria | Points | Description |
|----------|--------|-------------|
| **Core Features** | 30 | All 5 core features working |
| **Code Quality** | 20 | Clean architecture, type hints, proper patterns |
| **Test Coverage** | 15 | >80% coverage with meaningful tests |
| **Copilot Customization** | 15 | instructions.md, prompts, custom agents, skills |
| **Documentation** | 10 | README, docstrings, API docs |
| **Stretch Goals** | 10 | Each stretch goal = 2 bonus points |

**Maximum Score: 100 + 10 bonus**

---

## Topics Covered in This Challenge

| Workshop Topic | Where It's Used |
|----------------|-----------------|
| Plan Mode | Phase 1 — Planning user stories |
| Agent Mode | Phase 3 — Building everything |
| Copilot for Testing | Phase 3, Prompt 4 |
| Copilot for Documentation | Phase 5, Prompt 8 |
| Orchestration (Sub Agents & Handoffs) | Phase 4, Prompt 5 |
| Copilot Customization (instructions.md) | Phase 2 |
| Reusable Prompts | Phase 2 |
| Custom Agents | Phase 2 & 4, Prompt 6 |
| Agent Skills | Phase 2 (agent definitions) |
| MCP Overview | Phase 5, Prompt 9 |
| Copilot Coding Agent | Phase 6, Prompt 10 |
| Copilot for Refactoring | Phase 5, Prompt 7 |
| Code Review Agent | Phase 5, Prompt 7 |

---

## Tips for Success

1. **Don't type code manually** — Let Copilot generate everything. Your job is to direct and refine.
2. **Use Plan Mode first** — A good plan saves time during implementation.
3. **Set up customization early** — copilot-instructions.md makes every subsequent prompt better.
4. **Review Copilot's output** — Don't blindly accept. Read, understand, and refine.
5. **Use Agent Mode for multi-file changes** — It's faster than editing file by file.
6. **Run tests frequently** — After every major change.
7. **Commit often** — Small, focused commits. Use Copilot to write commit messages.

---

## Getting Help

- Stuck on a prompt? Ask Copilot: `"I'm trying to do X but it's not working. What's a better approach?"`
- Copilot generated bad code? Ask: `"Review this code and fix the issues"`
- Not sure what to do next? Ask: `"What should I build next based on PLAN.md?"`

---

**Good luck! 🚀 Build fast, build smart, and let Copilot do the heavy lifting.**
