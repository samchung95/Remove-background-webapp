# Use the official Nginx image as Base
FROM nginx:alpine

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy the SSL certificate and key
RUN mkdir -p /etc/nginx/ssl/
COPY server.crt /etc/nginx/ssl/
COPY server.key /etc/nginx/ssl/

# Replace it with our custom Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/
