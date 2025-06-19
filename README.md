# API_UI
UI to use Aizon api with reflex

Configure a Conda environment with Python 3.11, reflex & bigfiniteAPIclient (https://github.com/aizon-acs/solutions-platform-api-client.git)

REFLEX: https://reflex.dev/docs/getting-started/introduction/

pip isntall reflex

bigfiniteAPIclient: Follow the instructions on repository


Active conda environment
Init de DB using:
  - reflex db init (Create the database -sqlite-)
  - reflex db makemigrations (Write thes migration scripts)
  - reflex db migrate (Execute the migration script)
  - reflex run (start server)

Click on Login and them Register: 
- The user must be the same one used to connect to the API. Generally, the rule is NameSurname. It must match the one used in the CFG file.
- The cfg file will be searched for in: /Users/<<user>>/.config/BigfiniteAPIClient (hide file)
- In the assets folder you must place a file called First Name Last Name.JPG of the registered users so that the photo is recognized

Consult with an administrator to add more environments to the environment combo on the Entities CRUD page.
The configuration page will search for the CFG file in the detailed location and you can configure existing environments (even new ones must be created manually).
The configuration page will search for the CFG file in the specified location, and you can configure existing environments (even new ones must be created manually).
It will default to the username you registered.
Please note that the file has been modified so it may affect the use of the bigfiniteAPIclient in other projects.

And remember that if you are not in the AIZON offices you will need to connect the VPN