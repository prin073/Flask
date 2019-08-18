from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Thisisasecret!'

app.config['RECAPTCHA_PUBLIC_KEY'] = '6Ldpf7MUAAAAAJcokZrepH_MwBsMvkU7J0dx9q_t'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Ldpf7MUAAAAAG4AABYWQICoyllHR5tVlhzBXmwO'
# app.config['TESTING'] = True  #set to True to not allow recaptcha as mandatory

from Flask_WTF.WTF import routes
