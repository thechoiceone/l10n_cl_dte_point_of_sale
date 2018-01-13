from odoo import http
from odoo.addons.web.controllers.main import serialize_exception
import logging

_logger = logging.getLogger(__name__)
try:
    from odoo.addons.l10n_cl_fe.controllers.downloader import *
except:
    _logger.warning('No se puede cargar l10n_cl_fe')

class Binary(http.Controller):

    @http.route(["/download/xml/boleta/<model('pos.order'):rec_id>"], type='http', auth='user')
    @serialize_exception
    def download_book(self, rec_id, **post):
        filename = ('%s_%s.xml' % (rec_id.sii_document_class.sii_code, rec_id.sii_document_number)).replace(' ','_')
        filecontent = rec_id.sii_xml_request
        return document(filename, filecontent)
