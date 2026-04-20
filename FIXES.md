# Application Bug Fixes

## 1. `api/main.py`
* **Line 8:** * **Problem:** Redis connection host and port were hardcoded to `localhost` and `6379`. This will fail in a Docker network where Redis is on a separate container.
  * **Fix:** Replaced hardcoded values with `os.getenv("REDIS_HOST", "localhost")` and `os.getenv("REDIS_PORT", 6379)`.

## 2. `worker/worker.py`
* **Line 6:** * **Problem:** Redis connection was hardcoded to `localhost`, preventing cross-container communication.
  * **Fix:** Replaced hardcoded values with `os.getenv("REDIS_HOST", "localhost")` and `os.getenv("REDIS_PORT", 6379)`.
* **Line 4 & 14:** * **Problem:** The `signal` module was imported but unused, and the worker ran on an infinite `while True:` loop, preventing graceful shutdown by Docker orchestrators.
  * **Fix:** Implemented `handle_shutdown` to catch `SIGINT` and `SIGTERM` signals, and changed the loop to `while run_worker:` to allow current jobs to finish before exiting.

## 3. `frontend/app.js`
* **Line 6:** * **Problem:** `API_URL` was hardcoded to `http://localhost:8000`. Inside Docker, `localhost` refers to the frontend container itself, causing API requests to fail.
  * **Fix:** Changed to `const API_URL = process.env.API_URL || "http://localhost:8000";`.
* **Line 29:**
  * **Problem:** Application port was hardcoded to `3000`.
  * **Fix:** Changed to use `process.env.PORT || 3000` to allow dynamic port assignment.

## 4. `api/.env` (Security Risk)
* **Problem:** A `.env` file containing a hardcoded `REDIS_PASSWORD` was left in the `api` directory, violating security practices and risking credential leakage in version control.
  * **Fix:** Untracked the file using `git rm --cached`, added `**/.env` to the root `.gitignore` file, and documented the required variables using placeholder values in `.env.example`.