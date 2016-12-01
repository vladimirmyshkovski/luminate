# coding: utf-8
from flask import (render_template,
                   Blueprint,
                   request,
                   redirect,
                   url_for,
                   jsonify)
from ..utils.mail import mail
from ..forms import ProductForm
from ..models import Product, Contact, db

from flask_mail import Message


bp = Blueprint('mail', __name__, url_prefix='/mail')


@bp.route("/send", methods=['POST', 'GET'])
def send():
    if request.method == "POST":
        
        params = request.form
        email = params['email']
        phone = params['phone']
        id = params['id']
        product_name = Product.query.get(id)
        print('sex')

        db.create_all()
        
        contact = Contact(email = email, phone = phone)
        db.session.add(contact)
        db.session.commit()
        
                
        msg = Message("Заявка" + str(request.url_root),
        sender="SiegHeil@1488.hh",
        recipients=["illumiarts@gmail.com"])
        msg.body = "Заявка со страницы " + str(request.base_url) + "/n" + "E-mail " + str(email) + "/n" + "Phone " + str(phone) + "/n" + "ID" + str(id) + "/n" + "Product name " + str(product_name)
        msg.html = "<h1>Заявка со страницы "  + str(request.base_url)  +  "</h1>" + "<p>E-mail " + str(email) + "</p>" +  "<p>Phone "  + str(phone) + "</p>" + "<p>ID " + str(id) + "</p>" + "<p>Product name " + str(product_name) + "</p>"
        
        mail.send(msg)
                
        return str(request.form)
    else:
        return redirect(url_for('site.index'))
    
    return render_template('site/layout.html')
