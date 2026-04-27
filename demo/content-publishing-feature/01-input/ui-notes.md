# Content Publishing UI Notes

## 1. Feature Name

Content Publishing

---

## 2. Screens

| Screen | Platform | Notes |
|---|---|---|
| CMS Content List | Admin Panel / CMS | Shows content items and status |
| Content Editor | Admin Panel / CMS | Create and edit content |
| Preview Screen | Admin Panel / CMS | Preview draft before publishing |
| Public Content Detail | Web | Shows published content |
| Public Content List | Web | Lists published content |

---

## 3. CMS Elements

Expected elements:

- Title input
- Slug input
- Summary input
- Body editor
- Category selector
- Save Draft button
- Preview button
- Publish button
- Unpublish button
- Archive button
- Status badge
- Validation message area
- Loading state
- Success state
- Error state

---

## 4. Form Validation

| Field | Rule | Expected Behavior |
|---|---|---|
| Title | Required | Show validation or prevent save |
| Slug | Required and unique | Show validation or API error |
| Body | Required | Show validation or prevent save |
| Category | Optional or required based on product rule | Needs confirmation |

---

## 5. Success States

After save draft:

- Content is saved.
- Status badge shows Draft.
- Content is not public.

After publish:

- Status badge shows Published.
- Published content is visible on public route.
- Publish success message is shown.

After archive:

- Status badge shows Archived.
- Content is not visible publicly.

---

## 6. Error States

For invalid content:

- User remains on editor page.
- Validation message is displayed.
- Invalid content is not published.

For unauthorized CMS access:

- Access denied message or redirect should occur.
- CMS content should not be visible.

---

## 7. Loading States

While saving or publishing:

- Primary action button should show loading state.
- Duplicate submit should be prevented.
- User should not see false success before API confirms state change.

---

## 8. Responsive Behavior

Admin panel may be desktop-first, but should not break on tablet or smaller viewports if supported.

Public content pages should support responsive display.

---

## 9. Accessibility Notes

Consider:

- Inputs have labels.
- Error messages are readable.
- Publish and archive actions are clearly distinguishable.
- Keyboard navigation works for form fields.
- Status badge text is not color-only.

---

## 10. Missing UI Information

| Missing Item | Why Needed | Impact |
|---|---|---|
| Exact CMS routes | Needed for navigation tests | Redirect/access tests generic |
| Exact validation messages | Needed for UI assertions | Message checks vague |
| Exact status labels | Needed for UI state validation | Status expectations uncertain |
| Archive confirmation design | Needed for destructive-ish action validation | UX risk unclear |
| Role-specific button visibility | Needed for permission UI checks | Authorization UI behavior unclear |
