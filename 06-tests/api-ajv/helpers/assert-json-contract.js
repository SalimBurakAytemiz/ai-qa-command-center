import assert from 'node:assert/strict';
import Ajv from 'ajv';
import addFormats from 'ajv-formats';

export function createAjv() {
  const ajv = new Ajv({
    allErrors: true,
    strict: true,
    removeAdditional: false
  });

  addFormats(ajv);

  return ajv;
}

export function assertSchemaValid({ schema, data, label }) {
  const ajv = createAjv();
  const validate = ajv.compile(schema);
  const valid = validate(data);

  if (!valid) {
    const errors = ajv.errorsText(validate.errors, { separator: '\n' });
    assert.fail(`${label} schema validation failed:\n${errors}`);
  }
}

export function findNullOrEmptyValues(value, path = '$', errors = []) {
  if (value === null) {
    errors.push(`${path} is null`);
    return errors;
  }

  if (typeof value === 'string' && value.trim() === '') {
    errors.push(`${path} is an empty string`);
    return errors;
  }

  if (Array.isArray(value)) {
    if (value.length === 0) {
      errors.push(`${path} is an empty array`);
      return errors;
    }

    value.forEach((item, index) => {
      findNullOrEmptyValues(item, `${path}[${index}]`, errors);
    });

    return errors;
  }

  if (typeof value === 'object' && value !== null) {
    Object.entries(value).forEach(([key, nestedValue]) => {
      findNullOrEmptyValues(nestedValue, `${path}.${key}`, errors);
    });
  }

  return errors;
}

export function assertNoNullOrEmptyValues(data) {
  const errors = findNullOrEmptyValues(data);

  assert.equal(
    errors.length,
    0,
    `Response contains null or empty values:\n${errors.join('\n')}`
  );
}

export function assertResponseTimeBelow({ startedAt, thresholdMs }) {
  const durationMs = Date.now() - startedAt;

  assert.ok(
    durationMs < thresholdMs,
    `Response time expected below ${thresholdMs}ms but got ${durationMs}ms`
  );
}

export function assertNoSensitiveEcho({ responseText, sensitiveValues }) {
  const lowerResponse = responseText.toLowerCase();

  for (const value of sensitiveValues) {
    if (!value) continue;

    assert.ok(
      !lowerResponse.includes(String(value).toLowerCase()),
      'Response body must not echo sensitive request values.'
    );
  }
}
