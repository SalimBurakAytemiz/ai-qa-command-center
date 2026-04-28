import { test } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { getDefaultTestUser } from '../fixtures/test-users';
import { hasLoginEnv } from '../helpers/env';

test.describe('Login smoke tests', () => {
  test('registered user can log in with valid credentials', async ({ page }) => {
    test.skip(!hasLoginEnv(), 'WEB_BASE_URL, TEST_USER_EMAIL, and TEST_USER_PASSWORD are required for this test.');

    const loginPage = new LoginPage(page);
    const user = getDefaultTestUser();

    await loginPage.goto();
    await loginPage.expectLoaded();
    await loginPage.login(user.email, user.password);
    await loginPage.expectDashboardVisible();
  });
});
