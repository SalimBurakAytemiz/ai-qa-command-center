import { expect, type Page } from '@playwright/test';

export class LoginPage {
  constructor(private readonly page: Page) {}

  async goto(): Promise<void> {
    await this.page.goto('/login');
  }

  async expectLoaded(): Promise<void> {
    await expect(this.page.getByLabel(/email/i)).toBeVisible();
    await expect(this.page.getByLabel(/password/i)).toBeVisible();
    await expect(this.page.getByRole('button', { name: /login/i })).toBeVisible();
  }

  async login(email: string, password: string): Promise<void> {
    await this.page.getByLabel(/email/i).fill(email);
    await this.page.getByLabel(/password/i).fill(password);
    await this.page.getByRole('button', { name: /login/i }).click();
  }

  async expectDashboardVisible(): Promise<void> {
    await expect(this.page.getByRole('heading', { name: /dashboard/i })).toBeVisible();
  }
}
