### Overview 

Pleaceholder for detecting testing anti-patterns in IaC 

### Contributors

Mehedi Hassan (Lead) , Akond Rahman 

### Details 

> Test Pattern Miner for Ansible(TAMA) 

# What is TAMA
**T**est P**a**ttern **M**iner for **A**nsible  is a tool that identifies testing pattern instances that correlate with the appearance of bugs in Ansible test scripts. TAMA parses the relevant test YAML files of a repository where Ansible has been used and indicates some patterns like `Assertion Roulette`, `Linter Strangler`, `Local Only Testing` and `Remote Mystery Guest`.

# How to Use TAMA
## Pull TAMA
Download docker image from docker hub with below command:

`docker pull talismanic/tama`

## Run TAMA
Run the docker container binding the volume of the IaC (ansible) Project. For example, if project directory is /usr/project/name then we will run the following command:

`docker run -v /usr/project/name:/src -it talismanic/tama`

## Give your project name
TAMA will ask for the name of the project. Give it a name as per your wish.

## Check the findings
TAMA will scan the ansible test files and produce the output in the Ansible project directory. File name convention will be
`projectName_output.csv`


# Supported Tags
As we are under active development, currently we only support the `:latest` tag.

# Maintained By
[Paser Group](https://akondrahman.github.io/paser/)

Tennessee Tech University.



> First step, detect testing anti-patterns 
### Categories which will be focussed:

#### Assertion Roulette
###### Definition 
....Will Be Updated Later....

Example 01:
https://github.com/akondrahman/IaCTesting/blob/18b98460e0c059ad79aee81f2359f3d5d5f863f8/categ_ansible_test_code.txt#L4024
```
    def test_init(self):
        self.assertEqual(self.ml._prefix, 'prefix')
        self.assertEqual(self.ml._delimiter, '.')

        self.assertEqual(self.ml_no_prefix._prefix, '')
        self.assertEqual(self.ml_other_delim._delimiter, '*')
        self.assertEqual(self.ml_default._prefix, '')
```

Example 02:
https://github.com/akondrahman/IaCTesting/blob/18b98460e0c059ad79aee81f2359f3d5d5f863f8/categ_ansible_test_code.txt#L6533
```
    def test_two_ips(self):

        with self.assertRaises(di.MultipleIpForHostError) as context:
            di._check_multiple_ips_to_host(config)
        self.assertEqual(context.exception.current_ip, '192.168.1.1')
        self.assertEqual(context.exception.new_ip, '192.168.1.2')
        self.assertEqual(context.exception.hostname, 'host1')
```
In the above two examples we can see that multiple mention of assertion without proper debug message. So if any of those fails it will not be identifiable which one failed and why failed.


#### Remote Mystery Guest
###### Definition 
....Will Be Updated Later....

Example 01:
https://github.com/akondrahman/IaCTesting/blob/cc4e78aa7af6c3b6ccf5c86e03936b991f4cd36b/categ_ansible_test_code.txt#L5833

```
TARGET_DIR = path.join(os.getcwd(), 'tests', 'inventory')
BASE_ENV_DIR = INV_DIR
CONFIGS_DIR = path.join(os.getcwd(), 'etc', 'openstack_deploy')
CONFD = os.path.join(CONFIGS_DIR, 'conf.d')
AIO_CONFIG_FILE = path.join(CONFIGS_DIR, 'openstack_user_config.yml.aio')
USER_CONFIG_FILE = path.join(TARGET_DIR, 'openstack_user_config.yml')
```
For example in the above variable setup/definition we are seeing that files from external directory is being read.

Example 02:
https://github.com/akondrahman/IaCTesting/blob/cc4e78aa7af6c3b6ccf5c86e03936b991f4cd36b/categ_ansible_test_code.txt#L7587

```
[testenv]
usedevelop = True
install_command =
    pip install -c{env:UPPER_CONSTRAINTS_FILE:https://git.openstack.org/cgit/openstack/requirements/plain/upper-constraints.txt} {opts} {packages}
```
In the above snippet, we are seeing that files from internet is being downloaded for preparing test environment.

#### Local Only Testing

###### Definition 
....Will Be Updated Later....

Example 01:
https://github.com/akondrahman/IaCTesting/blob/fc4e7ab85bf04234869f00d4e4e173c4d488bab1/categ_ansible_test_code.txt#L308
```
- name: Prepare web server on localhost to serve python packages
  hosts: localhost
  connection: local
  become: yes
  any_errors_fatal: yes
  tasks:
    - name: Set venv_build_archive_path and venv_install_source_path
      set_fact:
        venv_build_host_wheel_path: >-
          {%- if ansible_distribution == "Ubuntu" %}
          {%-   set _path = "/var/www/html" %}
          {%- elif ansible_distribution == "CentOS" %}
          {%-   set _path = "/usr/share/nginx/html" %}
          {%- else %}
          {%-   set _path = "/srv/www/htdocs" %}
          {%- endif %}
          {{- _path }}

    
```
 
Example 02:
https://github.com/akondrahman/IaCTesting/blob/fc4e7ab85bf04234869f00d4e4e173c4d488bab1/categ_ansible_test_code.txt#L369
```
- name: Verify not using a build host
  hosts: "container1"
  remote_user: root
  any_errors_fatal: yes
  vars:
    venv_pip_packages:
      - "Jinja2==2.10"
    venv_install_destination_path: "/openstack/venvs/test-venv"
  tasks:

    - name: Execute venv install
      include_role:
        name: "python_venv_build"
        private: yes
      vars:
        venv_facts_when_changed:
          - section: "{{ inventory_hostname }}"
            option: "test"
            value: True
 ```

In the first example we can see that the role *Prepare web server on localhost to serve python packages* is running the task in localhost environment. Whereas in the second example we can see that role *Verify not using a build host* has executed the task in container1 environment. So example 1 has antipattern of testing only in localhost.


#### Linter Strangler
###### Definition 
....Will Be Updated Later....

Example 01:
https://github.com/akondrahman/IaCTesting/blob/fc4e7ab85bf04234869f00d4e4e173c4d488bab1/categ_ansible_test_code.txt#L811

```
    - name: Export NFS
      command: exportfs -rav
      tags:
        - skip_ansible_lint
 ```
 
Example 02:
https://github.com/akondrahman/IaCTesting/blob/fc4e7ab85bf04234869f00d4e4e173c4d488bab1/categ_ansible_test_code.txt#L905

```
    - name: Ensure mount are mounted
      command: grep -w '{{ item }}' /proc/mounts
      with_items:
        - /var/lib/sparse-file
        - /var/lib/test
      tags:
        - skip_ansible_lint
 ```

In the above two examples, we are seeing that a special tag has been added in the task named *skip_ansible_lint*. Essentially this tag tells the ansible_lint module not to perform linting on this task. This can sometime lead to non-standard coding convention or opens the door of coding loophole. 



#### Unit testing anti-pattern catalogues (Reading Resources)

1. Stack Overflow: https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue
2. https://www.yegor256.com/2018/12/11/unit-testing-anti-patterns.html
3. https://arxiv.org/ftp/arxiv/papers/1703/1703.10882.pdf
4. https://github.com/TestSmells/TestSmellDetector
5. https://julien.danjou.info/finding-definitions-from-a-source-file-and-a-line-number-in-python/
