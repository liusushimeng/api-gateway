# Rest-API
Rest-API service is reverse proxy for http request from frontend and forward it to backend http or rpc api.


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

Rest-API service is reverse proxy for http request from frontend and forward it to backend http or rpc api if have corresponding permession.

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

### Installation

1. Clone the repo
```
git clone https://code-management.mercedes-benz.com.cn/oap2/rest-api-service.git
```
2. Start the service
```
cd rest-api-service
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
...
for rpc proxy
http://oap2.cn.bg.corpintra.net/api/r/<backend_service>/<backend_service_rpc_method>

```



In code
```python
...
from nameko.standalone.rpc import ClusterRpcProxy
...
nameko_proxy_config = {
    'AMQP_URI': "pyamqp://<user>:<pw>@127.0.0.:5672"
}
...
with ClusterRpcProxy(nameko_proxy_config) as cluster_rpc:
    resp = cluster_rpc.cert_service.\
        upload_cert(
			project = 'OABDOS',
			stage = 'Prod',
			platform = 'AWS',
			owner_mails = 'mengyun.tian@daimler.com',
			admin_mails = 'wei.f.wang@daimler.com,ruoran.li@daimler.com',
			cert_body = open('tests/dsd-cn.i.daimler.com.crt').read(),
			cert_pk = open('tests/dsd-cn.i.daimler.com.key').read(),
			cert_chain = open('tests/QuoVadis_Global_SSL_ICA_G3.crt').read(),
			cert_rootca = open('tests/QuoVadis_Root_CA_2_G3.crt').read()
			)
...
with ClusterRpcProxy(nameko_proxy_config) as cluster_rpc:
    resp = cluster_rpc.cert_service.\
        convert_cert(
        	src_cert = open('tests/dsd-cn.i.daimler.com.crt').read(),
        	src_cert_type = 'pem',
        	dest_cert_type = 'der',
        	dest_cert_path = '/Users/enroll/Downloads'
        )

```

<!-- ROADMAP -->
## Roadmap

* Add support for target operation management
* Add support for target adapter layer for AWS, Azure, OS

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

ITT/Z Cloud Team - ittz-cloud@daimler.com

Project Link: [cert-service](https://code-management.mercedes-benz.com.cn/oap2/cert-service.git)