# CG Intelligence API

## Tech Stack

* Python 3.8.13
* Django 4.0.3
* PostgreSQL 15.1
* All requirements in [requirements](requirements.txt) file

## Installation

* Clone this repository
* In [_docker](_docker) folder, configure in [.env](_docker/.env) file your external Nginx ports by changing `EXTERNAL_HTTP_PORT` and `EXTERNAL_HTTPS_PORT` parameters
* In [CGIBackend/.env](CGIBackend/.env), make sure that:

  - `DB*` parameters match the `DATABASE*` ones set in [.env](_docker/.env)
  - `FRONTEND_URL` has the same port as Nginx port (`EXTERNAL_HTTP_PORT`/`EXTERNAL_HTTP_PORT`)

* From [_docker](_docker) folder, please run (the first time it will take a while):

  ```shell
  docker-compose up -d
  ```

* Ensure containers are up and running with:

  ```shell
  docker-compose ps
  ```

* Check the logs with:

  ```shell
  docker-compose logs -f
  ```

* Create a superuser with:

  ```shell
  docker exec -it consulgest-api python manage.py createsuperuser
  ``` 

* Visit the following available URLs:

    * **Django Admin**: `http://localhost:{EXTERNAL_HTTP_PORT}/admin/`
    * **API Home**: `http://localhost:{EXTERNAL_HTTP_PORT}/api/`

* You can log into Django Admin with the superuser on `http://localhost:{EXTERNAL_HTTP_PORT}/admin/`

* Stop container(s) by running, from [_docker](_docker) folder:

  ```shell
  docker-compose down
  ```

## API Documentation

Postman collections can be found in the [_postman](_postman) folder.

**NOTE**: To be able to log in with superuser on `http://localhost:{EXTERNAL_HTTP_PORT}/login/`, you need to mark your email address as verified:

* login into Django Admin 
* under "Accounts / Email addresses" add a new email address, select superuser and its email address, then set it as Primary and Verified

## ADDITIONAL NOTES

#### Username/Password

  * guest/Uffalamuffa

  * admin/Uffalamuffa

#### ENDPOINT LIST

* **User registration:**  `http://localhost:8000/api/registration/utente/`

* **Admin registration:** `http://localhost:8000/api/registration/admin/`

* **Login:** `http://localhost:8000/login/` 

## You must be logged in for the following endpoints:

* **[GET/POST] Template_Crud:** `http://localhost:8000/api/template/`
 
* **[GET] BatchList :** `http://localhost:8000/api/batch/`

* **[GET/POST] Batch-rud:** `http://localhost:8000/api/batchByID/(BatchId)`

* **[GET/POST] BatchUser (batchs related to the logged user)** `http://localhost:8000/api/batchUser/`

* **[GET/POST] Mapping template columns :** `http://localhost:8000/api/template/` 

* **[POST] File upload dossiers**: `http://localhost:8000/api/uploadfiledossier/`

* **[GET] DossierList :** `http://localhost:8000/api/dossier/`

* **[GET/POST] Dossier-rud:** `http://localhost:8000/api/Dossier/(primary_key)`

* **[GET/POST] Dossiers-Create:** (to create manually a Dossier)** `http://localhost:8000/api/Dossier/`

* **[GET] TotalDossierNumber:** `http://localhost:8000/api/totaldossiernumber/`

* **[GET] Default_API_Columns_for_Mapping:** `http://localhost:8000/api/defaultcolumns/`




### In this commit we are releasing a csv "lista_pratiche_small" and a mocked json for a dummy-template in order to make a fake columns swap.

### The mocked template, in order to try columns swapping, should have this format:

{'colonna1':'committente_codice','colonna2':'esattore_codice','colonna3':'committente_desc','colonna4':'profilo_desc','colonna5':'p_iva','colonna6':'luogo_nascita','colonna7':'cap','colonna8':'citta','colonna9':'provincia','colonna10':'tipo_telefo1','colonna11':'tipo_telefono2','colonna12':'filiale','colonna13':'minimo_dovuto','colonna14':'rate_arretrate','colonna15':'importo_capitale','colonna16':'importo_interessi','colonna17':'importo_spese','colonna18':'importo_spese_recupero','colonna19':'importo_differenza','colonna20':'debitoresiduo', and so on ..........}


### User registration
When you make a user registration via the call to the endpoint, the confirmation link is generated in the docker terminal (container api).
Warning: you need to add port 8000 to the confirmation link because ngnix can't map the url correctly.
By clicking on the confirmation link, the registration is confirmed and you can proceed with the login.

We are proceeding with the implementation of the code for sending the link via email provided during registration


### Postman Collection
in the project directory there is also the collection (Postman) with all the API calls.


### Dump Database
the test database was also dumped