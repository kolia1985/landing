import os
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def landingpage():
    agencies = [
        {
            'name': 'Ergonized',
            'logo': 'https://odesk-prod-portraits.s3.amazonaws.com/Companies:1046958:CompanyLogoURL?AWSAccessKeyId=1XVAX3FNQZAFC9GJCFR2&Expires=2147483647&Signature=5Pc4IlYtySpTBPzdHA2kEs9jorA%3D&1447238772',
            'job_success': '100',
            'description': 'php development, WordPress, Yii, Symphony, Mobile Applications',
            'total_jobs': 256,
            'location': 'Ukraine',
            'profile_url': 'https://www.upwork.com/companies/~01a5ddd182baca1686',
            'review': 'The company has done a superb work for us. The engineers we dealt with are top-notch professionals.',
            'skills': ['php', 'WordPress']
        }
    ] * 8
    context = {'agencies': agencies}
    return render_template('landing.html', **context)
