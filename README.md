# Recomendation system deployment suite

## Requirements:
- Docker with docker compose
- Min 2Ghz CPU
- Min 8GB ram
- Min 10 GB Storage


1. Clone repository 
 
`git clone https://github.com/ZPI-Recommendation-System/Recommendation-Deployment.git & cd Recommendation-Deployment`

2. Set up files in `./config` directiory:
  - .backend-env -> Config for backend, don't change db settings if you want to use provided DB, change default admin credentials if you want different admin account login
  -  .db-env -> Don't change anything unless you wanna change something DB related
  -  .frontend-env -> Change to the address where API will be available (default same address as site /api). For local testing you can setup `localhost/api`
  -  .scrapper-env -> Don't change anything for default settings
  -  .admin-env -> 
     -  Change REACT_APP_API_URL to address where API will be available (default same address as site + /api). You can set this up to `localhost/api` for local testing
     -  Change PUBLIC_URL for a direct address to your site (default same addess as site + /admin). You can set this up to `localhost/admin` for local testing
3. Execute `docker compose build & docker compose up`
4. After a few minutes app should be available on `http://ip_address`. 
-    Admin panel is available on `http://ip_address/admin`.   
-    Api is available on `http://ip_address/api`