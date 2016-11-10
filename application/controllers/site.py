# coding: utf-8
from flask import (render_template,
                   Blueprint)
from ..forms import ProductForm
from ..models import Product, db
import json

bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    """Index page."""
    return render_template('site/index/index.html')


@bp.route('/about')
def about():
    """About page."""
    return render_template('site/about/about.html')

@bp.route('/<keyword>')
def products(keyword):
    form = ProductForm()
    product = Product.query.filter_by(category=keyword)
    return render_template('site/products/products.html',
                           form=form,
                           product=product)



@bp.route('/parse')
def parse():
    db.create_all()
    
    """Parse"""
    import csv
    '''
    spamReader1 = csv.reader(open('/home/narnik/Программы/BS4/sima-land/sima-land2.csv', newline=''))
    #next(spamReader1)
    for row in spamReader1:
        product = Product(name = row[0], category=row[1], image = row[2],  specials=row[3])
        db.session.add(product)
        db.session.commit()
        
    '''
    from os import listdir
    for i in listdir('/home/narnik/Программы/BS4/sima-land/results/'):
        spamReader2 = csv.reader(open('/home/narnik/Программы/BS4/sima-land/results/' + i, newline=''))
        #next(spamReader2)
        for row in spamReader2:
            product = Product(name = row[0], category=row[1], image = row[2],  specials=row[3])
            db.session.add(product)
            db.session.commit()
    '''
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
    print(menu)
    return dict(menu=menu)
