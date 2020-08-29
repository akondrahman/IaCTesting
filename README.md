### Overview 

Pleaceholder for detecting testing anti-patterns in IaC 

### Contributors

Mehedi Hassan (Lead) , Akond Rahman 

### Details 

> Coming soon 

#### Categories which will be focussed:

##### Assertion Roulette
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


##### External dependency
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

3. Violation of execute and verify
4. Not collecting facts from remote host
5. Mishandled privilege escalation
6. Localhost testing
##### Not cleaning the test tnv
###### Definition 
....Will Be Updated Later....
Example 01:
https://github.com/akondrahman/IaCTesting/blob/b82895f06f85108a76ca27fc3d83cc7c4da4b65b/categ_ansible_test_code.txt#L7480

```
    def tearDown(self):
        test_inventory.cleanup()
 ```
 
 ```
def cleanup():
    for f_name in CLEANUP:
        f_file = path.join(TARGET_DIR, f_name)
        if os.path.exists(f_file):
            os.remove(f_file)
```
In this example, test script is actually calling a cleanup() function which is ultimately removing the test files from the redirectory. But in any scenarios we see that set environment has not been properly cleaned up after testing is completed or before starting testing.
8. Sensitive data leakage
