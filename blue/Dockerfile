# Use official NGINX image as the base
FROM nginx:latest

# Remove default nginx.conf (optional but safer)
RUN rm /etc/nginx/conf.d/default.conf || true

# Copy your custom nginx.conf into the container
COPY nginx.conf /etc/nginx/nginx.conf

# Copy your custom index.html into the NGINX web root
COPY index-blue.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Run NGINX in foreground (so container stays alive)
CMD ["nginx", "-g", "daemon off;"]
