# coding: utf-8
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import time
import random
import datetime
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from ..models import db, Contact
from ..utils.quere import Queue
import os

update_queue = Queue()

bp = Blueprint('bot', __name__)

bot = telepot.Bot('285591958:AAF5tUpkm1vay_tuV9wwBEPFtC-OPgUJLVI')
bot.setWebhook()


@bp.route('/send', methods=['POST'])
def send():
    if request.method == "POST":
        params = request.form
        email = params['email']
        phone = params['phone']
        id = params['id']
        bot.sendMessage(169641544, phone + "\n" + email)

        request.path == 'mail/send'
        request.method == 'POST'
        request.data == params
    return redirect(url_for('mail.send'))
'''
def get(msg):
    from pprint import pprint
    response = bot.getUpdates()
    pprint(response)
    command = msg['text']
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])



    if command == '/get':
        bot.sendMessage(169641544, 'hello')


bot.message_loop(get, 999)
'''
