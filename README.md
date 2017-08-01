# term_survey
This is a survey tool for having people review annotations such as definitions for an OWL Ontology.

## Installation and Use
This is a django project and should be setup/run in with the standard method according to their documentation.

The short version is
* Clone repo
* Create virtualenv, and install requirements
* `./manage migrate` to create the database
* `./manage load_ontology [http://link.to/ontology.owl] [URI for annotation]` import terms and annotation from an ontology
* `./manage createsuperuser` create a user for yourself
* `./manage runserver` visit `http://localhost:8000/admin` and log in with credentials just created
* Create a single entry in the Settings model via the admin interface
* Send users a link to the base page and they can begin to review terms.
