import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: Number(__ENV.K6_VUS || 1),
  duration: __ENV.K6_DURATION || '30s',
  thresholds: {
    http_req_failed: ['rate<0.05'],
    http_req_duration: ['p(95)<1000']
  }
};

export default function () {
  const baseUrl = __ENV.PERF_BASE_URL;
  const email = __ENV.PERF_TEST_USER_EMAIL;
  const password = __ENV.PERF_TEST_USER_PASSWORD;

  if (!baseUrl || !email || !password) {
    console.log('SKIPPED: PERF_BASE_URL, PERF_TEST_USER_EMAIL, and PERF_TEST_USER_PASSWORD are required.');
    sleep(1);
    return;
  }

  const response = http.post(
    `${baseUrl.replace(/\/$/, '')}/api/auth/login`,
    JSON.stringify({
      email,
      password
    }),
    {
      headers: {
        'Content-Type': 'application/json'
      }
    }
  );

  check(response, {
    'status is 200': (r) => r.status === 200
  });

  sleep(1);
}
