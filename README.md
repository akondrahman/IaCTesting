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

Example:
https://github.com/akondrahman/IaCTesting/blob/18b98460e0c059ad79aee81f2359f3d5d5f863f8/categ_ansible_test_code.txt#L4024
```
    def test_init(self):
        self.assertEqual(self.ml._prefix, 'prefix')
        self.assertEqual(self.ml._delimiter, '.')

        self.assertEqual(self.ml_no_prefix._prefix, '')
        self.assertEqual(self.ml_other_delim._delimiter, '*')
        self.assertEqual(self.ml_default._prefix, '')
```


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


3. Violation of execute and verify
4. Not collecting facts from remote host
5. Mishandled privilege escalation
6. Localhost testing
7. Not cleaning the test tnv
