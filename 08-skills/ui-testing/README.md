# Skill: UI Testing

## Purpose

This skill defines how AI QA agents should analyze user interface behavior and visible product quality.

It should be used by:

- Web Functional Test Agent
- Product Flow Test Agent
- Web Design and Pixel Perfect Agent
- Mobile Responsive Design Agent
- Accessibility Test Agent
- Output Reviewer Agent

## UI Testing Goals

UI testing must validate:

1. Page access
2. Navigation
3. Forms
4. Buttons
5. Links
6. Data display
7. Empty states
8. Loading states
9. Error states
10. Success states
11. Role-based visibility
12. Responsive behavior
13. Visual consistency
14. Accessibility basics
15. Cross-browser or cross-device risks

## Functional UI Areas

Validate:

- Login form
- Register form
- Password reset form
- Profile form
- Search
- Filters
- Sorting
- Pagination
- Tables
- Cards
- Lists
- Detail pages
- Modals
- Drawers
- Toast messages
- Tabs
- Dropdowns
- Checkboxes
- Radio buttons
- File upload
- Admin CRUD actions
- CMS content visibility

## UI State Checks

Validate:

- Default state
- Loading state
- Empty state
- Error state
- Success state
- Disabled state
- Focus state
- Selected state
- Hover state when relevant
- Validation state

## Form Validation Checks

Validate:

- Required fields
- Optional fields
- Invalid format
- Min length
- Max length
- Special characters
- Numeric boundaries
- Date boundaries
- File type
- File size
- Clear error messages
- Submit button behavior
- Duplicate submission prevention

## Role-Based UI Checks

Validate:

- Correct elements visible for each role
- Restricted elements hidden
- Restricted actions blocked
- Admin-only buttons not visible to normal users
- Content manager actions limited correctly
- Super admin actions not exposed to lower roles

## Responsive Checks

Validate:

- Desktop layout
- Tablet layout
- Mobile layout
- Header and menu behavior
- Overflow
- Clipping
- Horizontal scroll
- Text wrapping
- Button alignment
- Form usability
- Touch target size
- Sticky elements
- Modal behavior

## Visual Quality Checks

Validate:

- Spacing
- Alignment
- Typography
- Color consistency
- Icon consistency
- Component consistency
- Image scaling
- Broken images
- Design-system usage

## Accessibility Basics

Check:

- Label exists for form fields
- Keyboard focus is visible
- Focus order is logical
- Contrast appears acceptable
- Buttons and links are understandable
- Error messages are readable
- Important actions are not color-only
- Screen-reader labels exist when known

## Common Mistakes to Avoid

- Testing only the happy screen
- Ignoring empty states
- Ignoring loading states
- Ignoring error states
- Ignoring role-based visibility
- Ignoring responsive layout
- Writing vague expected results
- Mixing API-only validation into UI output
- Ignoring accessibility basics
- Marking visual judgment as confirmed without evidence

## Expected Result Rules

Bad:

"The page looks good."

Good:

"The page displays the user profile form with name, email, phone fields, and the Save button remains disabled until required fields are valid."

## Review Checklist

Before approving UI validation output, check:

- Are pages or screens listed?
- Are user roles included?
- Are UI states covered?
- Are form validations covered?
- Are responsive risks listed?
- Are expected results observable?
- Are backend dependencies mentioned only when relevant?
- Are automation candidates realistic?