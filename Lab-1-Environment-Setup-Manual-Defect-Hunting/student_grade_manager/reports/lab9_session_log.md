\# Lab 9: Exploratory Testing — Session Log

Date: 2026-10-27

Tester: dikgang76176268-glitch



\---



\## Charter 1: Boundary \& Edge Values

| Input / Action | Expected Result | Actual Result | Status |

|---|---|---|---|

| Grade = -1 | Rejected / Error | Accepted: \[-1] — NO VALIDATION! | ⚠️ ISSUE FOUND |

| Grade = 0 | Accepted (F) | Accepted: \[0] | ✅ Pass |

| Grade = 49 | Accepted (F) | Accepted: \[49] | ✅ Pass |

| Grade = 50 | Accepted (P) | Accepted: \[50] | ✅ Pass |

| Grade = 100 | Accepted (D) | Accepted: \[100] | ✅ Pass |

| Grade = 101 | Rejected / Error | Accepted: \[101] — NO VALIDATION! | ⚠️ ISSUE FOUND |

| Empty grades list | Avg = 0.0 | Returns 0.0 | ✅ Pass |

| Single grade | Correct avg | Works correctly | ✅ Pass |



\---



\## Charter 2: Data Integrity

| Action | Expected Result | Actual Result | Status |

|---|---|---|---|

| Add student → appears in list | Name present | Name appears in list | ✅ Pass |

| Add grade → count increases | Grades += 1 | Count increases correctly | ✅ Pass |

| Remove existing student → gone | Not in list | To be tested | ⬜ |

| Remove non-existent → False | Returns False | To be tested | ⬜ |

| Duplicate name added | Warned / Rejected | Accepted silently | ⚠️ OBSERVED |



\---



\## Charter 3: Clarity \& Edge Inputs

| Input / Action | Expected Result | Actual Result | Status |

|---|---|---|---|

| Empty name "" | Handled / rejected | To be tested | ⬜ |

| Whitespace name "   " | Handled / rejected | To be tested | ⬜ |

| Report non-existent → clear msg | "not found" message | Shows: "Student 'X' not found" | ✅ Pass |



\---



\## Charter 4: CLI Workflow

| Observation | Details |

|---|---|

| \*\*Bug Found ✅ FIXED\*\* | cli.py accessed index 5 → IndexError |

| Location | cli.py line 29 |

| Root Cause | Only 3 students exist (indices 0,1,2), code tried \[5] |

| Fix Applied | Added `if len(manager.students) > 5:` check before access |

| After Fix | Shows: "Index 5 is out of range. Only 3 students available." |

| Status | ✅ FIXED — no more crash! |



\---



\## Issues Found During Exploration



\### Issue 1 — Grade Values Not Validated

\- \*\*Charter:\*\* #1

\- \*\*Observed:\*\* Grades -1 and 101 accepted with no error

\- \*\*Expected:\*\* Grades must be 0–100; invalid values rejected

\- \*\*Severity:\*\* Medium

\- \*\*Impact:\*\* Invalid data corrupts calculations

\- \*\*Fix Idea:\*\* Add check in `add\_student()` or `add\_grade()` — reject if grade < 0 or > 100



\### Issue 2 — Duplicate Student Names Allowed

\- \*\*Charter:\*\* #2

\- \*\*Observed:\*\* Added "Max" twice — both accepted

\- \*\*Expected:\*\* System should warn or prevent duplicate names

\- \*\*Severity:\*\* Low

\- \*\*Impact:\*\* Ambiguity when fetching by name



\### Issue 3 — Index Out of Range in Demo

\- \*\*Charter:\*\* #4

\- \*\*Status:\*\* ✅ FIXED

\- \*\*Original:\*\* Hardcoded index 5 beyond list length

\- \*\*Fix:\*\* Added length check before accessing index

