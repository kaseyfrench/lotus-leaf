# Configurations

## config.js

`config.js` is a derived version from `config-example.js` (See `src/frontend/.config-example.js`)

- port: the port running the server (usually 80)
- db
    * name: database name
    * username: user of the database
    * password: password of the database
    * host: host of the database (usually localhost)
    * dialect: type of the database (default mysql)
- mode: `production` or `dev`. Running in `dev`, all the logs will be printed
- session_key: identification of current session
- secrete_ley: used for _csrf verification