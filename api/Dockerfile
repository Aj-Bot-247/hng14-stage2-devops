# Stage 1: Build
FROM python:3.9-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Production
FROM python:3.9-alpine
WORKDIR /app

# Install curl for the healthcheck
RUN apk add --no-cache curl

# Requirement: named_nonroot_user
RUN adduser -D hng_user
USER hng_user

# Requirement: multi_stage
COPY --from=builder /home/hng_user/.local /home/hng_user/.local
COPY . .

ENV PATH=/home/hng_user/.local/bin:$PATH

# Requirement: healthcheck
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["python", "main.py"]