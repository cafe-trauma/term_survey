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
        yN = input("""Are you sure you want to perform this import
Ontology: {}
Annotation: {}
Annotation Label: {}
[y/N]""".format(options['ontology'], options['annotation_uri'], annotation_label))
        if yN == 'y':
            for (uri, RDF.type, OWL.Class) in g:
                label = g.value(uri, RDFS.label)
                annotation_value = g.value(uri, annotation)
                if label != None and annotation_value != None:
                    print('{} - {}'.format(label, annotation_value))
                    Term.objects.create(label=label,
                                        annotation=annotation_value,
                                        uri=uri)
        else:
            print('exiting')
