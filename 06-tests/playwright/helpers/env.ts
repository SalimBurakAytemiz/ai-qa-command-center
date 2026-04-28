export function requiredEnv(name: string): string {
  const value = process.env[name];

  if (!value) {
    throw new Error(`Missing required environment variable: ${name}`);
  }

  return value;
}

export function hasLoginEnv(): boolean {
  return Boolean(
    process.env.WEB_BASE_URL &&
    process.env.TEST_USER_EMAIL &&
    process.env.TEST_USER_PASSWORD
  );
}
