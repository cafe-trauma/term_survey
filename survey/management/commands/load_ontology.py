from django.core.management.base import BaseCommand, CommandError
from survey.models import Term
from rdflib import graph, RDFS, URIRef, RDF, OWL

class Command(BaseCommand):
    help = 'Load an ontology from a url or file'

    def add_arguments(self, parser):
        parser.add_argument('ontology', help="the ontology to be loaded")
        parser.add_argument('annotation_uri', help="the full URI of the annotation")

    def handle(self, *args, **options):
        g = graph.Graph()
        g.load(options['ontology'])
        annotation = URIRef(options['annotation_uri'])
        annotation_label = g.value(annotation, RDFS.label)
        yN = input("""
Are you sure you want to perform this import
Ontology: {}
Annotation: {}
Annotation Label: {}
[y/N] """.format(options['ontology'], options['annotation_uri'], annotation_label))
        if yN == 'y':
            query = g.query("""PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select ?uri ?label ?annotation {{
    ?uri a owl:Class;
       rdfs:label ?label;
       <{}> ?annotation .
    FILTER NOT EXISTS {{ ?uri owl:deprecated true }} .
}}
            """.format(annotation))
            for (uri, label, annotation_value) in query:
                Term.objects.create(label=label,
                                    annotation=annotation_value,
                                    uri=uri)
        else:
            print('exiting')
