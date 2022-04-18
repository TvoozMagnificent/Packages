# password
Password validator and generator

Usage: 

command line: `pip3 install password`

python3: `from password import main` and `main()`

output:

```
Generate password? 
>>> yep
Website name? 
>>> numberbasher.onuniverse.com (PLZ visit)
Generated password for numberbasher.onuniverse.com (PLZ visit): "nUmBeRb@$HeR"
Check generated password? 
>>> yes, do that

Your password "nUmBeRb@$HeR" passed EASYTEST. 

Your password "nUmBeRb@$HeR" passed SHORTTEST. 

Your password "nUmBeRb@$HeR" passed COMMONTEST. 
Check your own password? 
>>> yippee!!!
Password? 
>>> Password
Sorry, common phrase #27: "pass" is in password "Password". Password is too easy. 
Sorry, common phrase #28: "word" is in password "Password". Password is too easy. 

Your password "Password" failed EASYTEST. 

Your password "Password" passed SHORTTEST. 
Sorry, password "Password" is the #1 common password. Password is too common. 
Sorry, password "Password" is the #275 common password. Password is too common. 
--snip--
Sorry, password "Password" is in the #958659 common password: "viswaspassword". Password is too common. 
Sorry, password "Password" is in the #969773 common password: "vgpassword". Password is too common. 

Your password "Password" failed COMMONTEST. 
Generate password? 
>>> quit
```



