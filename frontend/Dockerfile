# Use an official Node.js runtime as a parent image
FROM node:16 as build

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json yarn.lock /app/
RUN yarn install

# Copy the rest of the application code
COPY . /app/

# Build the React app
RUN yarn build

# Use Nginx to serve the built React app
FROM nginx:alpine

# Copy the built React app to Nginx's public folder
COPY --from=build /app/build /usr/share/nginx/html

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]