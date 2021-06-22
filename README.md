# Api-Gateway
Api-Gateway service is reverse proxy for http request from frontend and forward it to backend http or rpc api.


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project

Api-Gateway service is reverse proxy for http request from frontend and forward it to backend http or rpc api if have corresponding permession.

With Rest-API:
* HTTP Proxy
* RPC proxy
* Authorization

### Built With
* [Nameko](https://github.com/nameko/nameko)
* [RabbitMQ](https://www.rabbitmq.com/)
* [PyJwt](https://pypi.python.org/pypi/PyJwt)
* [cryptography](https://pypi.python.org/pypi/cryptography)



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* nameko
```
pip install nameko
```
* rabbitmq
```
docker run -d --hostname amqp_local --name amqp_local -p 15672:15672 -p 5672:5672 --restart=always rabbitmq:3-management
```
* PyJwt and cryptography
```
pip install -r requirements.txt
```
* Get bearer token for authorization
```
https://ittz-tech-platform.cn.svc.corpintra.net/api/auth/login
```
* Add IAM policy to corresponding user
``` 
{"actions":"post,get","resource":"aws:cn-north-1:oap:oap:sansec-service:decrypt_data","condition":"true","effect":true}
``` 

### Installation

1. Clone the repo
```
git clone https://github.com/liusushimeng/api-gateway.git
```
2. Start the service
```
cd api-gateway
bash bin/Entrypoint.sh 
```
3. Test functions in your service or postman
```
postman
```

<!-- USAGE EXAMPLES -->
## Usage
In Postman

```python
for http proxy
URL: http://oap2.cn.bg.corpintra.net/api/h/<devops-service-name>/<path>
Method: POST/GET
...
for rpc proxy
http://oap2.cn.bg.corpintra.net/api/r/<backend_service>/<backend_service_rpc_method>
method: POST/GET
...
http://oap2.cn.bg.corpintra.net/api/r/sansec_service/decrypt_data

post json

{
"cert_content": "user cert content",
"encrypted_datakey": "user encrypted data key",
"encrypted_data": "your encrypted data"
}

```



In code
```python
...
import requests
...
    req_url = "http://oap2.cn.bg.corpintra.net/api/r/sansec_service/decrypt_data"
    req_headers = {}
    req_headers['Content-Type'] = "application/json"

    request_data = {
        "encrypted_data": "your encrypted data",
        "cert_content": "user cert content",
        "encrypted_datakey": "user encrypted data key"
    }

    response = requests.post(
        req_url,
        data=json.dumps(request_data), headers=req_headers,
        verify=False)

```

<!-- ROADMAP -->
## Roadmap

* Add support for dynamic loading config when backend rpc service register

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

 This project is licensed under the GNU General Public License v3.0. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Wei Wang  359703299@qq.com

Project Link: [api-gateway](https://github.com/liusushimeng/api-gateway.git)
