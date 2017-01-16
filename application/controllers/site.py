# coding: utf-8
from flask import (render_template,
                   Blueprint, redirect, url_for)
from ..forms import ProductForm, SaleForm
from ..models import Product, db
import json

bp = Blueprint('site', __name__)


@bp.route('/')
@bp.route('/index')
def index():
    """Index page."""
    saleform = SaleForm()
    return render_template('site/index/index.html', saleform=saleform)


@bp.route('/о нас')
def about():
    """About page."""
    saleform = SaleForm()
    return render_template('site/about/about.html', saleform=saleform)


@bp.route('/контакты')
def contacts():
    saleform = SaleForm()
    """Contacts page."""
    return render_template('site/contacts/contacts.html', saleform=saleform)


@bp.route('/<keyword>')
def products(keyword):
    productform = ProductForm()
    saleform = SaleForm()
    product = Product.query.filter_by(category=keyword)
    return render_template('site/products/products.html',
        productform=productform,
        saleform=saleform,
        product=product,
        keyword=keyword)


@bp.route('/delete')
def delete():
    product = Product.query.filter_by(category='Пластиковые шары').first()
    db.session.delete(product)
    db.session.commit()
    
    return redirect(url_for('site.delete'))


@bp.route('/parse')
def parse():
    '''
    db.create_all()
    import csv
    Reader = csv.reader(open('/home/narnik/duralite.csv', newline=''))
    for row in Reader:
        product = Product(name = row[0], specials = row[3], category = row[1], image = row[2])
        db.session.add(product)
        db.session.commit()
    """Parse"""
    
    import csv
    spamReader = csv.reader(open('/home/narnik/Программы/BS4/neoneon/www.neoneon.ru.csv', newline=''))
    for row in spamReader:
        product = Product(name = row[0], specials = row[1], images = row[2], category = row[3])
        db.session.add(product)
        db.session.commit()


    spamReader1 = csv.reader(open('/home/narnik/Программы/BS4/sima-land/sima-land2.csv', newline=''))
    #next(spamReader1)
    for row in spamReader1:
        product = Product(name = row[0], category=row[1], image = row[2],  specials=row[3])
        db.session.add(product)
        db.session.commit()


    from os import listdir
    for i in listdir('/home/narnik/Программы/BS4/sima-land/results/'):
        spamReader2 = csv.reader(open('/home/narnik/Программы/BS4/sima-land/results/' + i, newline=''))
        #next(spamReader2)
        for row in spamReader2:
            product = Product(name = row[0], category=row[1], image = row[2],  specials=row[3])
            db.session.add(product)
            db.session.commit()


    from os import listdir
    for i in listdir('/home/narnikgamarnik/PycharmProjects/my_phyton3_projects/parsers/results/'):
        spamReader3 = csv.reader(open('/home/narnikgamarnik/PycharmProjects/my_phyton3_projects/parsers/results/' + i, newline=''))
        next(spamReader3)
        for row in spamReader3:
            product = Product(name = row[1], image = json.dumps((row[2])), category = row[0], size = row[3])
            db.session.add(product)
            db.session.commit()
    '''
    return render_template('layout.html')

@bp.context_processor
def menu():
    menu = {i.category for i in Product.query.group_by(Product.id, Product.category).all()} 
    return dict(menu=menu)
