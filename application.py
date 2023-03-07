# Flask
from flask import Flask, request, render_template, jsonify
#from gevent.pywsgi import WSGIServer
import people_also_ask1
import people_also_ask1.request.session
import random
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# ip_addresses = ["85.237.57.198:44959", "116.0.2.94:43379", "186.86.247.169:39168", "185.132.179.112:1080", "190.61.44.86:9991"]


proxy = ["http://brd-customer-hl_e4d957e0-zone-zone2-country-us:dr5e2sr1rk92",
"http://brd-customer-hl_e4d957e0-zone-zone2-country-am:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225",
"http://brd-customer-hl_e4d957e0-zone-zone2-country-td:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225",
"http://brd-customer-hl_e4d957e0-zone-zone2-country-br:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225",
"http://brd-customer-hl_e4d957e0-zone-zone2-country-cr:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225",
"http://brd-customer-hl_e4d957e0-zone-zone2-country-et:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225",
"http://brd-customer-hl_e4d957e0-zone-zone2-country-gu:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225",
"http://brd-customer-hl_e4d957e0-zone-zone2-country-it:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225",
"http://brd-customer-hl_e4d957e0-zone-zone2-country-kw:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225",
"http://brd-customer-hl_e4d957e0-zone-zone2-country-il:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225",
]

# Declare a flask app
application = Flask(__name__)

print('Model loaded. Check http://127.0.0.1:5000/')


@application.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@application.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        print("python_code")
        inputSearch = request.json['inputSearch']
        inputDepth = request.json['inputDepth']

        if inputDepth == "1":
            
            result = people_also_ask1.get_related_questions(inputSearch, 2)
            dictionary = {k: v for k, v in enumerate(result)}
            return jsonify(result=dictionary)
        elif inputDepth == "2":
            result = []
            # proxy_index = random.randint(0, len(ip_addresses) - 1)
            # proxies = {'http': 'http://203.176.221.40:80'}
            # proxy = {"http":  ip_addresses[proxy_index], "https":  ip_addresses[proxy_index]}
            # proxy[random.randint(0,len(proxy)-1)]]
            people_also_ask1.request.session.set_proxies(
                    proxy

                )
            result1 = people_also_ask1.get_related_questions(inputSearch, 2)
           
            for i in range(len(result1)):
                people_also_ask1.request.session.set_proxies(
                    proxy

                )
                # proxy[random.randint(0,len(proxy)-1)]]
                # proxy_index = random.randint(0, len(ip_addresses) - 1)

                # proxy = {"http": ip_addresses[proxy_index], "https":  ip_addresses[proxy_index]}
                # people_also_ask.request.session.proxies.update(proxies)
                # people_also_ask.request.session.set_proxies(
                #     proxy
                # )
                #result1 = people_also_ask1.get_related_questions(inputSearch, 2)
                # people_also_ask.request.session.set_proxies(
                #     "http://46.101.49.62:80"+ ip_addresses[proxy_index]
                # )
                result2 = people_also_ask1.get_related_questions(result1[i], 2)
                result.append(result2)
            dictionary = dict(zip(result1, result))
            return jsonify(result=dictionary)
        else:
            result_depth1 = []
            result_depth2 = []
            result1 = people_also_ask1.get_related_questions(inputSearch, 2)
            for i in range(len(result1)):
                people_also_ask1.request.session.set_proxies(
                    proxy

                )
                if len(result1[i]) != 0:

                    result2 = people_also_ask1.get_related_questions(result1[i], 2)
                else:
                    result2 = [" ", " ", " "]
                result_depth1.append(result2)
                for j in range(len(result2)):
                    if result2[j] != " ":
                        result3 = people_also_ask1.get_related_questions(result2[j], 2)
                    else:
                        result3 = [" ", " ", " "]
                    result_depth2.append(result3)

            dictionary = dict(zip(result1, result_depth1))
            final_dict = {
                "first" : dictionary,
                "second" : result_depth2
            }
            print(final_dict)
            # final_dict = {"first":{"What does Audi stand for?":["What do the 4 rings in Audi mean?","What is the meaning of Audi?","What does Audi mean in English?"],"Which is better BMW or Audi?":["Which is better BMW or Audi or Mercedes?","Which brand is more reliable BMW or Mercedes or Audi?","Which is more reliable Mercedes or BMW?"],"Who owns Audi in Pakistan?":["Does Audi operate in Pakistan?","Who is the CEO of Audi Pakistan?","Which is better Audi or Mercedes?"]},"second":[["Is Audi reliable than BMW?","Which brand is more reliable BMW or Mercedes or Audi?","Is BMW better quality than Mercedes?"],["What has better reliability BMW or Audi?","Which is best Audi or BMW?","Are BMW's more reliable than Audi's?"],["Why BMW is more reliable than Mercedes?","Is BMW cheaper to maintain than Mercedes?","Which is more reliable BMW or Mercedes?"],[],["What was Audi named for?","How did Audi get its name?","Did Audi copy the Olympics logo?"],["How did Audi get its name?","What is the meaning of Audi?","What car symbol is 5 rings?"],["Who owns Audi in Pakistan?","Is there Audi in Pakistan?","How many Audi cars are there in Pakistan?"],["Where are Audi factories located?","Does Audi have a plant in Pakistan?","Who is the brand ambassador of Pakistan Audi?"],["Which is more luxurious Mercedes or Audi?","Which is better BMW or Audi or Mercedes?","Is Mercedes more luxurious than BMW?"]]}
            return jsonify(result=final_dict)
            

        

    return None


if __name__ == '__main__':
     application.run(port=5002, threaded=False)

    # Serve the app with gevent
   # http_server = WSGIServer(('0.0.0.0', 5000), application)
    #http_server.serve_forever()
