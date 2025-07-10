from flask import Flask,render_template,request
from url_checker import check_url,get_target_ip
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
        target_ip=get_target_ip(url)
        ip_address  =request.remote_addr
        user_agent = request.headers.get ('user-agent')   
        log_scan(check_url, result, target_ip, user_agent)

    # ✅ HERE is Step 4 — show result page
        return render_template("result.html", url=url, result=result,target_ip=target_ip)

    return render_template('index.html',result=result)



if __name__=='__main__':
    app.run(debug=True)



