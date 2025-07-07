# Step 1: Build the React app
FROM node:20 AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json first (to leverage Docker cache)
COPY movie-explorer-frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app
COPY movie-explorer-frontend/ ./

RUN pwd

EXPOSE 5173

CMD ["npm", "run", "serve"]

