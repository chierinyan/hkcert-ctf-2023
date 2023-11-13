```patch
--- solve.py
+++ solve.py
@@ -30,14 +30,12 @@
 
     key_server = b''
 
-    for i in range(16):
-        s = sign(r, b'\0'*(i+1), 'testing')
+    for i in range(2, 18, 2):
+        s = sign(r, b'\0'*(i), 'testing')
 
-        for guess in range(256):
-            key_server_guess = key_server + int.to_bytes(guess, 1, 'big')
-            if sign_message(b'\0'*(i+1), key_server_guess, 'testing') != s: continue
+        for guess in range(256*256):
+            key_server_guess = key_server + int.to_bytes(guess, 2, 'big')
+            if sign_message(b'\0'*(i), key_server_guess, 'testing') != s: continue
             key_server = key_server_guess
             break
         print(f'{key_server = }')
```
