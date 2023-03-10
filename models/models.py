# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta, datetime


class user(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'
    _description = 'salespop users'

    name = fields.Char()
    user_name = fields.Char()
    mail = fields.Char()
    password = fields.Char()
    num_tel = fields.Integer()
    on_sale = fields.One2many('salespop.product', 'seller')
    valoracion = fields.One2many('salespop.valoracion', 'valoracion_usuario')

class product(models.Model):
    _name = 'salespop.product'
    _description = 'salespop products'

    name = fields.Char()
    price = fields.Integer()
    categoria = fields.Many2one('salespop.category')
    description = fields.Char()
    ubication = fields.Char()
    publication_date = fields.Datetime(readonly=True, default=fields.Datetime.now)
    seller = fields.Many2one('res.partner', ondelete = "cascade")
    foto = fields.One2many('salespop.foto', 'foto_articulo')

class category(models.Model):
    _name = 'salespop.category'
    _description = 'salespop categories'

    name = fields.Selection([('MOTOR', "Motor"), ('INMOBILIARIA', "Inmobiliaria"), ('JUEGOS', "Juegos"), ('INFORMATICA', "Informatica"), ('TELEFONIA', "Telefonia"), ('MODA', "Moda"), ('DEPORTES', "Deportes")], default = 'MOTOR')
    articulo_categoria = fields.One2many('salespop.product', 'categoria')

class valoracion(models.Model):
    _name = 'salespop.valoracion'
    _description = 'salespop valoracion'

    name = fields.Char()
    puntuacion = fields.Selection([('1', "MEDIOCRE"), ('2', "MALO"), ('3', "REGULAR"), ('4', "BUENO"), ('5', "MUY BUENO")], default = '1')
    valoracion_usuario = fields.Many2one('salespop.user', 'valoracion')

class foto(models.Model):
    _name = 'salespop.foto'
    _description = 'salespop foto'

    name = fields.Char()
    url_imagen = fields.Char()
    foto_articulo = fields.Many2one('salespop.product')

class empleado(models.Model):
    _name = 'salespop.empleado'
    _description = 'salespop empleado'

    name = fields.Char()
    email = fields.Char()
    password = fields.Char()




#private String name;
#private int price;
#private String description;
#private String ubication;
#private Categoria categoria;
#private Date fechaPubli;
#private Usuario vendedor;
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
