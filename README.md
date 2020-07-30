# Cert
Cert service is one-stop and full life cycle ssl/tls certificate management system for hybrid cloud (AWS, Azure, Ali, DataCenter, etc.)


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

Cert service which is one-stop and full life cycle ssl/tls certificate management system for hybrid cloud can upload certificate to database, and then deploy it to differenet target which you want.

With Cert:
* Certificate management
* Domain management
* Certificate scan
* PrivateKey management
* Target management
* Target operation management
* Target adapter layer

### Built With
* [Nameko](https://github.com/nameko/nameko)
* [RabbitMQ](https://www.rabbitmq.com/)
* [pyOpenSSL](https://pypi.org/project/pyOpenSSL/)



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
* pyOpenSSL
```
pip install -r requirements.txt
```

### Installation

1. Clone the repo
```
git clone https://code-management.mercedes-benz.com.cn/oap2/cert-service.git
```
2. Start the service
```
cd cert-service
bash bin/Entrypoint.sh 
```
3. Test functions in your service or nameko shell cli
```
nameko shell
```

<!-- USAGE EXAMPLES -->
## Usage
In nameko shell
```python
n.rpc.cert_service.verify_cert(
			cert_body = open('tests/dsd-cn.i.daimler.com.crt').read(),
			cert_pk = open('tests/dsd-cn.i.daimler.com.key').read()
			)
...
n.rpc.cert_service.verify_cert_chain(
			cert_body = open('tests/dsd-cn.i.daimler.com.crt').read(),
			trusted_cas = [open('tests/QuoVadis_Root_CA_2_G3.crt').read()]
			)
...
n.rpc.cert_service.parse_cert(
            cert_body = open('tests/dsd-cn.i.daimler.com.crt').read()
            )
...
n.rpc.cert_service.upload_cert(
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