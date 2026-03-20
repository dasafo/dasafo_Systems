# 01. Coding Standards & Vibe
> **Objective:** Maximize development velocity (Vibe) without sacrificing structural integrity (Solidity).

## 1. Naming & Self-Documentation
- Use explicit and descriptive names. The use of generic verbs like `getData()` is strictly prohibited.
  - ✅ **Good:** `getSensorReadingById()`, `calculateIsolationForestScore()`
  - ❌ **Bad:** `process()`, `handleData()`
- Avoid unnecessary comments. Code must explain itself.
- **Exceptions for comments:** Non-obvious business rules, temporary technical compromises, or explicit trade-offs.

## 2. Immutability by Default
- Treat all data as immutable unless mutation is strictly necessary.
- Prefer pure functions and explicit state transitions.
- Avoid shared mutable state to prevent hidden side effects during multi-agent collaboration.

## 3. Early Return Pattern
- Avoid deep code nesting.
- It is mandatory to handle error cases or trivial conditions at the beginning of the function.

```javascript
// ✅ Good: Flat and predictable logic
if (!condition) return;
if (!anotherCondition) return;
// happy path
```

## 4. UI Vibe & Atomic Design System
- **Tokenization:** NEVER hardcode generic colors, spacing, or borders. Always use semantic tokens (e.g., `Colors.danger`, `var(--color-brand-bg)`).
- **Aesthetic Vibe:** The user must be amazed at first glance. Use curated palettes, elegant dark mode (Glassmorphism), fluid transitions, and dynamic micro-animations.
- **Visual Resilience:** Every UI component must anticipate, design, and test for the following states: *Loading*, *Error*, *Empty State*, and *Data Overflow*.
