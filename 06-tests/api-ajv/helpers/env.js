export function getRequiredEnv(name) {
  const value = process.env[name];

  if (!value) {
    throw new Error(`Missing required environment variable: ${name}`);
  }

  return value;
}

export function hasLoginCodeEnv() {
  return Boolean(
    process.env.API_BASE_URL &&
    process.env.TEST_USER_EMAIL &&
    process.env.TEST_USER_PASSWORD
  );
}
