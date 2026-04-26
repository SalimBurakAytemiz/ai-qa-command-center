# Playwright Testing Patterns

## Purpose

This document defines practical Playwright testing patterns for AI QA agents.

Use this reference when generating Playwright test plans, automation candidates, locator strategies, or example automation code.

---

## 1. Prefer User-Facing Locators

### Bad

```typescript
await page.locator("div:nth-child(3) > button").click();