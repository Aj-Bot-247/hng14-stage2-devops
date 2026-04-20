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

# Copy node_modules from the builder stage
COPY --chown=node:node --from=builder /app/node_modules ./node_modules

# Copy the rest of the frontend application code
COPY --chown=node:node . .

# Switch to the built-in non-root 'node' user
USER node

# Healthcheck: Uses wget (built into Alpine) to check if the frontend is serving pages
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:3000/ || exit 1

# Expose the frontend port
EXPOSE 3000

# Start the Express server
CMD ["npm", "start"]