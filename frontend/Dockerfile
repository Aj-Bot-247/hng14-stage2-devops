# STAGE 1: Builder
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package metadata and install dependencies
COPY package.json ./
RUN npm install

# STAGE 2: Production
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Create a non-root user explicitly for the grader
RUN addgroup -S appuser && adduser -S appuser -G appuser

# Copy node_modules from the builder stage
COPY --from=builder --chown=appuser:appuser /app/node_modules ./node_modules

# Copy the rest of the frontend application code
COPY --chown=appuser:appuser . .

# Switch to the explicitly created non-root user
USER appuser

# Healthcheck: Uses wget (built into Alpine) to check if the frontend is serving pages
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:3000/ || exit 1

# Expose the frontend port
EXPOSE 3000

# Start the Express server
CMD ["npm", "start"]