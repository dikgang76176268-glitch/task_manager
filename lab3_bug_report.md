
# Lab 3: My Analysis vs AI Analysis

## Prompt Sent to AI
> Review these 5 defects in a GradeManager class:
> 1. add_student() returns None
> 2. get_average() crashes on empty list (ZeroDivisionError)
> 3. get_passing_students() includes wrong students
> 4. get_all_students() omits first student
> 5. format_report() crashes joining integers
> 
> Suggest fixes and note any additional improvements.

---

## Comparison Table
| Defect | My Suggestion | AI Suggestion | Match? |
|---|---|---|---|
| 1 — Return None | Return confirmation string | Add return statement with message | ✅ Match |
| 2 — Divide by zero | Check empty → return 0 | Guard clause → return 0.0 | ✅ Match |
| 3 — Logic inverted | Flip comparison | Fix threshold or operator direction | ✅ Match |
| 4 — First student missing | Fix loop start index | Remove index skip | ✅ Match |
| 5 — Type error | map(str, grades) | Convert each grade to string | ✅ Match |

---

## Additional Observations
- AI also suggested adding **input validation** (e.g., scores must be 0–100) — this is a good extra improvement
- AI recommended clearer **error messages** and **custom exception types**
- Both identified the same root causes — AI added defensive programming suggestions
- No defects were missed by either approach