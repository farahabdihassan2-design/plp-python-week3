# Week 3 Assignment: Conditions and Loops

## File Descriptions
- `grade_reporter.py`: Prompts for test scores, computes average grades using loops, and assigns letter grades with conditional statements.
- `bug_hunt.py`: Fixes three errors (syntax, type, and logical) using explicit `# BUG:` comments to correctly output the sum of 1 to 5 as 15.
- `README.md`: Contains the project overview, file descriptions, and reflection on debugging Part B.

## Reflection
The hardest bug to find in Part B was the logical error in the loop condition (`while count < 5`). Since Python ran the program without throwing a syntax or runtime error message, the bug was completely hidden. I realized something was wrong when the output printed `10` instead of the required `15`, which signaled that the loop ended before adding the final number.