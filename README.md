# Solteo technical exercise

## Deployment

To deploy this project run

```bash
git clone https://github.com/Wonderworlds/solteo.git
cd solteo
```

## Deployment backend

Docker Deployment (recommended)

```bash
cd backsolteo
make
```

Local deployment

```bash
replace the value in .env to connect the database
flask db init
flask db migrate
flask db upgrade
flask run --host=0.0.0.0
```

Careful of other application using our ports

```bash
Backend Server listen on 5000
```

When the server is running you can use the CRUD API with cURL or Postman

```bash
http://localhost:5000
```

## Deployment frontend

```bash
cd frontsolteo
yarn && yarn dev
```

Careful of other application using our ports

```bash
Frontend Server listen on 3000
```

When the server is running you can access the page in your browser at:

```bash
http://localhost:5000
```

## Stack

- frontend => Nextjs, Axios
- Backend => Flask app with Python

## Authors

- [@wonderworlds](https://www.github.com/wonderworlds)
