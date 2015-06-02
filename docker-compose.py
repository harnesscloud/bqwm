web:
  build: .
  links:
   - db
  ports:
   - "80:8000"
db:
  image: mariadb
