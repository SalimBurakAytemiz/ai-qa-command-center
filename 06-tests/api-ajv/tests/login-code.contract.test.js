import test from 'node:test';
import assert from 'node:assert/strict';
import loginRequestSchema from '../schemas/login-request.schema.json' with { type: 'json' };
import loginCodeResponseSchema from '../schemas/login-code-response.schema.json' with { type: 'json' };
import { getRequiredEnv, hasLoginCodeEnv } from '../helpers/env.js';
import {
  assertNoNullOrEmptyValues,
  assertNoSensitiveEcho,
  assertResponseTimeBelow,
  assertSchemaValid
} from '../helpers/assert-json-contract.js';

test('login code API returns strict AJV-valid contract response', { skip: !hasLoginCodeEnv() }, async () => {
  const baseUrl = getRequiredEnv('API_BASE_URL').replace(/\/$/, '');
  const email = getRequiredEnv('TEST_USER_EMAIL');
  const password = getRequiredEnv('TEST_USER_PASSWORD');

  const requestBody = {
    email,
    password
  };

  assertSchemaValid({
    schema: loginRequestSchema,
    data: requestBody,
    label: 'Login request'
  });

  const startedAt = Date.now();

  const response = await fetch(`${baseUrl}/api/auth/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(requestBody)
  });

  const responseText = await response.text();

  assert.equal(response.status, 200);
  assertResponseTimeBelow({ startedAt, thresholdMs: Number(process.env.API_RESPONSE_TIME_LIMIT_MS || 200) });
  assertNoSensitiveEcho({ responseText, sensitiveValues: [password] });

  let jsonData;

  try {
    jsonData = JSON.parse(responseText);
  } catch (error) {
    assert.fail(`Response is not valid JSON: ${error.message}`);
  }

  assertSchemaValid({
    schema: loginCodeResponseSchema,
    data: jsonData,
    label: 'Login response'
  });

  assertNoNullOrEmptyValues(jsonData);
});
