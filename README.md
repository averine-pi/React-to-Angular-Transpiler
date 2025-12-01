# React-to-Angular-Transpiler
A lightweight Python-based tool that converts simple React JSX components into Angular components.
This transpiler focuses on beginner-friendly JSX structures and uses Python’s re module to map React syntax into Angular equivalents. 

I followed a step-by-step transformation pipeline, applying multiple regex substitutions using methods instead of one large parser. I identified the various parts of the code in both frameworks and works to produce an accurate mapping from one syntax to the other.

1. Event Replacement
Identify onClick={...}
Replace with Angular's (click) syntax
Add parentheses properly around function calls

2. Variable Interpolation
Convert {variable} to {{ variable }}

3. Map → NgFor Transformation
Capture array name, element variable, and index
Replace .map() with *ngFor
Remove extra JSX parentheses

4. Cleanup Stage
Remove leftover React-specific brackets
Tidy up closing tags introduced by regex

This approach ensures the output is readable and mostly Angular-valid. 

# Limitations
This tool intentionally focuses on introductory JSX patterns.
It might not correctly handle:
-> nested components
-> hooks like useState
-> complex logic
-> conditional rendering

These require an AST parser (e.g., Babel), which can be added on further to expand the scope of this project.

# Future Improvements
If given more time, the next steps would be:
-> Replace regex with a real AST approach
-> Migrating from regex to a true AST parser (Babel + Python bridge)
-> Add support for ternary conditions → *ngIf
-> Convert React hooks to Angular component class syntax

