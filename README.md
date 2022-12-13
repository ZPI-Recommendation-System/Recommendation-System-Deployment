# Recomendation system deployment suite

## Requirements:
- Docker with docker compose
- Min 2Ghz CPU
- Min 8GB ram
- Min 10 GB Storage


1. Clone repository 
 
`git clone https://github.com/ZPI-Recommendation-System/Recommendation-Deployment.git & cd Recommendation-Deployment`

3. Set up files in `./config` directiory:
  - .backend-env -> Config for backend, don't change db settings if you want to use provided DB, change default admin credentials if you want different admin account login
  - .db-env -> Don't change anything unless you want to change something DB related
  - .scrapper-env -> Don't change anything for default settings. Change CLIENT_ID and CLIENT_SECRET to assign your application. Check details on https://developer.allegro.pl/tutorials/uwierzytelnianie-i-autoryzacja-zlq9e75GdIR     
4. Execute `docker compose build & docker compose up`
5. After a few minutes app should be available on `http://ip_address`. 
-    Frontend is available on `http://ip_address/`
-    Admin panel is available on `http://ip_address/admin`
-    Api is available on `http://ip_address/api`