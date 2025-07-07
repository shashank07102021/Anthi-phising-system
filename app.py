from flask import Flask,render_template,request
from url_checker import check_url
from flask import request
import csv
from datetime import datetime

app=Flask(__name__)
def log_scan(url, result, ip_address, user_agent):
    with open("scan_log.csv", "a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), url, result, ip_address, user_agent])
                        
 

@app.route('/' ,methods=['GET','POST'])
def home():
    result=None
    if request.method =='POST':
        url=request.form['url']
        result=check_url(url)

        ip_address  =request.remote_addr
        user_agent = request.headers.get ('usre-agent')   
        log_scan(check_url, result, ip_address, user_agent)

    # ✅ HERE is Step 4 — show result page
        return render_template("result.html", url=check_url, result=result)

    return render_template('index.html',result=result)



if __name__=='__main__':
    app.run(debug=True)



