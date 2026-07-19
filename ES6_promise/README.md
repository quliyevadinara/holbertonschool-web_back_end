# ES6 Promises

## Description

This project is part of the Holberton School / ALX Web Back-End specialization. It covers the fundamentals of **JavaScript Promises (ES6)** — creating them, resolving and rejecting them, chaining handlers, combining multiple promises, and handling errors with `try`/`catch`.

By the end of this project, you should be able to explain, without external help:

- Why and how to use Promises
- How to use `then`, `resolve`, and `catch` methods
- How to use every method of the Promise object (`all`, `allSettled`, `race`, etc.)
- How to use `async` / `await`
- How to handle multiple successful promises
- How to handle multiple promises that fail
- How to throw and catch errors with `try` / `catch`

## Repository

- **GitHub repository:** `holbertonschool-web_back_end`
- **Directory:** `ES6_promise`

## Requirements

- All files are executed on Ubuntu 20.04 LTS using Node.js (via `npm run dev` / Babel).
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Code is compliant with `eslint`.

## Setup

```bash
npm install
```

Run any file with:

```bash
npm run dev <filename>.js
```

## Files

| File                    | Description                                                                 |
|-------------------------|-------------------------------------------------------------------------------|
| `0-promise.js`          | Returns an empty resolved `Promise` from `getResponseFromAPI()`.              |
| `1-promise.js`          | Returns a resolved or rejected `Promise` from `getFullResponseFromAPI(success)` depending on the boolean argument. |
| `2-then.js`             | Attaches `then`/`catch`/`finally` handlers to a given promise via `handleResponseFromAPI(promise)`. |
| `3-all.js`              | Uses `Promise.all` to resolve `uploadPhoto` and `createUser` together in `handleProfileSignup()`. |
| `4-user-promise.js`     | Returns a resolved promise with a user object from `signUpUser(firstName, lastName)`. |
| `5-photo-reject.js`     | Returns a rejected promise with an error from `uploadPhoto(fileName)`.        |
| `6-final-user.js`       | Uses `Promise.allSettled` to combine `signUpUser` and `uploadPhoto` results in `handleProfileSignup(firstName, lastName, fileName)`. |
| `7-load_balancer.js`    | Uses `Promise.race` to return the value of whichever promise resolves first in `loadBalancer(chinaDownload, USDownload)`. |
| `8-try.js`              | `divideFunction(numerator, denominator)` throws an error when dividing by 0.  |
| `9-try.js`              | `guardrail(mathFunction)` wraps a function call in `try`/`catch`/`finally` and returns a queue of results/errors. |

## Task Details

### 0. Keep every promise you make and only make promises you can keep
`getResponseFromAPI()` returns a `Promise` (checked via `instanceof Promise`).

### 1. Don't make a promise...if you know you can't keep it
`getFullResponseFromAPI(success)`:
- `true` → resolves with `{ status: 200, body: 'Success' }`
- `false` → rejects with `Error('The fake API is not working currently')`

### 2. Catch me if you can!
`handleResponseFromAPI(promise)` attaches:
- `.then()` → returns `{ status: 200, body: 'success' }`
- `.catch()` → returns an empty `Error` object
- `.finally()` → logs `Got a response from the API`

### 3. Handle multiple successful promises
`handleProfileSignup()` uses `Promise.all([uploadPhoto(), createUser()])` and logs:
```
<photo.body> <user.firstName> <user.lastName>
```
On error, logs `Signup system offline`.

### 4. Simple promise
`signUpUser(firstName, lastName)` returns a resolved promise with `{ firstName, lastName }`.

### 5. Reject the promises
`uploadPhoto(fileName)` returns a promise rejected with `Error('<fileName> cannot be processed')`.

### 6. Handle multiple promises
`handleProfileSignup(firstName, lastName, fileName)` uses `Promise.allSettled` on `signUpUser` and `uploadPhoto`, returning an array of `{ status, value }` objects (where `value` holds the resolved value or the rejection reason).

### 7. Load balancer
`loadBalancer(chinaDownload, USDownload)` uses `Promise.race` to return the value of the first promise to resolve.

### 8. Throw an error
`divideFunction(numerator, denominator)` throws `Error('cannot divide by 0')` if `denominator` is `0`, otherwise returns `numerator / denominator`.

### 9. Throw error / try catch
`guardrail(mathFunction)` executes `mathFunction`, pushing its return value (or the stringified error, if it throws) into a `queue` array, then always pushes `'Guardrail was processed'` before returning the queue.

## Author

Holberton School / ALX Web Back-End student project.