export type TestUser = {
  email: string;
  password: string;
};

export function getDefaultTestUser(): TestUser {
  return {
    email: process.env.TEST_USER_EMAIL || '',
    password: process.env.TEST_USER_PASSWORD || ''
  };
}
