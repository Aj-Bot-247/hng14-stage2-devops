# Stage 1: Build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install

# Stage 2: Production
FROM node:18-alpine
WORKDIR /app

# Install curl for the healthcheck
RUN apk add --no-cache curl

# Requirement: fe_named_nonroot_user
RUN adduser -D hng_user
USER hng_user

# Requirement: fe_multi_stage
COPY --from=builder /app/node_modules ./node_modules
COPY . .

# Requirement: fe_healthcheck (Frontend is on port 3000)
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:3000/ || exit 1

EXPOSE 3000
CMD ["npm", "start"]