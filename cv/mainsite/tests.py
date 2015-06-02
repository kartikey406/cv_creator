"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import docx

def demo():
	 document = docx.newdocument()
	 body = document.xpath('/w:document/w:body', namespaces=docx.nsprefixes)[0]
	 body.add_heading('Document Title')
	 body.save('demo1.docx')


